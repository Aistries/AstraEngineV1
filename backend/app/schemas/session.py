"""
User session schemas.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SessionResponse(BaseModel):

    id: int

    device_name: str | None = None

    ip_address: str | None = None

    last_activity: datetime

    expires_at: datetime

    is_revoked: bool

    model_config = ConfigDict(from_attributes=True)