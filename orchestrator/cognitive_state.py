from datetime import datetime
from pydantic import BaseModel
from typing import Dict, Any


class CognitiveState(BaseModel):
    timestamp: datetime
    execution_mode: str
    allocation: Dict[str, float]
    active_goals: int
    system_status: str = "healthy"
