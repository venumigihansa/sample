import logging
import requests
import threading

logger = logging.getLogger(__name__)

def search_hotels_tool(query: str):
    '''Search for hotels using the hotel API.

    Args:
        query: Search query string.
    Returns:
        List of hotel results or empty list on failure.
    '''
    try:
        endpoint = f'http://hotel-api/search?query={requests.utils.quote(query)}'
        logger.debug('Calling hotel search API: %s', endpoint)
        response = requests.get(endpoint, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error('search_hotels_tool failed: %s | thread_id=%s | user_message=%s',
                     str(e),
                     threading.get_ident(),
                     query)
        return []
