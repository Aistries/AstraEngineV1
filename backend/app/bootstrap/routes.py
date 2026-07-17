"""
Route registration.
"""

from fastapi import FastAPI

from app.api.v1.router import api_router


def register_routes(app: FastAPI) -> None:
    """
    Register API routes.
    """

    app.include_router(api_router)