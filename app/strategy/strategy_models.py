from pydantic import BaseModel
from datetime import datetime


class StrategyInsight(BaseModel):
    insight_id: str
    category: str
    description: str
    confidence: float
    created_at: datetime


class StrategicMemory(BaseModel):
    key: str
    value: dict
    updated_at: datetime