"""
AI provider settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class AISettings(BaseSettings):

    ai_provider: str = "none"

    openai_api_key: str = ""

    ollama_url: str = "http://localhost:11434"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )