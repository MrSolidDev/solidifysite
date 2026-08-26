import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from app.models import PublicationStatus


class ORMModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class LoginRequest(BaseModel):
    email: str = Field(min_length=3, max_length=320)
    password: str = Field(min_length=8, max_length=200)


class UserRead(ORMModel):
    id: uuid.UUID
    email: str


class TechnologyCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    slug: str = Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$", max_length=100)
    icon: str | None = Field(default=None, max_length=500)


class TechnologyRead(TechnologyCreate, ORMModel):
    id: uuid.UUID


class MediaCreate(BaseModel):
    type: str = Field(pattern=r"^(image|video|demo)$")
    url: str = Field(min_length=1, max_length=500)
    alt: str = Field(default="", max_length=300)
    sort_order: int = Field(default=0, ge=0)


class MediaRead(MediaCreate, ORMModel):
    id: uuid.UUID
    project_id: uuid.UUID


class ProjectBase(BaseModel):
    slug: str = Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$", max_length=160)
    name: str = Field(min_length=1, max_length=200)
    tagline: str | None = Field(default=None, max_length=300)
    short_description: str | None = None
    full_description: str | None = None
    status: str | None = Field(default=None, max_length=100)
    project_url: HttpUrl | None = None
    repository_url: HttpUrl | None = None
    featured: bool = False
    publication_status: PublicationStatus = PublicationStatus.draft
    published_at: datetime | None = None


class ProjectCreate(ProjectBase):
    technology_ids: list[uuid.UUID] = Field(default_factory=list)


class CaseStudySummary(ORMModel):
    id: uuid.UUID
    slug: str
    title: str
    challenge: str
    results: str


class ProjectUpdate(BaseModel):
    slug: str | None = Field(default=None, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$", max_length=160)
    name: str | None = Field(default=None, min_length=1, max_length=200)
    tagline: str | None = Field(default=None, max_length=300)
    short_description: str | None = None
    full_description: str | None = None
    status: str | None = Field(default=None, max_length=100)
    project_url: HttpUrl | None = None
    repository_url: HttpUrl | None = None
    featured: bool | None = None
    publication_status: PublicationStatus | None = None
    published_at: datetime | None = None
    technology_ids: list[uuid.UUID] | None = None


class ProjectRead(ProjectBase, ORMModel):
    id: uuid.UUID
    project_url: str | None
    repository_url: str | None
    created_at: datetime
    updated_at: datetime
    technologies: list[TechnologyRead]
    media: list[MediaRead]
    case_studies: list[CaseStudySummary]


class ProjectSummary(ORMModel):
    id: uuid.UUID
    slug: str
    name: str
    tagline: str | None
    technologies: list[TechnologyRead]


class CaseStudyBase(BaseModel):
    project_id: uuid.UUID
    slug: str = Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$", max_length=160)
    title: str = Field(min_length=1, max_length=250)
    challenge: str = Field(min_length=1)
    solution: str = Field(min_length=1)
    architecture: str | None = None
    results: str = Field(min_length=1)
    publication_status: PublicationStatus = PublicationStatus.draft
    published_at: datetime | None = None


class CaseStudyCreate(CaseStudyBase):
    pass


class CaseStudyUpdate(BaseModel):
    slug: str | None = Field(default=None, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$", max_length=160)
    title: str | None = Field(default=None, min_length=1, max_length=250)
    challenge: str | None = Field(default=None, min_length=1)
    solution: str | None = Field(default=None, min_length=1)
    architecture: str | None = None
    results: str | None = Field(default=None, min_length=1)
    publication_status: PublicationStatus | None = None
    published_at: datetime | None = None


class CaseStudyRead(CaseStudyBase, ORMModel):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    project: ProjectSummary
