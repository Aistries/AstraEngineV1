"""
Central application configuration.
"""

from dataclasses import dataclass

from app.core.settings.ai import AISettings
from app.core.settings.app import AppSettings
from app.core.settings.database import DatabaseSettings
from app.core.settings.logging import LoggingSettings
from app.core.settings.redis import RedisSettings
from app.core.settings.security import SecuritySettings


@dataclass(frozen=True)
class Settings:
    app: AppSettings
    database: DatabaseSettings
    redis: RedisSettings
    security: SecuritySettings
    logging: LoggingSettings
    ai: AISettings


settings = Settings(
    app=AppSettings(),
    database=DatabaseSettings(),
    redis=RedisSettings(),
    security=SecuritySettings(),
    logging=LoggingSettings(),
    ai=AISettings(),
)