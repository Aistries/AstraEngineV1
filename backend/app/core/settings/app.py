"""
Application settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application configuration."""

    app_name: str = "ASTRA Intelligence Engine"
    app_version: str = "0.1.0"

    app_env: str = "development"

    debug: bool = True

    host: str = "0.0.0.0"

    port: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )