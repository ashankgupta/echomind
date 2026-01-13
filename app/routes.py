"""API routes for EchoMind."""
from typing import Dict, List, Any
from fastapi import HTTPException, APIRouter
from .models import IngestRequest, QueryRequest, DeleteRequest
from .config import model, DISTANCE_THRESHOLD
from .database import get_collection

router = APIRouter()

@router.post("/ingest")
def ingest_text(req: IngestRequest) -> Dict[str, str]:
    """Ingest a new memory text into the vector database.

    Args:
        req: Request containing the text to store.

    Returns:
        Dict with status and assigned ID.
    """
    collection = get_collection()
    emb = model.encode([req.text], convert_to_numpy=True).tolist()[0]
    doc_id = f"id-{collection.count()}"
    collection.add(documents=[req.text], ids=[doc_id], embeddings=[emb])
    return {"status": "stored", "id": doc_id}

@router.post("/context")
def fetch_similar(req: QueryRequest) -> Dict[str, List[str]]:
    """Fetch similar memories based on query using vector similarity.

    Args:
        req: Request containing query and top_k.

    Returns:
        Dict with list of similar contexts.
    """
    collection = get_collection()
    if collection.count() == 0:
        return {"context": []}

    emb = model.encode([req.query], convert_to_numpy=True).tolist()
    results = collection.query(
        query_embeddings=emb,
        n_results=req.top_k,
        include=["documents", "distances"]
    )

    documents = results.get("documents")
    distances = results.get("distances")

    if not documents or not distances:
        return {"context": []}

    docs = documents[0]
    dists = distances[0]

    filtered = [doc for doc, dist in zip(docs, dists) if dist <= DISTANCE_THRESHOLD]

    return {"context": filtered}

@router.get("/all_memories")
def all_memories() -> Dict[str, Any]:
    """Retrieve all stored memories.

    Returns:
        Dict with documents and metadata.
    """
    collection = get_collection()
    results = collection.get(include=["documents"])
    return results

@router.delete("/delete")
def delete_memory(req: DeleteRequest) -> Dict[str, str]:
    """Delete a memory by ID.

    Args:
        req: Request containing the ID to delete.

    Returns:
        Dict with status.

    Raises:
        HTTPException: If deletion fails.
    """
    collection = get_collection()
    try:
        collection.delete(ids=[req.id])
        return {"status": "deleted", "id": req.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete: {str(e)}")