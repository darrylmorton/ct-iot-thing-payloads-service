from config import APP_VERSION
from tests.helper.routes_helper import RoutesHelper
from thing_payloads_service.service import server


async def test_healthz():
    expected_result = {"message": "ok", "version": APP_VERSION}

    response = await RoutesHelper.http_client(server, RoutesHelper.TEST_URL, "/healthz")

    assert response.status_code == 200
    assert response.json() == expected_result
