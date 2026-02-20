from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import uuid


class GoalStatus(str, Enum):
    CREATED = "created"
    VALIDATED = "validated"
    PLANNED = "planned"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    AGED = "aged"
    RETIRED = "retired"

class GoalPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AutonomousGoal(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str

    source_signal: str
    confidence: float = 0.0

    priority: GoalPriority = GoalPriority.MEDIUM
    status: GoalStatus = GoalStatus.CREATED

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    age_score: float = 0.0
last_activity_at: datetime = Field(default_factory=datetime.utcnow)

    metadata: Optional[Dict[str, Any]] = None
