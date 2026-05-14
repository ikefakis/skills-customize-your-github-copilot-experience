"""
FastAPI Application for Managing a Book Collection
This starter code provides the basic structure for a REST API.
Your tasks are to implement the endpoints defined in the assignment.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

# Create the FastAPI application
app = FastAPI(
    title="Book API",
    description="A simple REST API for managing a collection of books",
    version="1.0.0"
)

# ============================================================================
# Data Models
# ============================================================================

class Book(BaseModel):
    """Model for a Book resource"""
    id: int
    title: str
    author: str
    year: int


# ============================================================================
# In-Memory Data Storage
# ============================================================================

# Initialize with some example books
books_db: List[Book] = [
    Book(id=1, title="Clean Code", author="Robert C. Martin", year=2008),
    Book(id=2, title="The Pragmatic Programmer", author="David Thomas", year=1999),
    Book(id=3, title="Design Patterns", author="Gang of Four", year=1994),
]

next_id = 4  # Counter for generating new book IDs


# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint that returns a welcome message"""
    return {"message": "Welcome to the Book API! Visit /docs to see the interactive documentation."}


# TODO: Implement Task 1 endpoints
# - GET /books
# - POST /books


# TODO: Implement Task 2 endpoints
# - GET /books/{book_id}
# - PUT /books/{book_id}
# - DELETE /books/{book_id}


# TODO: Implement Task 3 endpoints (Stretch Goal)
# - Enhance GET /books with query parameters for filtering


# ============================================================================
# Run the Application
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
