from psycopg2 import DatabaseError
from sqlalchemy import select

from schemas import ThingPayload
from database import async_session
from models import ThingPayloadModel

from logger import log


async def find_thing_payloads_by_timestamps(
    start_timestamp: int, end_timestamp: int
) -> list[ThingPayload]:
    try:
        async with async_session() as session:
            async with session.begin():
                stmt = (
                    select(ThingPayloadModel)
                    .filter(
                        ThingPayloadModel.payload_timestamp.between(
                            int(start_timestamp), int(end_timestamp)
                        )
                    )
                    .order_by(ThingPayloadModel.payload_timestamp.asc())
                    .order_by(ThingPayloadModel.device_id.asc())
                    .limit(300)
                )

                result = await session.execute(stmt)

                await session.close()

                return result.scalars().all()
    except DatabaseError as error:
        log.error(f"Error while executing find_thing_payloads_by_timestamps: {error}")
