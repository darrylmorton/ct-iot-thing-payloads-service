import datetime

from util.app_util import is_iso_timestamp_valid, create_default_epoch_timestamps


class TestUtil:
    timestamp = "2023-08-25T00:00:00Z"

    def test_is_iso_timestamp_valid_false(self):
        actual_result = is_iso_timestamp_valid("")

        assert actual_result is False

    def test_is_iso_timestamp_valid_true(self):
        actual_result = is_iso_timestamp_valid(self.timestamp)

        assert actual_result is True

    def test_create_default_timestamps(self):
        today = datetime.datetime.today()
        expected_today_timestamp = int(today.timestamp())
        expected_yesterday_timestamp = int(
            (today - datetime.timedelta(days=1)).timestamp()
        )

        actual_yesterday_timestamp, actual_today_timestamp = (
            create_default_epoch_timestamps()
        )

        assert actual_yesterday_timestamp >= expected_yesterday_timestamp
        assert actual_today_timestamp <= expected_today_timestamp
