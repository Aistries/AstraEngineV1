"""
Redis settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):

    redis_host: str = "redis"

    redis_port: int = 6379

    redis_db: int = 0

    redis_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )