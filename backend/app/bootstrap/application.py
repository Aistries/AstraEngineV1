"""
Application factory.
"""

from fastapi import FastAPI

from app.bootstrap.lifespan import lifespan
from app.bootstrap.middleware import register_middleware
from app.bootstrap.routes import register_routes
from app.core.config import settings


def create_application() -> FastAPI:
    """
    Build and configure the FastAPI application.
    """

    app = FastAPI(
        title=settings.app.app_name,
        version=settings.app.app_version,
        description="ASTRA Intelligence Engine",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    register_middleware(app)

    register_routes(app)

    return app