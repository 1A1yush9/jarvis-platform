from pydantic import BaseModel
from datetime import datetime


class Prediction(BaseModel):
    prediction_id: str
    client_id: str
    prediction_type: str
    probability: float
    explanation: str
    created_at: datetime