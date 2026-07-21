"""
Generic repository implementation.
"""

from typing import Any
from typing import Generic
from typing import Type
from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """
    Generic CRUD repository.
    """

    def __init__(
        self,
        model: Type[ModelType],
    ):
        self.model = model

    async def get(
        self,
        db: AsyncSession,
        object_id: Any,
    ) -> ModelType | None:

        return await db.get(
            self.model,
            object_id,
        )

    async def list(
        self,
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
    ) -> list[ModelType]:

        result = await db.execute(
            select(self.model)
            .offset(skip)
            .limit(limit)
        )

        return list(result.scalars().all())

    async def create(
        self,
        db: AsyncSession,
        obj: ModelType,
    ) -> ModelType:

        db.add(obj)

        await db.commit()

        await db.refresh(obj)

        return obj

    async def update(
        self,
        db: AsyncSession,
        obj: ModelType,
    ) -> ModelType:

        await db.commit()

        await db.refresh(obj)

        return obj

    async def delete(
        self,
        db: AsyncSession,
        obj: ModelType,
    ):

        await db.delete(obj)

        await db.commit()