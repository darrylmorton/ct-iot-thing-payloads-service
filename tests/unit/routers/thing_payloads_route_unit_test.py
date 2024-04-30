import datetime
from unittest.mock import patch

from tests.helper.routes_helper import mock_http_client
from thing_payloads_service.service import server


class TestThingPayloadsRoute:
    @patch("routers.thing_payloads.find_thing_payloads_by_timestamps")
    async def test_thing_payloads_default_timestamps(
        self, mock_find_thing_payloads_by_timestamps
    ):
        mock_find_thing_payloads_by_timestamps.return_value = []

        response = await mock_http_client(server, "http://test", "/api/thing-payloads")

        actual_result = response.json()

        assert response.status_code == 200
        assert actual_result == []

    @patch("routers.thing_payloads.find_thing_payloads_by_timestamps")
    async def test_thing_payloads_with_timestamps(
        self, mock_find_thing_payloads_by_timestamps
    ):
        mock_find_thing_payloads_by_timestamps.return_value = []

        start_date = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=12)
        start_timestamp: datetime = start_date + datetime.timedelta(hours=12)
        end_timestamp: datetime = start_date + datetime.timedelta(hours=88)

        params = {
            "start_timestamp": int(start_timestamp.timestamp()),
            "end_timestamp": int(end_timestamp.timestamp()),
        }

        response = await mock_http_client(
            server, "http://test", "/api/thing-payloads", params
        )

        actual_result = response.json()

        assert response.status_code == 200
        assert actual_result == []
