from fastapi import APIRouter, Depends, HTTPException
from typing import List
from .models import Item  # Import the Item model
from .auth import verify_token  # Import the verify_token function

# Create an APIRouter instance
router = APIRouter()

# In-memory storage for items (temporary for demonstration purposes)
items = []

# Route to get all items
@router.get("/items", response_model=List[Item])
def get_items():
    return items

# Route to add a new item
@router.post("/items", response_model=Item)
def add_item(item: Item, user=Depends(verify_token)):
    # Check for duplicate items by ID
    if any(existing_item.id == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    items.append(item)
    return item

# Route to delete an item by ID
@router.delete("/items/{id}", response_model=Item)
def delete_item(id: int, user=Depends(verify_token)):
    for item in items:
        if item.id == id:
            items.remove(item)
            return item
    raise HTTPException(status_code=404, detail="Item not found.")
