"""
Central logging configuration.
"""

import sys
from loguru import logger

from app.core.config import settings


def configure_logging() -> None:
    """
    Configure the global application logger.
    """

    logger.remove()

    logger.add(
        sys.stdout,
        level=settings.logging.log_level,
        colorize=True,
        enqueue=True,
        backtrace=True,
        diagnose=settings.app.debug,
    )


def get_logger():
    """
    Return the configured logger instance.
    """
    return logger