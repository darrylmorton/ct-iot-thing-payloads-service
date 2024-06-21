from sqlalchemy import select

from models import ThingPayloadModel


def thing_payloads_by_timestamps_stmt(start_timestamp: int, end_timestamp: int):
    return (
        select(ThingPayloadModel)
        .filter(
            ThingPayloadModel.payload_timestamp.between(
                int(start_timestamp), int(end_timestamp)
            )
        )
        .order_by(ThingPayloadModel.payload_timestamp.asc())
        .order_by(ThingPayloadModel.device_id.asc())
        .limit(300)
    )
