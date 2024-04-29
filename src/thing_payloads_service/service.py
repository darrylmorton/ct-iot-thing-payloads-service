import contextlib
import logging

from alembic import command
from alembic.config import Config
from fastapi import FastAPI

from config import SERVICE_NAME, get_logger
from routers import health, thing_payloads

# log = logging.getLogger("thing_payloads_service")
log = get_logger()


async def run_migrations():
    log.info("Running migrations...")

    try:
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")

        log.info("Migrations completed successfully")
    except Exception as error:
        log.error(f"Database migration error on startup: {error}")


@contextlib.asynccontextmanager
async def lifespan_wrapper(app: FastAPI):
    log.info(f"Starting {SERVICE_NAME}...{app.host}")

    await run_migrations()

    log.info(f"{SERVICE_NAME} is ready")

    yield
    log.info(f"{SERVICE_NAME} is shutting down...")


server = FastAPI(title="FastAPI server", lifespan=lifespan_wrapper)

server.include_router(health.router, include_in_schema=False)

server.include_router(thing_payloads.router, prefix="/api")
