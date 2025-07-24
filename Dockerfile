# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and ChromaDB storage
COPY main.py .
COPY ./vector_db ./vector_db

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
