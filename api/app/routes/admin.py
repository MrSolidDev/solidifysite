import uuid
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, Response, UploadFile, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload

from app.dependencies import AdminAccess, DbSession
from app.config import get_settings
from app.models import CaseStudy, Project, ProjectMedia, Technology
from app.schemas import (
    CaseStudyCreate, CaseStudyRead, CaseStudyUpdate, MediaCreate, MediaRead,
    ProjectCreate, ProjectRead, ProjectUpdate, TechnologyCreate, TechnologyRead,
)

router = APIRouter(dependencies=[])


def image_suffix(header: bytes) -> str | None:
    if header.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if header.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if header.startswith((b"GIF87a", b"GIF89a")):
        return ".gif"
    if len(header) >= 12 and header[:4] == b"RIFF" and header[8:12] == b"WEBP":
        return ".webp"
    return None


def project_or_404(project_id: uuid.UUID, db: DbSession) -> Project:
    project = db.scalar(select(Project).where(Project.id == project_id).options(selectinload(Project.technologies), selectinload(Project.media), selectinload(Project.case_studies)))
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


def commit(db: DbSession) -> None:
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=409, detail="Slug, name, relation or media order already exists") from exc


def stored_media_path(url: str) -> Path | None:
    if not url.startswith("/uploads/"):
        return None
    upload_root = Path(get_settings().upload_directory).resolve()
    candidate = (upload_root / url.removeprefix("/uploads/")).resolve()
    return candidate if upload_root in candidate.parents else None


@router.get("/projects", response_model=list[ProjectRead])
def list_all_projects(_: AdminAccess, db: DbSession) -> list[Project]:
    query = select(Project).options(selectinload(Project.technologies), selectinload(Project.media), selectinload(Project.case_studies)).order_by(Project.updated_at.desc())
    return list(db.scalars(query).all())


@router.post("/projects", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate, _: AdminAccess, db: DbSession) -> Project:
    data = payload.model_dump(exclude={"technology_ids"}, mode="json")
    project = Project(**data)
    if payload.technology_ids:
        project.technologies = list(db.scalars(select(Technology).where(Technology.id.in_(payload.technology_ids))).all())
        if len(project.technologies) != len(set(payload.technology_ids)):
            raise HTTPException(status_code=422, detail="One or more technologies do not exist")
    db.add(project)
    commit(db)
    return project_or_404(project.id, db)


@router.patch("/projects/{project_id}", response_model=ProjectRead)
def update_project(project_id: uuid.UUID, payload: ProjectUpdate, _: AdminAccess, db: DbSession) -> Project:
    project = project_or_404(project_id, db)
    changes = payload.model_dump(exclude_unset=True, exclude={"technology_ids"}, mode="json")
    for key, value in changes.items():
        setattr(project, key, value)
    if payload.technology_ids is not None:
        technologies = list(db.scalars(select(Technology).where(Technology.id.in_(payload.technology_ids))).all())
        if len(technologies) != len(set(payload.technology_ids)):
            raise HTTPException(status_code=422, detail="One or more technologies do not exist")
        project.technologies = technologies
    commit(db)
    return project_or_404(project.id, db)


@router.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: uuid.UUID, _: AdminAccess, db: DbSession) -> Response:
    project = project_or_404(project_id, db)
    stored_files = [path for media in project.media if (path := stored_media_path(media.url))]
    db.delete(project)
    commit(db)
    for stored_file in stored_files:
        stored_file.unlink(missing_ok=True)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/technologies", response_model=TechnologyRead, status_code=status.HTTP_201_CREATED)
def create_technology(payload: TechnologyCreate, _: AdminAccess, db: DbSession) -> Technology:
    technology = Technology(**payload.model_dump())
    db.add(technology)
    commit(db)
    db.refresh(technology)
    return technology


@router.post("/projects/{project_id}/media", response_model=MediaRead, status_code=status.HTTP_201_CREATED)
def create_media(project_id: uuid.UUID, payload: MediaCreate, _: AdminAccess, db: DbSession) -> ProjectMedia:
    project_or_404(project_id, db)
    media = ProjectMedia(project_id=project_id, **payload.model_dump())
    db.add(media)
    commit(db)
    db.refresh(media)
    return media


@router.post("/projects/{project_id}/media/upload", response_model=MediaRead, status_code=status.HTTP_201_CREATED)
def upload_media(
    project_id: uuid.UUID,
    _: AdminAccess,
    db: DbSession,
    file: UploadFile = File(),
    alt: str = Form(default=""),
    sort_order: int = Form(default=0),
) -> ProjectMedia:
    project_or_404(project_id, db)
    first_chunk = file.file.read(1024 * 1024)
    suffix = image_suffix(first_chunk)
    if not suffix:
        raise HTTPException(status_code=415, detail="Only JPEG, PNG, WebP and GIF images are allowed")
    if len(alt) > 300 or sort_order < 0:
        raise HTTPException(status_code=422, detail="Invalid media metadata")

    settings = get_settings()
    relative_directory = Path("projects") / str(project_id)
    target_directory = Path(settings.upload_directory) / relative_directory
    target_directory.mkdir(parents=True, exist_ok=True)
    target = target_directory / f"{uuid.uuid4().hex}{suffix}"
    total = 0
    try:
        with target.open("xb") as output:
            total = len(first_chunk)
            if total > settings.max_upload_bytes:
                raise HTTPException(status_code=413, detail="Image exceeds the configured size limit")
            output.write(first_chunk)
            while chunk := file.file.read(1024 * 1024):
                total += len(chunk)
                if total > settings.max_upload_bytes:
                    raise HTTPException(status_code=413, detail="Image exceeds the configured size limit")
                output.write(chunk)
    except Exception:
        target.unlink(missing_ok=True)
        raise
    finally:
        file.file.close()

    media = ProjectMedia(
        project_id=project_id,
        type="image",
        url=f"/uploads/{relative_directory.as_posix()}/{target.name}",
        alt=alt,
        sort_order=sort_order,
    )
    db.add(media)
    try:
        commit(db)
    except Exception:
        target.unlink(missing_ok=True)
        raise
    db.refresh(media)
    return media


@router.delete("/media/{media_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_media(media_id: uuid.UUID, _: AdminAccess, db: DbSession) -> Response:
    media = db.get(ProjectMedia, media_id)
    if not media:
        raise HTTPException(status_code=404, detail="Media not found")
    stored_file = stored_media_path(media.url)
    db.delete(media)
    commit(db)
    if stored_file:
        stored_file.unlink(missing_ok=True)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/case-studies/{study_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_case_study(study_id: uuid.UUID, _: AdminAccess, db: DbSession) -> Response:
    study = db.get(CaseStudy, study_id)
    if not study:
        raise HTTPException(status_code=404, detail="Case study not found")
    db.delete(study)
    commit(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/case-studies", response_model=list[CaseStudyRead])
def list_all_case_studies(_: AdminAccess, db: DbSession) -> list[CaseStudy]:
    query = select(CaseStudy).options(selectinload(CaseStudy.project).selectinload(Project.technologies)).order_by(CaseStudy.updated_at.desc())
    return list(db.scalars(query).all())


@router.post("/case-studies", response_model=CaseStudyRead, status_code=status.HTTP_201_CREATED)
def create_case_study(payload: CaseStudyCreate, _: AdminAccess, db: DbSession) -> CaseStudy:
    if not db.get(Project, payload.project_id):
        raise HTTPException(status_code=422, detail="Project does not exist")
    study = CaseStudy(**payload.model_dump())
    db.add(study)
    commit(db)
    return db.scalar(select(CaseStudy).where(CaseStudy.id == study.id).options(selectinload(CaseStudy.project).selectinload(Project.technologies)))


@router.patch("/case-studies/{study_id}", response_model=CaseStudyRead)
def update_case_study(study_id: uuid.UUID, payload: CaseStudyUpdate, _: AdminAccess, db: DbSession) -> CaseStudy:
    study = db.get(CaseStudy, study_id)
    if not study:
        raise HTTPException(status_code=404, detail="Case study not found")
    for key, value in payload.model_dump(exclude_unset=True, mode="json").items():
        setattr(study, key, value)
    commit(db)
    return db.scalar(select(CaseStudy).where(CaseStudy.id == study.id).options(selectinload(CaseStudy.project).selectinload(Project.technologies)))
