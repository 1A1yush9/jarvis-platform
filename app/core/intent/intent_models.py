from enum import Enum
from pydantic import BaseModel
from datetime import datetime
import uuid


class IntentLevel(str, Enum):
    SHORT = "short_term"
    MID = "mid_term"
    LONG = "long_term"


class StrategicIntent(BaseModel):
    id: str = str(uuid.uuid4())
    title: str
    level: IntentLevel
    priority: float = 0.5
    created_at: datetime = datetime.utcnow()
