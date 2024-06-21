from sqlalchemy.exc import SQLAlchemyError

from database import async_session
from schemas import ThingPayload

from logger import log
from util import db_util


async def find_thing_payloads_by_timestamps(
    start_timestamp: int, end_timestamp: int
) -> list[ThingPayload]:
    error_message = (
        f"find_thing_payloads_by_timestamps {start_timestamp=} {end_timestamp=}"
    )

    async with async_session() as session:
        async with session.begin():
            stmt = db_util.thing_payloads_by_timestamps_stmt(
                start_timestamp=start_timestamp, end_timestamp=end_timestamp
            )

            try:
                result = await session.execute(stmt)

                return result.scalars().all()
            except SQLAlchemyError:
                log.error(error_message)
                raise SQLAlchemyError(error_message)
            finally:
                await session.close()
