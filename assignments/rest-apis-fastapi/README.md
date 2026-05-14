# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build production-ready REST APIs using the FastAPI framework. You'll create endpoints to manage a collection of books, implementing CRUD operations (Create, Read, Update, Delete) and understand HTTP methods, path parameters, and request validation.

## 📝 Tasks

### 🛠️ Task 1: Create Basic Endpoints

#### Description
Set up a FastAPI application with basic GET and POST endpoints to manage a book collection. Start with simple in-memory storage using a Python list.

#### Requirements
Completed program should:

- Define a `Book` Pydantic model with fields: `id`, `title`, `author`, and `year`
- Implement a GET `/books` endpoint that returns all books
- Implement a POST `/books` endpoint that adds a new book to the collection
- Use FastAPI's automatic request validation and documentation

**Example:**
```json
GET /books
Response: [{"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008}]

POST /books
Body: {"title": "The Pragmatic Programmer", "author": "David Thomas", "year": 1999}
Response: {"id": 2, "title": "The Pragmatic Programmer", "author": "David Thomas", "year": 1999}
```

### 🛠️ Task 2: Implement Individual Resource Endpoints

#### Description
Add endpoints to retrieve, update, and delete individual books by their ID. Implement proper HTTP status codes and error handling.

#### Requirements
Completed program should:

- Implement a GET `/books/{book_id}` endpoint to retrieve a specific book
- Implement a PUT `/books/{book_id}` endpoint to update a book's details
- Implement a DELETE `/books/{book_id}` endpoint to remove a book
- Return appropriate HTTP status codes (200, 404, 400 as needed)
- Handle cases where a book ID doesn't exist with clear error messages

**Example:**
```json
GET /books/1
Response: {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008}

DELETE /books/1
Response: {"message": "Book deleted successfully"}

GET /books/999
Response: {"detail": "Book not found"}
```

### 🛠️ Task 3: Add Filtering and Validation (Stretch Goal)

#### Description
Enhance the API with query parameters for filtering books and add comprehensive input validation. This task introduces more advanced API design patterns.

#### Requirements
Completed program should:

- Add query parameters to GET `/books` to filter by author and/or minimum year (e.g., `GET /books?author=David%20Thomas&min_year=1990`)
- Validate that the book ID is a positive integer and year is within a reasonable range
- Return a 422 status code with clear validation error messages when invalid data is submitted
- Sort the filtered results by year in descending order

**Example:**
```json
GET /books?author=David%20Thomas&min_year=1990
Response: [{"id": 2, "title": "The Pragmatic Programmer", "author": "David Thomas", "year": 1999}]

POST /books
Body: {"title": "Book", "author": "Author", "year": 2050}
Response: {"detail": [{"loc": ["body", "year"], "msg": "Year must be between 1000 and 2025"}]}
```
