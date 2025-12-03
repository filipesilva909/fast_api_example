from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4

app = FastAPI(title="Example FastAPI App", version="1.0.0")

# ------------------------
# Pydantic model
# ------------------------
class Item(BaseModel):
    id: Optional[UUID] = None
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

# In-memory database (dictionary)
db_items = {}

@app.get("/health", tags=["Health"])
def health():
    """
    Health check endpoint.
    """
    return {"status": "ok"}

@app.get("/items", response_model=List[Item], tags=["Items"])
def get_items():
    """
    Return all items in the "database".
    """
    return list(db_items.values())

@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: UUID):
    """
    Get a single item by its ID.
    """
    item = db_items.get(str(item_id))
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item, status_code=201, tags=["Items"])
def create_item(item: Item):
    """
    Create a new item.
    """
    item.id = uuid4()
    db_items[str(item.id)] = item
    return item

    return

@app.delete("/items/{item_id}", status_code=204, tags=["Items"])
def delete_item(item_id: UUID):
    """
    Delete an item by its ID.
    """
    if str(item_id) not in db_items:
        raise HTTPException(status_code=404, detail="Item not found")
    del db_items[str(item_id)]
    return