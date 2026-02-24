from enum import Enum
from pydantic import BaseModel
from datetime import datetime


class ExecutionMode(str, Enum):
    SAFE = "safe_mode"
    BALANCED = "balanced_mode"
    AGGRESSIVE = "aggressive_mode"


class ExecutivePolicyState(BaseModel):
    mode: ExecutionMode
    confidence: float
    updated_at: datetime = datetime.utcnow()
