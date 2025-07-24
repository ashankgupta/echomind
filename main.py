from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import chromadb

app = FastAPI()

origins = [
    "http://localhost:8501",  # Streamlit ka default port
    "http://127.0.0.1:8501",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./vector_db")
collection = client.get_or_create_collection(name="persona")

class IngestRequest(BaseModel):
    text: str

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

class DeleteRequest(BaseModel):
    id: str

@app.post("/ingest")
def ingest_text(req: IngestRequest):
    emb = model.encode([req.text], convert_to_numpy=True).tolist()[0]
    doc_id = f"id-{collection.count()}"
    collection.add(documents=[req.text], ids=[doc_id], embeddings=[emb])
    return {"status": "stored", "id": doc_id}


@app.post("/context")
def fetch_similar(req: QueryRequest):
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

    DISTANCE_THRESHOLD = 1.2  # tune as per needs

    filtered = [doc for doc, dist in zip(docs, dists) if dist <= DISTANCE_THRESHOLD]

    return {"context": filtered}


@app.get("/all_memories")
def all_memories():
    results = collection.get(include=["documents"])
    return results

@app.delete("/delete")
def delete_memory(req: DeleteRequest):
    try:
        collection.delete(ids=[req.id])
        return {"status": "deleted", "id": req.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete: {str(e)}")

