from database import async_session
from models import ThingPayloadModel
from tests.abstract_crud import CrudInterface


class Crud(CrudInterface):
    def __init__(self):
        self.session = async_session()

    async def insert_thing_payload(self, thing_payload: ThingPayloadModel) -> None:
        async with self.session as session:
            async with session.begin():
                session.add(thing_payload)
                await session.commit()

                await session.refresh(thing_payload)
                await session.close()

    async def insert_thing_payloads(
        self, thing_payloads: list[ThingPayloadModel]
    ) -> None:
        async with self.session as session:
            async with session.begin():
                session.add_all(thing_payloads)
                await session.commit()

                await session.refresh(thing_payloads)
                await session.close()
