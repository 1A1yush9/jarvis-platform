from pydantic import BaseModel
from datetime import datetime


class Incident(BaseModel):
    type: str
    severity: str
    message: str
    detected_at: datetime
