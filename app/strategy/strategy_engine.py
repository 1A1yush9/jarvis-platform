import json
import os
from uuid import uuid4
from datetime import datetime

from .strategy_models import StrategyInsight

DATA_PATH = "app/database"
MEMORY_FILE = f"{DATA_PATH}/strategic_memory.json"
INSIGHT_FILE = f"{DATA_PATH}/strategy_insights.json"


def ensure_database():
    os.makedirs(DATA_PATH, exist_ok=True)


def _load(path):
    ensure_database()
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def _save(path, data):
    ensure_database()
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


# --------------------------------
# BUILD STRATEGIC MEMORY
# --------------------------------
def update_strategic_memory(growth_actions):
    memory = _load(MEMORY_FILE)

    summary = {
        "total_actions": len(growth_actions),
        "timestamp": str(datetime.utcnow())
    }

    memory.append(summary)
    _save(MEMORY_FILE, memory)

    return summary


# --------------------------------
# GENERATE STRATEGIC INSIGHTS
# --------------------------------
def generate_strategy_insights():
    memory = _load(MEMORY_FILE)
    insights = _load(INSIGHT_FILE)

    new_insights = []

    if len(memory) >= 3:
        insight = StrategyInsight(
            insight_id=str(uuid4()),
            category="PLATFORM_GROWTH_PATTERN",
            description="Repeated growth activity detected across clients",
            confidence=0.82,
            created_at=datetime.utcnow()
        ).dict()

        new_insights.append(insight)

    insights.extend(new_insights)
    _save(INSIGHT_FILE, insights)

    return new_insights