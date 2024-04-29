from fastapi import APIRouter
from sqlalchemy.exc import DatabaseError
from starlette.requests import Request
from starlette.responses import JSONResponse

from schemas import ThingPayload
from crud import find_thing_payloads_by_timestamps
from util.app_util import create_default_epoch_timestamps

from logger import log


router = APIRouter()


@router.get("/thing-payloads", response_model=list[ThingPayload])
async def get_thing_payloads(req: Request) -> list[ThingPayload] | JSONResponse:
    start_timestamp = req.query_params.get("start_timestamp")
    end_timestamp = req.query_params.get("end_timestamp")

    if not start_timestamp or not end_timestamp:
        start_timestamp, end_timestamp = create_default_epoch_timestamps()

    try:
        return await find_thing_payloads_by_timestamps(start_timestamp, end_timestamp)

    except DatabaseError as error:
        log.error(f"get_thing_payloads database error {error}")

        return JSONResponse(status_code=500, content=f"Database error {error}")
