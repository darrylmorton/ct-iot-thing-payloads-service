#!/usr/bin/env python

import asyncio

import logging
import datetime

from sqlalchemy import delete
from sqlalchemy.exc import DatabaseError

from conftest import DEVICE_IDS
from models import ThingPayloadModel
from database import async_session
from tests.helper.seeds_helper import create_timestamp
from seeds.thing_payloads import thing_payloads_seed

log = logging.getLogger("thing_payloads_report_seed_data")


async def main():
    log.info("Starting thing_payloads_report_seed_data...")

    payloads_total = 366
    end_timestamp = create_timestamp("2020-08-08T00:00:00Z")
    start_timestamp = end_timestamp - datetime.timedelta(days=payloads_total)

    payloads = thing_payloads_seed(DEVICE_IDS, payloads_total, start_timestamp)

    try:
        async with async_session() as session:
            async with session.begin():
                await session.execute(delete(ThingPayloadModel))

                session.add_all(payloads)
                await session.commit()

                await session.close()
    except DatabaseError as error:
        log.error(f"Error with thing_payloads_report_seed_data {error}")

        raise DatabaseError


if __name__ == "__main__":
    asyncio.run(main())
