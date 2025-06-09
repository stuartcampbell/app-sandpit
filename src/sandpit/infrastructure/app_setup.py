import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from sandpit.infrastructure.logging import logger

from sandpit.version import get_version

local_development_mode = False


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Log the version of the sandpit package
    logger.info(f"Sandpit Play API Version: {get_version()}")


    yield

    # Cleanup tasks or shutdown procedures can be added here
