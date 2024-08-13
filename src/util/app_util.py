import datetime
import toml
from pathlib import Path
from typing import Tuple

from dateutil.parser import isoparse


class AppUtil:
    @staticmethod
    def is_iso_timestamp_valid(iso_timestamp: str) -> bool:
        try:
            return bool(isoparse(iso_timestamp))
        except ValueError:
            return False

    @staticmethod
    def create_default_epoch_timestamps() -> Tuple[int, int]:
        today = datetime.datetime.now(datetime.UTC)

        today_timestamp = int(today.timestamp())
        yesterday_timestamp = int((today - datetime.timedelta(days=1)).timestamp())

        return today_timestamp, yesterday_timestamp

    @staticmethod
    def get_app_version() -> str:
        app_version = None

        pyproject_toml_file = Path(__file__).parent.parent.parent / "pyproject.toml"

        if pyproject_toml_file.exists() and pyproject_toml_file.is_file():
            app_version = toml.load(pyproject_toml_file)["tool"]["poetry"]["version"]

        return app_version
