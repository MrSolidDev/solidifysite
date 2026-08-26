from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload, with_loader_criteria

from app.dependencies import DbSession
from app.models import CaseStudy, Project, PublicationStatus, Technology
from app.schemas import CaseStudyRead, ProjectRead, TechnologyRead

router = APIRouter()


@router.get("/projects", response_model=list[ProjectRead])
def list_projects(db: DbSession, featured: bool | None = None) -> list[Project]:
    query = (
        select(Project)
        .where(Project.publication_status == PublicationStatus.published)
        .options(
            selectinload(Project.technologies),
            selectinload(Project.media),
            selectinload(Project.case_studies),
            with_loader_criteria(CaseStudy, CaseStudy.publication_status == PublicationStatus.published),
        )
        .order_by(Project.featured.desc(), Project.published_at.desc())
    )
    if featured is not None:
        query = query.where(Project.featured == featured)
    return list(db.scalars(query).all())


@router.get("/projects/{slug}", response_model=ProjectRead)
def get_project(slug: str, db: DbSession) -> Project:
    project = db.scalar(
        select(Project)
        .where(Project.slug == slug, Project.publication_status == PublicationStatus.published)
        .options(
            selectinload(Project.technologies),
            selectinload(Project.media),
            selectinload(Project.case_studies),
            with_loader_criteria(CaseStudy, CaseStudy.publication_status == PublicationStatus.published),
        )
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/case-studies", response_model=list[CaseStudyRead])
def list_case_studies(db: DbSession) -> list[CaseStudy]:
    query = (
        select(CaseStudy)
        .where(CaseStudy.publication_status == PublicationStatus.published)
        .options(selectinload(CaseStudy.project).selectinload(Project.technologies))
        .order_by(CaseStudy.published_at.desc())
    )
    return list(db.scalars(query).all())


@router.get("/case-studies/{slug}", response_model=CaseStudyRead)
def get_case_study(slug: str, db: DbSession) -> CaseStudy:
    study = db.scalar(
        select(CaseStudy)
        .where(CaseStudy.slug == slug, CaseStudy.publication_status == PublicationStatus.published)
        .options(selectinload(CaseStudy.project).selectinload(Project.technologies))
    )
    if not study:
        raise HTTPException(status_code=404, detail="Case study not found")
    return study


@router.get("/technologies", response_model=list[TechnologyRead])
def list_technologies(db: DbSession) -> list[Technology]:
    return list(db.scalars(select(Technology).order_by(Technology.name)).all())
