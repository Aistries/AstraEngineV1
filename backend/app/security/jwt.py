"""
JWT utilities.
"""

from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import jwt

from app.core.config import settings
from app.security.tokens import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    REFRESH_TOKEN_EXPIRE_DAYS,
)

ALGORITHM = "HS256"


def create_access_token(subject: str) -> str:

    expire = datetime.now(
        timezone.utc
    ) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": subject,
        "exp": expire,
        "type": "access",
    }

    return jwt.encode(
        payload,
        settings.security.secret_key,
        algorithm=ALGORITHM,
    )


def create_refresh_token(subject: str) -> str:

    expire = datetime.now(
        timezone.utc
    ) + timedelta(
        days=REFRESH_TOKEN_EXPIRE_DAYS
    )

    payload = {
        "sub": subject,
        "exp": expire,
        "type": "refresh",
    }

    return jwt.encode(
        payload,
        settings.security.secret_key,
        algorithm=ALGORITHM,
    )


def decode_token(token: str):

    return jwt.decode(
        token,
        settings.security.secret_key,
        algorithms=[ALGORITHM],
    )