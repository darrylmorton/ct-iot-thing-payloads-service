from tests.helper.routes_helper import RoutesHelper


async def test_health():
    expected_result = {"message": "ok"}

    response = await RoutesHelper.http_client(RoutesHelper.TEST_URL, "healthz")
    actual_result = response.json()

    assert response.status_code == 200
    assert actual_result == expected_result
