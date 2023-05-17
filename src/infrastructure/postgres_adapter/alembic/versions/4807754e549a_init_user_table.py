"""init user table

Revision ID: 4807754e549a
Revises:
Create Date: 2023-05-16 13:20:40.291707

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4807754e549a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("username", sa.String(50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    def downgrade() -> None:
        op.drop_table("users")
