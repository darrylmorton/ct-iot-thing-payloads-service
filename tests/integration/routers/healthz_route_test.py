from config import APP_VERSION
from tests.helper.routes_helper import RoutesHelper


async def test_health():
    expected_result = {"message": "ok", "version": APP_VERSION}

    response = await RoutesHelper.http_client(RoutesHelper.TEST_URL, "healthz")

    assert response.status_code == 200
    assert response.json() == expected_result
