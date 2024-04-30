import uuid

from httpx import AsyncClient, Response, ASGITransport

from tests.config import APP_PORT


TEST_URL = f"http://localhost:{APP_PORT}"


async def http_client(base_url, path, params=None) -> Response:
    async with AsyncClient(base_url=base_url) as ac:
        if params:
            ac.params.set("start_timestamp", params["start_timestamp"])
            ac.params.set("end_timestamp", params["end_timestamp"])

        return await ac.get(path, params=params)


async def mock_http_client(app, base_url, path, params=None):
    async with AsyncClient(transport=ASGITransport(app=app), base_url=base_url) as ac:
        # if params:
        #     ac.params.set("start_timestamp", params["start_timestamp"])
        #     ac.params.set("end_timestamp", params["end_timestamp"])

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
            "id": "5fef2e58-adc5-488a-b55f-07be533d3621",
            "device_id": "aaa-111111",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 5.99, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 29.01,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "0cee258a-480f-4959-ac2e-f6e7d9606179",
            "device_id": "bbb-222222",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 12.47, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 60.35,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "2d38f3e3-d2e6-4de5-9ab7-a00b6113b722",
            "device_id": "ccc-333333",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 7.48, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 36.21,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "c4c0577c-203e-4517-856c-ac4702111dfd",
            "device_id": "ddd-444444",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -4.38, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -21.22,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "66cad734-6a94-4df8-a789-265a08410d99",
            "device_id": "eee-555555",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -12.22, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -59.14,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "260a6b96-38f9-422a-a210-cbf34c251528",
            "device_id": "fff-666666",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -8.82, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -42.69,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592784000,
        },
        {
            "id": "7941f66c-1f72-4455-8f80-a0ade07a5516",
            "device_id": "aaa-111111",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 10.52, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 50.91,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "e02e5b90-f657-4984-905b-a87cf08f15fa",
            "device_id": "bbb-222222",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 11.37, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 55.01,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "53bd0c83-0856-42b4-a0df-912bbe08726b",
            "device_id": "ccc-333333",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 1.76, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 8.54,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "db912c08-8e31-4a41-9523-913869696c49",
            "device_id": "ddd-444444",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -9.46, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -45.79,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "0191d077-7cc3-43c1-833c-bbfb0e6a6103",
            "device_id": "eee-555555",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -11.99, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -58.01,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "6d0bec16-eada-4607-9b0a-894ff5f96b85",
            "device_id": "fff-666666",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -3.49, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -16.9,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592870400,
        },
        {
            "id": "82a7a515-ab90-495a-b46a-ba0af6202324",
            "device_id": "aaa-111111",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 12.47, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 60.35,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "5dc45c61-ba50-4e19-978d-23cedb632420",
            "device_id": "bbb-222222",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 7.48, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 36.21,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "f6dc31de-4ae2-4fe2-9038-a9721c14f51c",
            "device_id": "ccc-333333",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -4.38, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -21.22,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "f7994933-4acc-4b3d-8c90-48e0cef2ce8b",
            "device_id": "ddd-444444",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -12.22, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -59.14,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "78d7b5d2-4ae6-4409-88c2-364cf1545cc2",
            "device_id": "eee-555555",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": -8.82, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": -42.69,
                    "unit": "%",
                    "connection": "pin:6",
                    "precipitation": False,
                },
            },
            "payload_timestamp": 1592956800,
        },
        {
            "id": "fc6233f2-7da8-4ceb-a895-3812ad1aa016",
            "device_id": "fff-666666",
            "payload": {
                "cadence": {"value": 1800, "unit": "seconds"},
                "battery": {"value": 50, "unit": "%"},
                "temperature": {"value": 2.69, "unit": "C", "connection": "pin:4"},
                "humidity": {
                    "value": 13.01,
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
