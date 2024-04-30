import asyncio
import datetime
import json
import math
import uuid

import pytest
from dotenv import load_dotenv
from sqlalchemy import delete

from models import ThingPayloadModel
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
async def seed_args() -> (int, datetime, datetime):
    payloads_total = 48
    end_timestamp = create_timestamp("2020-08-08T00:00:00Z")
    start_timestamp = end_timestamp - datetime.timedelta(days=payloads_total)

    return payloads_total, start_timestamp, end_timestamp


@pytest.fixture
async def thing_payloads_fixture(db_cleanup, seed_args) -> (datetime, datetime):
    payloads = []

    payloads_total, start_timestamp, end_timestamp = seed_args

    for device_id_index in range(len(DEVICE_IDS)):
        data_point_value = device_id_index

        for payload_index in range(payloads_total):
            date_timestamp = start_timestamp + datetime.timedelta(days=payload_index)
            timestamp = int(date_timestamp.timestamp())
            temperature_value = math.sin(data_point_value) * 12.5
            humidity_value = math.sin(data_point_value) * 60.5

            payload = json.dumps({
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {
                    "value": 50,
                    "unit": "%",
                },
                "temperature": {
                    "value": round(temperature_value, 2),
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": round(humidity_value, 2),
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            })

            thing_payload = ThingPayloadModel(
                id=uuid.uuid4(),
                device_id=DEVICE_IDS[device_id_index],
                payload_timestamp=timestamp,
                payload=payload,
            )

            payloads.append(thing_payload)

            data_point_value += 0.5

    async with async_session() as session:
        async with session.begin():
            session.add_all(payloads)
            await session.commit()

            await session.close()

    return start_timestamp, end_timestamp
