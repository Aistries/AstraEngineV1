"""
Application constants.

Shared constants used throughout the ASTRA platform.
"""

from enum import StrEnum


class Environment(StrEnum):
    DEVELOPMENT = "development"
    TESTING = "testing"
    STAGING = "staging"
    PRODUCTION = "production"


class LogFormat(StrEnum):
    CONSOLE = "console"
    JSON = "json"


class AIProvider(StrEnum):
    NONE = "none"
    OPENAI = "openai"
    OLLAMA = "ollama"
    ANTHROPIC = "anthropic"


class HealthStatus(StrEnum):
    OK = "ok"
    WARNING = "warning"
    ERROR = "error"


API_PREFIX = "/api/v1"

HEALTH_ENDPOINT = "/health"

DEFAULT_PAGE_SIZE = 25

MAX_PAGE_SIZE = 100