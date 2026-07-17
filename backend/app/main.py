"""
ASTRA entry point.
"""

from app.bootstrap.application import create_application
from app.bootstrap.logging import bootstrap_logging

bootstrap_logging()

app = create_application()