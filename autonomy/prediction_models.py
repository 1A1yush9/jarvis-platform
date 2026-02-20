from pydantic import BaseModel
from datetime import datetime


class PredictedSignal(BaseModel):
    type: str
    score: float
    reason: str
    created_at: datetime = datetime.utcnow()
