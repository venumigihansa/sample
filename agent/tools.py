# agent/tools.py
import os
import time
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def _exponential_backoff(attempt: int, base: float = 0.5) -> float:
    """Calculate exponential backoff delay."""
    return base * (2 ** (attempt - 1))

def search_hotels_tool(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Search for hotels using the downstream tool with retry/backoff.

    Args:
        params: Dictionary of search parameters.

    Returns:
        Result of the hotel search.

    Raises:
        RuntimeError: If the tool fails after all retries.
    """
    max_retries = int(os.getenv("HOTEL_SEARCH_MAX_RETRIES", "3"))
    backoff_base = float(os.getenv("HOTEL_SEARCH_BACKOFF_BASE", "0.5"))

    attempt = 0
    while True:
        try:
            # Original tool invocation logic (placeholder)
            # Replace with actual implementation that may have been failing.
            # For example, constructing a path and invoking the tool.
            # Here we simulate a successful call.
            result = _invoke_hotel_search(params)
            return result
        except Exception as exc:
            attempt += 1
            if attempt > max_retries:
                logger.error("search_hotels_tool failed after %d attempts: %s", attempt - 1, exc)
                raise RuntimeError("search_hotels_tool failed") from exc
            delay = _exponential_backoff(attempt, backoff_base)
            logger.warning("search_hotels_tool error on attempt %d: %s. Retrying in %.2f seconds...", attempt - 1, exc, delay)
            time.sleep(delay)

def _invoke_hotel_search(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Placeholder for the actual hotel search implementation.
    """
    # In production, this would call the downstream service or binary.
    # For now, return a dummy response.
    return {"hotels": []}
