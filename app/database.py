import chromadb
from .config import VECTOR_DB_PATH, COLLECTION_NAME

# Initialize ChromaDB client and collection
client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

def get_collection():
    return collection