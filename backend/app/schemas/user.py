"""
User schemas.
"""

from pydantic import BaseModel, ConfigDict, EmailStr

from app.schemas.role import RoleResponse


class UserResponse(BaseModel):

    id: int

    username: str

    email: EmailStr

    full_name: str | None = None

    is_active: bool

    is_verified: bool

    roles: list[RoleResponse] = []

    model_config = ConfigDict(from_attributes=True)