import uuid

from httpx import AsyncClient, Response

from tests.config import APP_PORT


TEST_URL = f"http://localhost:{APP_PORT}"


async def http_client(base_url, path, params=None) -> Response:
    async with AsyncClient(base_url=base_url) as ac:
        if params:
            ac.params.set("start_timestamp", params["start_timestamp"])
            ac.params.set("end_timestamp", params["end_timestamp"])

        return await ac.get(path, params=params)


async def mock_http_client(app, base_url, path):
    async with AsyncClient(app=app, base_url=base_url) as ac:
        return await ac.get(path)


def validate_uuid4(uuid_string) -> bool:
    """
    Validate that a UUID string is in
    fact a valid uuid4.
    Happily, the uuid module does the actual
    checking for us.
    It is vital that the 'version' kwarg be passed
    to the UUID() call, otherwise any 32-character
    hex string is considered valid.
    """

    try:
        val = uuid.UUID(uuid_string, version=4)

    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        return False

    # If the uuid_string is a valid hex code,
    # but an invalid uuid4,
    # the UUID.__init__ will convert it to a
    # valid uuid4. This is bad for validation purposes.

    return str(val) == uuid_string


def expected_filtered_thing_payloads():
    return [
        {
            "id": "05406777-34be-4e68-8f1b-7f6fc03da050",
            "device_id": "aaa-111111",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 5.992819232552538,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 29.005245085554282,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "39cd4801-3394-4700-a6ec-13838577414d",
            "device_id": "bbb-222222",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 12.468687332550681,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 60.34844668954529,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "c5eb4d98-bbc3-4e3d-b4a6-ae99e9ee2b61",
            "device_id": "ccc-333333",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 7.4809018012994555,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 36.20756471828936,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "51323b92-70e0-4ccc-83ba-cd5d598374e3",
            "device_id": "ddd-444444",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": -4.384790346120248,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": -21.222385275222,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "03561efb-356e-43b1-8cd3-03427287512a",
            "device_id": "eee-555555",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": -12.219126470813713,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": -59.14057211873837,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "b9cffee6-c7d5-408e-90c3-89b3449d1aab",
            "device_id": "fff-666666",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": -8.819254069629899,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": -42.68518969700871,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "c44d30bf-7248-430a-9b58-5b5a733b3dc7",
            "device_id": "aaa-111111",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 10.518387310098706,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 50.90899458087774,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "263907c5-4960-423e-b681-a12175cce944",
            "device_id": "bbb-222222",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 11.366217835321022,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 55.01249432295374,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "47d8da0e-d83f-4db7-b974-6c58e0b05cd7",
            "device_id": "ccc-333333",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 1.7640001007483401,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 8.537760487621966,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "81d6211e-e68e-4f79-b5b1-89e75b379dc4",
            "device_id": "ddd-444444",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": -9.460031191349104,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": -45.78655096612966,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "d1e7d0ad-636c-48e2-bc54-5a826eb965f3",
            "device_id": "eee-555555",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": -11.986553433289231,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": -58.014918617119875,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "ce367eda-b462-474d-a137-7bf90b72cee6",
            "device_id": "fff-666666",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": -3.4926937274865733,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": -16.904637641035016,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "865d9e4c-3291-41f0-a8d2-26aa3d3cc26f",
            "device_id": "aaa-111111",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 12.468687332550681,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 60.34844668954529,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "c0b63267-0312-4f88-b0df-5c157ff69eac",
            "device_id": "bbb-222222",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 7.4809018012994555,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 36.20756471828936,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "2d90df7f-5105-4b60-be6a-4f9be9672581",
            "device_id": "ccc-333333",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": -4.384790346120248,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": -21.222385275222,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "805c0096-4de5-41ec-b648-3f472db1e473",
            "device_id": "ddd-444444",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": -12.219126470813713,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": -59.14057211873837,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "cbe805ba-b873-48c3-9c1b-e0b2821ec917",
            "device_id": "eee-555555",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": -8.819254069629899,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": -42.68518969700871,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "5f53b3a4-eaa7-4421-956a-5236e9758f3f",
            "device_id": "fff-666666",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {
                    "value": 2.688999851097694,
                    "unit": "C",
                    "connection": "pin:4",
                },
                "humidity": {
                    "value": 13.01475927931284,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
    ]


def assert_thing_payload(actual_result, expected_result):
    assert validate_uuid4(actual_result["id"]) is True
    assert actual_result["device_id"] == expected_result["device_id"]
    assert actual_result["payload_timestamp"] == expected_result["payload_timestamp"]
    assert actual_result["payload"] == expected_result["payload"]


def assert_thing_payloads(actual_result, expected_result):
    assert len(actual_result) == len(expected_result)

    for index in range(len(actual_result) - 1):
        assert_thing_payload(actual_result[index], expected_result[index])
