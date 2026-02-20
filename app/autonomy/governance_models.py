from enum import Enum
from pydantic import BaseModel


class GovernanceDecision(str, Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    DELAYED = "delayed"


class GovernanceResult(BaseModel):
    decision: GovernanceDecision
    reason: str
    risk_score: float = 0.0
