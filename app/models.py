from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    type: str
    amount: int
    origin: Optional[str] = None
    destination: Optional[str] = None
