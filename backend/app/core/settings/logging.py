"""
Logging settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingSettings(BaseSettings):

    log_level: str = "INFO"

    log_format: str = "console"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )