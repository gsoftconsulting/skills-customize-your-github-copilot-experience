# Starter Code for Building REST APIs with FastAPI Assignment

from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI(title="FastAPI Assignment API")


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None


class Item(ItemCreate):
    id: int


# In-memory store: key = item id, value = item dict
items_db = {}
next_item_id = 1


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/items", response_model=Item)
def create_item(item: ItemCreate):
    global next_item_id

    created_item = {
        "id": next_item_id,
        "name": item.name,
        "description": item.description,
    }
    items_db[next_item_id] = created_item
    next_item_id += 1
    return created_item


@app.get("/items")
def list_items(
    name: Optional[str] = None,
    limit: int = Query(default=10, gt=0),
):
    results = list(items_db.values())

    if name:
        lowered = name.lower()
        results = [entry for entry in results if lowered in entry["name"].lower()]

    return results[:limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_item = {
        "id": item_id,
        "name": item.name,
        "description": item.description,
    }
    items_db[item_id] = updated_item
    return updated_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    del items_db[item_id]
    return {"message": "Item deleted"}


# Run locally with:
# uvicorn starter-code:app --reload
