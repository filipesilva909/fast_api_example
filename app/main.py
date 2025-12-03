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