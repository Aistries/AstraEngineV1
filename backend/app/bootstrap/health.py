"""
Application startup health verification.

This module verifies that critical platform services
are available before ASTRA begins serving requests.
"""

from dataclasses import dataclass
from typing import Awaitable, Callable

from app.core.logging import get_logger

logger = get_logger()


@dataclass(slots=True)
class HealthCheck:
    """
    Represents a startup health check.
    """

    name: str
    checker: Callable[[], Awaitable[bool]]
    required: bool = True


class StartupHealth:

    def __init__(self) -> None:
        self._checks: list[HealthCheck] = []

    def register(
        self,
        name: str,
        checker: Callable[[], Awaitable[bool]],
        required: bool = True,
    ) -> None:
        """
        Register a startup health check.
        """
        self._checks.append(
            HealthCheck(
                name=name,
                checker=checker,
                required=required,
            )
        )

    async def run(self) -> None:
        """
        Execute every registered startup check.
        """

        logger.info("Running startup health checks...")

        for check in self._checks:

            logger.info("Checking {}", check.name)

            try:

                healthy = await check.checker()

            except Exception as exc:

                logger.exception(exc)

                healthy = False

            if healthy:

                logger.success("{} OK", check.name)

                continue

            logger.error("{} FAILED", check.name)

            if check.required:

                raise RuntimeError(
                    f"Required service unavailable: {check.name}"
                )

        logger.success("Startup health checks completed.")


startup_health = StartupHealth()