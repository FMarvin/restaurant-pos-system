from typing import List, Optional
from pydantic import BaseModel

class ItemCreate(BaseModel):
    dish_id: int
    quantity: int

class OrderCreate(BaseModel):
    table_number: int
    special_instructions: Optional[str] = None
    items: List[ItemCreate]
