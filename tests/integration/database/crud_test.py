import datetime

from crud import find_thing_payloads_by_timestamps


class TestThingPayloadsDatabase:
    async def test_thing_payloads_default_timestamps(self, thing_payloads_fixture):
        start_date, end_date = thing_payloads_fixture
        start_timestamp: datetime = int(start_date.timestamp())
        end_timestamp: datetime = int(end_date.timestamp())

        actual_result = await find_thing_payloads_by_timestamps(
            start_timestamp, end_timestamp
        )

        assert len(actual_result) == 288

    async def test_thing_payloads_with_timestamps(self, thing_payloads_fixture):
        start_date, _ = thing_payloads_fixture
        start_timestamp = int((start_date + datetime.timedelta(hours=12)).timestamp())
        end_timestamp = int((start_date + datetime.timedelta(hours=88)).timestamp())

        actual_result = await find_thing_payloads_by_timestamps(
            start_timestamp, end_timestamp
        )

        assert len(actual_result) == 18
