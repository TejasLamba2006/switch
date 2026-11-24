"""An agent's own switch for showing what its tool calls did

Marked `expand_only`: adding a nullable column only extends the schema, so an
older pod keeps serving through a rolling upgrade.

Revision ID: c3f8a1d27e54
Revises: 5c50c7ae76dd
Create Date: 2026-10-31 00:00:00.000000
"""

import sqlalchemy as sa
from alembic import op

revision: str = "c3f8a1d27e54"
down_revision: str | None = "5c50c7ae76dd"
branch_labels = None
depends_on = None
expand_only: bool = True


def upgrade() -> None:
    op.add_column("agents", sa.Column("tool_details", sa.Boolean(), nullable=True))


def downgrade() -> None:
    op.drop_column("agents", "tool_details")
