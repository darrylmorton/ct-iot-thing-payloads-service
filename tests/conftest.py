import asyncio
import datetime

import pytest
from dotenv import load_dotenv
from sqlalchemy import delete

from models import ThingPayloadModel
from seeds.thing_payloads import thing_payloads_seed
from tests.database import async_session
from tests.helper.seeds_helper import create_timestamp

load_dotenv(dotenv_path=".env.test")

DEVICE_IDS = [
    "aaa-111111",
    "bbb-222222",
    "ccc-333333",
    "ddd-444444",
    "eee-555555",
    "fff-666666",
]


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def db_cleanup():
    async with async_session() as session:
        async with session.begin():
            await session.execute(delete(ThingPayloadModel))
            await session.commit()
            await session.close()


@pytest.fixture
async def seed_default_args() -> (int, datetime, datetime):
    payloads_total = 48
    end_timestamp = create_timestamp("2020-08-08T00:00:00Z")
    start_timestamp = end_timestamp - datetime.timedelta(days=payloads_total)

    return payloads_total, start_timestamp, end_timestamp


@pytest.fixture
async def thing_payloads_fixture(db_cleanup, seed_default_args) -> (datetime, datetime):
    payloads_total, start_timestamp, end_timestamp = seed_default_args

    payloads = thing_payloads_seed(DEVICE_IDS, payloads_total, start_timestamp)

    async with async_session() as session:
        async with session.begin():
            session.add_all(payloads)
            await session.commit()

            await session.close()

    return start_timestamp, end_timestamp
