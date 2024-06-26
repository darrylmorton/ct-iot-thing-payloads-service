import datetime
import uuid

from sqlalchemy import Column, INTEGER, String, DateTime
from sqlalchemy.dialects.postgresql import JSON, UUID

from database import Base


class ThingPayloadModel(Base):
    __tablename__ = "thing_payloads"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    device_id = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    payload_timestamp = Column(INTEGER, nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now(datetime.UTC),
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now(datetime.UTC),
    )
