from sqlalchemy import select

from database import async_session
from models import ThingPayloadModel
from schemas import ThingPayload


async def find_thing_payloads_by_timestamps(
    start_timestamp: int, end_timestamp: int
) -> list[ThingPayload]:
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
