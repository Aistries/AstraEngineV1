"""
Middleware registration.
"""

from fastapi import FastAPI

from app.middleware.request_id import RequestIDMiddleware
from app.middleware.security_headers import SecurityHeadersMiddleware


def register_middleware(app: FastAPI) -> None:
    """
    Register application middleware.
    """

    app.add_middleware(RequestIDMiddleware)

    app.add_middleware(SecurityHeadersMiddleware)