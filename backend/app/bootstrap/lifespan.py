"""
Application lifespan.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import get_logger

from app.bootstrap.health import startup_health
from app.database.health import database_health

logger = get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup and shutdown events.
    """

    logger.info("===================================")
    logger.info("Starting {}", settings.app.app_name)
    logger.info("Version {}", settings.app.app_version)
    logger.info("Environment {}", settings.app.app_env)
    logger.info("===================================")

    # Register platform checks
    startup_health.register(
        "PostgreSQL",
        database_health,
    )

    # Run startup health checks
    await startup_health.run()

    yield

    logger.info("Stopping ASTRA")