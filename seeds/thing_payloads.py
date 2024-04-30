import datetime
import json
import math
import uuid

from models import ThingPayloadModel


DEVICE_IDS = [
    "aaa-111111",
    "bbb-222222",
    "ccc-333333",
    "ddd-444444",
    "eee-555555",
    "fff-666666",
]


def thing_payloads_seed(
    payloads_total: int, start_timestamp: datetime
) -> list[ThingPayloadModel]:
    payloads = []

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

    return payloads
