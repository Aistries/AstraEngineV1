"""
Standard API response builders.
"""

from typing import Any


def success(
    data: Any = None,
    message: str = "Success",
):
    return {
        "success": True,
        "message": message,
        "data": data,
    }


def error(
    message: str,
    details: Any = None,
):
    return {
        "success": False,
        "message": message,
        "details": details,
    }