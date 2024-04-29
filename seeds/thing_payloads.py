import datetime
import json
import math
import uuid


from models import ThingPayloadModel
from tests.crud import insert_thing_payload
from tests.database import async_session

DEVICE_IDS = [
    "aaa-111111",
    "bbb-222222",
    "ccc-333333",
    "ddd-444444",
    "eee-555555",
    "fff-666666",
]


async def thing_payloads(total: int = 48) -> (int, int):
    payloads = []
    end_timestamp = datetime.datetime.now(datetime.UTC)
    start_timestamp = end_timestamp - datetime.timedelta(days=2)

    for device_id_index in range(len(DEVICE_IDS)):
        data_point_value = device_id_index

        for payload_index in range(total):
            date_timestamp = start_timestamp + datetime.timedelta(days=payload_index)
            timestamp = int(date_timestamp.timestamp())
            temperature_value = math.sin(data_point_value) * 12.5
            humidity_value = math.sin(data_point_value) * 60.5

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

            await insert_thing_payload(thing_payload)

            payloads.append(thing_payload)

            data_point_value += 0.5

    async with async_session() as session:
        async with session.begin():
            session.add_all(payloads)
            await session.commit()

            await session.close()

    return start_timestamp, end_timestamp
