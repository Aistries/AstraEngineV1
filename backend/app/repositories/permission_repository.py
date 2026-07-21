"""
Permission repository.
"""

from app.models.permission import Permission
from app.repositories.base_repository import BaseRepository


class PermissionRepository(
    BaseRepository[Permission]
):

    def __init__(self):

        super().__init__(Permission)


permission_repository = PermissionRepository()