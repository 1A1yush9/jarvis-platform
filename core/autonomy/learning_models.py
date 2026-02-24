from pydantic import BaseModel
from datetime import datetime


class GoalOutcome(BaseModel):
    goal_id: str
    success: bool
    performance_delta: float
    stability_delta: float
    completed_at: datetime = datetime.utcnow()
