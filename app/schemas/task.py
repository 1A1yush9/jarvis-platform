from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    id: str
    name: str
    status: Optional[str] = "pending"
    description: Optional[str] = None