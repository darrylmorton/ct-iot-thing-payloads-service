import os

import uvicorn

import config
from logger import log


def main(port: int = config.APP_PORT):
    log.info(f"Starting {config.SERVICE_NAME}...")

    try:
        cores = os.cpu_count()

        if cores is None:
            calculated_workers = 3
        else:
            calculated_workers = 2 * cores + 1

        log.info(f"Running uvicorn with multiple workers {calculated_workers}")

        uvicorn.run(
            app="thing_payloads_service.service.server",
            host="0.0.0.0",
            port=port,
            workers=calculated_workers,
            log_config=None,
        )
    except Exception as e:
        log.error(f"Error with uvicorn {e}")
        raise Exception


if __name__ == "__main__":
    main()
