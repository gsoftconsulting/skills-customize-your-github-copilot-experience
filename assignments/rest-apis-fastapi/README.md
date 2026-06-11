# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a simple REST API using FastAPI. You will create endpoints for creating, reading, updating, and deleting resources while practicing request validation and proper HTTP response behavior.

## 📝 Tasks

### 🛠️	Create a FastAPI Application and Basic Endpoints

#### Description
Set up a FastAPI application and implement foundational endpoints to verify the API is running and can return structured JSON responses.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Add a `GET /` endpoint that returns a welcome message in JSON format.
- Add a `GET /health` endpoint that returns API status information.
- Run successfully with Uvicorn.

### 🛠️	Implement CRUD Endpoints for Items

#### Description
Build a small in-memory items API where each item has an `id`, `name`, and optional `description`. Use Pydantic models for request validation.

#### Requirements
Completed program should:

- Define Pydantic models for item input and item output.
- Implement `POST /items` to create an item.
- Implement `GET /items` to list all items and `GET /items/{item_id}` to fetch one item.
- Implement `PUT /items/{item_id}` to update an item.
- Implement `DELETE /items/{item_id}` to remove an item.
- Return `404` for operations on non-existent item IDs.

### 🛠️	Add Query Parameters and Filtering

#### Description
Extend the list endpoint so users can filter and limit results using query parameters.

#### Requirements
Completed program should:

- Support a `name` query parameter to filter items by name.
- Support a `limit` query parameter to control how many results are returned.
- Validate that `limit` is a positive integer.
- Return filtered results as JSON.
