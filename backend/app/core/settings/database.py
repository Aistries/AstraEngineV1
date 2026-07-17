"""
Database settings.
"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Database configuration."""

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "astra"
    postgres_user: str = "astra"
    postgres_password: str = "astra_password"

    # Development default (SQLite)
    database_url: str = Field(
        default="sqlite:///./astra.db",
        alias="DATABASE_URL",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        populate_by_name=True,
    )