from config import get_logger
from tests.helper.routes_helper import TEST_URL, http_client

log = get_logger()


class TestThingPayloadsRoute:
    async def test_thing_payloads(self, thing_payloads_fixture):
        expected_result = []

        response = await http_client(TEST_URL, "/api/thing-payloads")

        actual_result = response.json()
        log.info(f"** * actual_result {actual_result[0]}")

        assert response.status_code == 200
        assert actual_result == expected_result
