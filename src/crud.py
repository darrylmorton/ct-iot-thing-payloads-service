from sqlalchemy.exc import SQLAlchemyError
from database import async_session

from abstract_crud import CrudInterface
from schemas import ThingPayload

from logger import log
from util.db_util import DbUtil


class Crud(CrudInterface):
    def __init__(self):
        self.session = async_session()

    async def find_thing_payloads_by_timestamps(
        self, start_timestamp: int, end_timestamp: int
    ) -> list[ThingPayload]:
        error_message = (
            f"find_thing_payloads_by_timestamps {start_timestamp=} {end_timestamp=}"
        )

        async with self.session:
            async with self.session.begin():
                stmt = DbUtil.thing_payloads_by_timestamps_stmt(
                    start_timestamp=start_timestamp, end_timestamp=end_timestamp
                )

                try:
                    result = await self.session.execute(stmt)

                    return result.scalars().all()
                except SQLAlchemyError:
                    log.error(error_message)
                    raise SQLAlchemyError(error_message)
                finally:
                    await self.session.close()
