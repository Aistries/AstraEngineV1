"""
Session repository.
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.session import Session
from app.repositories.base_repository import BaseRepository


class SessionRepository(
    BaseRepository[Session]
):

    def __init__(self):

        super().__init__(Session)

    async def get_active_sessions(
        self,
        db: AsyncSession,
        user_id: int,
    ):

        result = await db.execute(
            select(Session).where(
                Session.user_id == user_id,
                Session.is_revoked == False,
            )
        )

        return result.scalars().all()


session_repository = SessionRepository()