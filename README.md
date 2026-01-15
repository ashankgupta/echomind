# EchoMind

## Description

EchoMind is a personal memory assistant that leverages AI-powered vector embeddings to store and retrieve your memories based on semantic similarity. Whether it's notes, ideas, or personal reflections, EchoMind helps you organize and rediscover your thoughts effortlessly.

## Features

- 🧠 **Add Memories**: Store personal notes and memories as text
- 🔍 **Smart Search**: Find similar memories using natural language queries
- 📚 **Manage Memories**: View, organize, and delete stored memories
- ⚡ **Fast Retrieval**: Vector-based similarity search with configurable thresholds
- 🎨 **Modern UI**: Clean, responsive interface built with Streamlit

## Architecture

EchoMind follows a modular architecture:

- **Backend (FastAPI)**: Handles API requests, vector embeddings, and database operations
  - `app/config.py`: Configuration and model loading
  - `app/models.py`: Pydantic request/response models
  - `app/database.py`: ChromaDB setup and operations
  - `app/routes.py`: API endpoints
  - `main.py`: Application entry point

- **Frontend (Streamlit)**: User interface for interacting with memories
  - `components/`: Modular UI components for each feature
  - `utils.py`: API interaction utilities
  - `streamlit_app.py`: Main app with tabs and layout

- **Infrastructure**: Docker containers for easy deployment

## Technologies

- **Backend**: FastAPI, ChromaDB, Sentence Transformers
- **Frontend**: Streamlit
- **Embeddings**: all-MiniLM-L6-v2 model
- **Database**: ChromaDB vector database
- **Deployment**: Docker & Docker Compose

## Prerequisites

- Python 3.11 or higher
- Git
- Docker and Docker Compose (for easy setup)

## Quick Start with Docker Compose (Recommended for Non-Tech Users)

1. Install Docker and Docker Compose on your system.

2. Clone the repository:
   ```
   git clone https://github.com/ashangupta/echomind
   cd echomind
   ```

3. Run the application:
   ```
   docker-compose up
   ```

4. Open your browser and go to `http://localhost:8501` to access the app.

That's it! The backend and frontend will start automatically.

## Local Setup (For Developers)

1. Clone the repository:
   ```
   git clone https://github.com/ashankgupta/echomind
   cd echomind
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Linux/Mac: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the FastAPI server:
    ```
    uvicorn main:app --reload
    ```

6. In another terminal, run the Streamlit app:
    ```
    streamlit run streamlit_app.py
    ```

## Project Structure

```
echomind/
├── app/                    # Backend package
│   ├── __init__.py
│   ├── config.py          # Configuration and model setup
│   ├── database.py        # ChromaDB operations
│   ├── models.py          # Pydantic models
│   └── routes.py          # API endpoints
├── components/            # Frontend components
│   ├── add_memory.py
│   ├── search_memories.py
│   └── manage_memories.py
├── utils.py               # API utilities
├── main.py                # FastAPI app entry point
├── streamlit_app.py       # Streamlit app entry point
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project metadata
├── Dockerfile             # Backend container
├── Dockerfile.streamlit   # Frontend container
├── docker-compose.yml     # Multi-container setup
└── README.md
```

## Usage

- Open the Streamlit app in your browser (usually http://localhost:8501)
- Add memories in the "Add Memory" section
- Search for memories in the "Search Memories" section
- View and delete memories in the "Show all stored memories" section

## API Endpoints

- POST /ingest: Ingest a new memory (text)
- POST /context: Query similar memories (query, top_k)
- GET /all_memories: Retrieve all stored memories
- DELETE /delete: Delete a memory by ID

## Docker

### Backend (FastAPI)

1. Build the backend image:
   ```
   docker build -t echomind-backend .
   ```

2. Run the backend container:
   ```
   docker run -p 8000:8000 echomind-backend
   ```

### Frontend (Streamlit)

1. Build the frontend image:
   ```
   docker build -f Dockerfile.streamlit -t echomind-frontend .
   ```

2. Run the frontend container:
   ```
   docker run -p 8501:8501 echomind-frontend
   ```

Note: The Streamlit app is configured to connect to `http://localhost:8000`. When running in Docker, you may need to use Docker networking or adjust the API_URL in `streamlit_app.py` to point to the backend container.

## License

This project is licensed under the MIT License.
