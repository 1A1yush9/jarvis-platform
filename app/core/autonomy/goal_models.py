from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum
from pydantic import BaseModel


# =====================================================
# Goal Status Enum
# =====================================================

class GoalStatus(str, Enum):
    pending = "pending"
    active = "active"
    completed = "completed"
    failed = "failed"
    cancelled = "cancelled"


# =====================================================
# Autonomous Goal Model
# =====================================================

class AutonomousGoal(BaseModel):

    id: str
    name: str
    description: Optional[str] = None

    status: GoalStatus = GoalStatus.pending

    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    last_activity_at: datetime = datetime.utcnow()

    metadata: Optional[Dict[str, Any]] = None