from fastapi import APIRouter
from starlette.responses import JSONResponse

from config import APP_VERSION

router = APIRouter()


@router.get("/healthz")
async def health() -> JSONResponse:
    return JSONResponse(
        status_code=200, content={"message": "ok", "version": APP_VERSION}
    )
