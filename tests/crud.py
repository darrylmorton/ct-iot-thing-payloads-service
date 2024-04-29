from database import async_session
from models import ThingPayloadModel


async def insert_thing_payload(thing_payload: ThingPayloadModel) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add(thing_payload)
            await session.commit()

            await session.refresh(thing_payload)
            await session.close()


async def insert_thing_payloads(thing_payloads: list[ThingPayloadModel]) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all(thing_payloads)
            await session.commit()

            await session.refresh(thing_payloads)
            await session.close()
