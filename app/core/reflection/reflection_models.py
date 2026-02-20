from pydantic import BaseModel
from datetime import datetime


class ReflectionReport(BaseModel):
    timestamp: datetime
    success_rate: float
    stability_score: float
    recommended_mode_bias: str
    notes: str
