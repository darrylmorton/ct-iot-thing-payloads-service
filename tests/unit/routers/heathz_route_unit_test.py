from config import APP_VERSION
from thing_payloads_service.service import server
from tests.helper.routes_helper import RoutesHelper


async def test_unit_health():
    expected_result = {"message": "ok", "version": APP_VERSION}

    response = await RoutesHelper.mock_http_client(server, "http://test", "/healthz")

    assert response.status_code == 200
    assert response.json() == expected_result
