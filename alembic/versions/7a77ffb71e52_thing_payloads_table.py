"""thing_payloads table

Revision ID: 7a77ffb71e52
Revises:
Create Date: 2024-04-22 18:20:10.458363

"""

from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7a77ffb71e52"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "thing_payloads",
        sa.Column("id", sa.Uuid, primary_key=True, nullable=False),
        sa.Column("device_id", sa.String, nullable=False),
        sa.Column("payload_timestamp", sa.Integer, nullable=False),
        sa.Column("payload", sa.JSON, nullable=False),
        sa.Column("created_at", sa.DateTime, default=datetime.now()),
        sa.Column("updated_at", sa.DateTime, default=datetime.now()),
    )


def downgrade() -> None:
    op.drop_table("thing_payloads")
