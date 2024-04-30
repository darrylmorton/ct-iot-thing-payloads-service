from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, Json


class ThingPayload(BaseModel):
    id: UUID
    device_id: str
    payload: Json
    payload_timestamp: int
    updated_at: datetime = Field(exclude=True)
    created_at: datetime = Field(exclude=True)

    class ConfigDict:
        from_attributes = True
