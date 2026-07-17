"""
Health check endpoints.
"""

from datetime import datetime, timezone

from fastapi import APIRouter

from app.core.config import settings
from app.core.constants import HealthStatus

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    summary="Health Check",
)
async def health_check():
    """
    Basic platform health check.
    """

    return {
        "status": HealthStatus.OK,
        "application": settings.app.app_name,
        "version": settings.app.app_version,
        "environment": settings.app.app_env,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }