from pydantic import BaseModel
from typing import List
from datetime import datetime


class GrowthSignal(BaseModel):
    client_id: str
    signal_type: str
    score: float
    description: str
    created_at: datetime


class GrowthAction(BaseModel):
    action_id: str
    client_id: str
    action_type: str
    priority: int
    recommendation: str
    approved: bool = False
    executed: bool = False
    created_at: datetime