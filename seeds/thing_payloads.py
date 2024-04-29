import datetime
import json
import logging
import math
import uuid

from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from config import get_logger
from models import ThingPayloadModel
from schemas import Payload, PayloadValueUnit, Humidity, Temperature
from tests.crud import insert_thing_payloads, insert_thing_payload
from tests.database import async_session

DEVICE_IDS = [
    "aaa-111111",
    "bbb-222222",
    "ccc-333333",
    "ddd-444444",
    "eee-555555",
    "fff-666666",
]

# log = logging.getLogger("thing_payloads_service")
log = get_logger()


async def thing_payloads(total: int = 48) -> None:
    payloads = []
    start_date = datetime.datetime.now() - datetime.timedelta(days=2)

    for device_id_index in range(len(DEVICE_IDS)):
        data_point_value = device_id_index

        for payload_index in range(total):
            date_timestamp = start_date + datetime.timedelta(days=payload_index)
            timestamp = int(date_timestamp.timestamp())
            temperature_value = math.sin(data_point_value) * 12.5
            humidity_value = math.sin(data_point_value) * 60.5

            # payload = Payload(
            #     cadence=PayloadValueUnit(value=1800, unit="seconds"),
            #     battery=PayloadValueUnit(value=50, unit="%"),
            #     temperature=Temperature(
            #         value=temperature_value, unit="C", connection="pin:4"
            #     ),
            #     humidity=Humidity(
            #         value=humidity_value,
            #         unit="unknown",
            #         connection="pin:6",
            #         precipitation=False,
            #     ),
            # ).model_dump()

            # payload = Payload(
            #     cadence={"value": 1800, "unit": "seconds"},
            #     battery={
            #         "value": 50,
            #         "unit": "%",
            #     },
            #     temperature={
            #         "value": temperature_value,
            #         "unit": "C",
            #         "connection": "pin:4",
            #     },
            #     humidity={
            #         "value": humidity_value,
            #         "unit": "%",
            #         "connection": "pin:6",
            #         "precipitation": False,
            #     },
            # )

            payload = {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {
                    "value": 50,
                    "unit": "%",
                },
                "temperature": {
                    "value": temperature_value,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": humidity_value,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            }

            thing_payload = ThingPayloadModel(
                id=uuid.uuid4(),
                device_id=DEVICE_IDS[device_id_index],
                payload_timestamp=timestamp,
                payload=json.dumps(payload),
            )

            # log.info(f"BEFORE INSERT {thing_payload}")

            # payload=Payload(
            #     cadence=PayloadValueUnit(
            #         value=1800,
            #         unit="seconds"
            #     ),
            #     # "battery": {
            #     #     "value": 50,
            #     #     "unit": "%",
            #     # },
            #     # "temperature": {
            #     #     "value": temperature_value,
            #     #     "unit": "C",
            #     #     "connection": "pin:4",
            #     # },
            #     # "humidity": {
            #     #     "value": humidity_value,
            #     #     "unit": "%",
            #     #     "connection": "pin:6",
            #     #     "precipitation": False,
            #     # },
            # ),
            # # )

            await insert_thing_payload(thing_payload)

            payloads.append(thing_payload)

            data_point_value += 0.5

    # try:
    async with async_session() as session:
        async with session.begin():
            session.add_all(payloads)
            # await session.commit()

            # await session.refresh(thing_payload)
            await session.close()
    # except DatabaseError as error:
    #     log.error(f"Error while inserting thing payload: {error}")

    # await insert_thing_payloads(payloads)
    # return items
