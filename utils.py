import os
import requests
from typing import Optional

API_URL: str = os.getenv("API_URL", "http://localhost:8000")

def check_api_status() -> bool:
    """Check if the API is reachable.

    Returns:
        True if API is connected, False otherwise.
    """
    try:
        response = requests.get(f"{API_URL}/all_memories")
        return response.status_code == 200
    except:
        return False

def add_memory(text: str) -> requests.Response:
    """Add a new memory to the database.

    Args:
        text: The memory text to store.

    Returns:
        API response object.
    """
    response = requests.post(f"{API_URL}/ingest", json={"text": text})
    return response

def search_memories(query: str, top_k: int = 5) -> requests.Response:
    """Search for similar memories.

    Args:
        query: Search query.
        top_k: Number of results to return.

    Returns:
        API response object.
    """
    response = requests.post(f"{API_URL}/context", json={"query": query, "top_k": top_k})
    return response

def get_all_memories() -> requests.Response:
    """Retrieve all memories.

    Returns:
        API response object.
    """
    response = requests.get(f"{API_URL}/all_memories")
    return response

def delete_memory(mem_id: str) -> requests.Response:
    """Delete a memory by ID.

    Args:
        mem_id: ID of the memory to delete.

    Returns:
        API response object.
    """
    response = requests.delete(f"{API_URL}/delete", json={"id": mem_id})
    return response
