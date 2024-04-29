import datetime

from logger import log
from tests.helper.routes_helper import (
    TEST_URL,
    http_client,
    expected_filtered_thing_payloads,
    assert_thing_payloads,
)


class TestThingPayloadsRoute:
    async def test_thing_payloads(self, thing_payloads_fixture):
        start_date, _ = thing_payloads_fixture
        start_timestamp: datetime = start_date + datetime.timedelta(hours=12)
        end_timestamp: datetime = start_date + datetime.timedelta(hours=88)

        params = {
            "start_timestamp": int(start_timestamp.timestamp()),
            "end_timestamp": int(end_timestamp.timestamp()),
        }
        expected_result = expected_filtered_thing_payloads()

        response = await http_client(TEST_URL, "/api/thing-payloads", params)

        actual_result = response.json()

        assert response.status_code == 200

        assert_thing_payloads(actual_result, expected_result)
