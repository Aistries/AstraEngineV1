"""
Bootstrap logging.
"""

from app.core.logging import configure_logging


def bootstrap_logging() -> None:
    """
    Initialize application logging.
    """
    configure_logging()