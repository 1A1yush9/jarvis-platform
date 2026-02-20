from pydantic import BaseModel
from typing import Optional


class Intent(BaseModel):
    name: str
    confidence: Optional[float] = 0.0