import datetime
from unittest.mock import patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from crud import Crud


class TestCrudUtil:
    @patch("crud.DbUtil.thing_payloads_by_timestamps_stmt")
    async def test_find_thing_payloads_by_timestamps_exception(
        self,
        mock_stmt,
        thing_payloads_fixture,
    ):
        mock_stmt.return_value = None

        start_date, _ = thing_payloads_fixture
        start_timestamp: datetime = start_date + datetime.timedelta(hours=12)
        end_timestamp: datetime = start_date + datetime.timedelta(hours=88)

        start_timestamp_int = int(start_timestamp.timestamp())
        end_timestamp_int = int(end_timestamp.timestamp())

        with pytest.raises(SQLAlchemyError):
            await Crud().find_thing_payloads_by_timestamps(
                start_timestamp_int, end_timestamp_int
            )
