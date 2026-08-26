"""Initial content schema."""
from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "20260826_01"
down_revision: str | None = None
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None

publication_status = postgresql.ENUM("draft", "published", "archived", name="publication_status", create_type=False)


def upgrade() -> None:
    publication_status.create(op.get_bind(), checkfirst=True)
    op.create_table(
        "projects",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("slug", sa.String(160), nullable=False),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("tagline", sa.String(300)),
        sa.Column("short_description", sa.Text()),
        sa.Column("full_description", sa.Text()),
        sa.Column("status", sa.String(100)),
        sa.Column("project_url", sa.String(500)),
        sa.Column("repository_url", sa.String(500)),
        sa.Column("featured", sa.Boolean(), server_default=sa.false(), nullable=False),
        sa.Column("publication_status", publication_status, server_default="draft", nullable=False),
        sa.Column("published_at", sa.DateTime(timezone=True)),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_index("ix_projects_slug", "projects", ["slug"])
    op.create_table(
        "technologies",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("slug", sa.String(100), nullable=False),
        sa.Column("icon", sa.String(500)),
        sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("name"), sa.UniqueConstraint("slug"),
    )
    op.create_index("ix_technologies_slug", "technologies", ["slug"])
    op.create_table(
        "project_technologies",
        sa.Column("project_id", sa.Uuid(), sa.ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True),
        sa.Column("technology_id", sa.Uuid(), sa.ForeignKey("technologies.id", ondelete="CASCADE"), primary_key=True),
    )
    op.create_table(
        "case_studies",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("project_id", sa.Uuid(), sa.ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, unique=True),
        sa.Column("slug", sa.String(160), nullable=False, unique=True),
        sa.Column("title", sa.String(250), nullable=False),
        sa.Column("challenge", sa.Text(), nullable=False),
        sa.Column("solution", sa.Text(), nullable=False),
        sa.Column("architecture", sa.Text()),
        sa.Column("results", sa.Text(), nullable=False),
        sa.Column("publication_status", publication_status, server_default="draft", nullable=False),
        sa.Column("published_at", sa.DateTime(timezone=True)),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_case_studies_slug", "case_studies", ["slug"])
    op.create_table(
        "project_media",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("project_id", sa.Uuid(), sa.ForeignKey("projects.id", ondelete="CASCADE"), nullable=False),
        sa.Column("type", sa.String(30), nullable=False),
        sa.Column("url", sa.String(500), nullable=False),
        sa.Column("alt", sa.String(300), nullable=False),
        sa.Column("sort_order", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("project_id", "sort_order", name="uq_project_media_order"),
    )
    op.create_index("ix_project_media_project_id", "project_media", ["project_id"])


def downgrade() -> None:
    op.drop_table("project_media")
    op.drop_table("case_studies")
    op.drop_table("project_technologies")
    op.drop_table("technologies")
    op.drop_table("projects")
    publication_status.drop(op.get_bind(), checkfirst=True)
