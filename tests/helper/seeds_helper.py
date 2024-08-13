import datetime

from dateutil.parser import isoparse


class SeedsHelper:
    @staticmethod
    def create_timestamp(iso_date: str) -> datetime:
        return datetime.datetime.fromisoformat(iso_date)

    @staticmethod
    def isodate_to_timestamp(timestamp: str) -> int:
        return int(isoparse(timestamp).timestamp())
