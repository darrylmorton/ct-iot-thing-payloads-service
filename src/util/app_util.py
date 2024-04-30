import datetime
from typing import Tuple

from dateutil.parser import isoparse


def is_iso_timestamp_valid(iso_timestamp: str) -> bool:
    try:
        return bool(isoparse(iso_timestamp))
    except ValueError:
        return False


def create_default_epoch_timestamps() -> Tuple[int, int]:
    today = datetime.datetime.now(datetime.UTC)

    today_timestamp = int(today.timestamp())
    yesterday_timestamp = int((today - datetime.timedelta(days=1)).timestamp())

    return today_timestamp, yesterday_timestamp
