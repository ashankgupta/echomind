from pydantic import BaseModel

class IngestRequest(BaseModel):
    text: str

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

class DeleteRequest(BaseModel):
    id: str