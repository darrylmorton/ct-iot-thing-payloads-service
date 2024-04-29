import uuid
import json
from typing import Any

from datetime import datetime

from sqlalchemy import Column, DATETIME, INTEGER, String, Uuid
from sqlalchemy.dialects.postgresql import JSON, UUID, JSONB

from sqlalchemy.orm import MappedColumn, Mapped, DeclarativeBase
from database import Base


# class Base(DeclarativeBase):
#     type_annotation_map = {dict[str, Any]: JSON}


class ThingPayloadModel(Base):
    __tablename__ = "thing_payloads"

    id = Column(UUID, primary_key=True)
    device_id = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    payload_timestamp = Column(INTEGER, nullable=False)
    updated_at = Column(DATETIME, nullable=False, default=datetime.now())
    created_at = Column(DATETIME, nullable=False, default=datetime.now())


# class Base(DeclarativeBase):
#     type_annotation_map = {dict[str, Any]: JSON}
#
#
# class ThingPayloadModel(Base):
#     __tablename__ = "thing_payloads"
#
#     id: Mapped[uuid.UUID] = MappedColumn(type_=Uuid, primary_key=True, index=True)
#     device_id: Mapped[str] = MappedColumn(nullable=False)
#     payload: Mapped[JSON] = MappedColumn(type_=JSON, nullable=False)
#     payload_timestamp: Mapped[int] = MappedColumn(nullable=False)
#     updated_at: Mapped[datetime] = MappedColumn(
#         nullable=False, default=datetime.utcnow()
#     )
#     created_at: Mapped[datetime] = MappedColumn(
#         nullable=False, default=datetime.utcnow()
#     )
