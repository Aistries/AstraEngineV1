"""
Database health checks.
"""

from sqlalchemy import text

from app.database.session import AsyncSessionLocal


async def database_health():
    try:
        async with AsyncSessionLocal() as session:

            await session.execute(text("SELECT 1"))

            return True

    except Exception:

        return False