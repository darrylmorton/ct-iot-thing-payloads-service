import datetime

from dateutil.parser import isoparse


def create_timestamp(iso_date: str) -> datetime:
    return datetime.datetime.fromisoformat(iso_date)


def isodate_to_timestamp(timestamp: str) -> int:
    return int(isoparse(timestamp).timestamp())
