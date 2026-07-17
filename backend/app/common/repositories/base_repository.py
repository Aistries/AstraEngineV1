"""
Generic repository.
"""

from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        model,
        db: AsyncSession,
    ):
        self.model = model
        self.db = db

    async def get(self, item_id: int):

        return await self.db.get(
            self.model,
            item_id,
        )

    async def list(self):

        result = await self.db.execute(
            select(self.model)
        )

        return result.scalars().all()

    async def create(self, obj):

        self.db.add(obj)

        await self.db.commit()

        await self.db.refresh(obj)

        return obj

    async def delete(self, obj):

        await self.db.delete(obj)

        await self.db.commit()