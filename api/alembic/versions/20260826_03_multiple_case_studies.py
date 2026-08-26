"""Allow multiple case studies per project."""
from collections.abc import Sequence

from alembic import op

revision: str = "20260826_03"
down_revision: str | None = "20260826_02"
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None


def upgrade() -> None:
    op.drop_constraint("case_studies_project_id_key", "case_studies", type_="unique")
    op.create_index("ix_case_studies_project_id", "case_studies", ["project_id"])


def downgrade() -> None:
    op.drop_index("ix_case_studies_project_id", table_name="case_studies")
    op.create_unique_constraint("case_studies_project_id_key", "case_studies", ["project_id"])
