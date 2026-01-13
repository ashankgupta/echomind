"""Configuration module for EchoMind."""
from sentence_transformers import SentenceTransformer

# Configuration constants
MODEL_NAME: str = "all-MiniLM-L6-v2"
DISTANCE_THRESHOLD: float = 1.2
VECTOR_DB_PATH: str = "./vector_db"
COLLECTION_NAME: str = "persona"

# Load the model
model: SentenceTransformer = SentenceTransformer(MODEL_NAME)