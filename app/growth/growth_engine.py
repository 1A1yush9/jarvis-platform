import json
import os
from datetime import datetime
from uuid import uuid4

from .growth_models import GrowthSignal, GrowthAction

DATA_PATH = "app/database"
SIGNAL_FILE = f"{DATA_PATH}/growth_signals.json"
ACTION_FILE = f"{DATA_PATH}/growth_actions.json"


def _load(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)


def _save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)


# -----------------------------
# SIGNAL DETECTION
# -----------------------------
def detect_growth_signals(usage_data):
    signals = []

    for client in usage_data:
        usage = client.get("requests", 0)
        revenue = client.get("revenue", 0)

        if usage > 1000:
            signals.append(
                GrowthSignal(
                    client_id=client["client_id"],
                    signal_type="HIGH_USAGE",
                    score=0.9,
                    description="Client showing strong usage growth",
                    created_at=datetime.utcnow()
                ).dict()
            )

        if revenue > 500:
            signals.append(
                GrowthSignal(
                    client_id=client["client_id"],
                    signal_type="REVENUE_EXPANSION",
                    score=0.85,
                    description="Upsell opportunity detected",
                    created_at=datetime.utcnow()
                ).dict()
            )

    existing = _load(SIGNAL_FILE)
    existing.extend(signals)
    _save(SIGNAL_FILE, existing)

    return signals


# -----------------------------
# STRATEGY GENERATION
# -----------------------------
def generate_growth_actions():
    signals = _load(SIGNAL_FILE)
    actions = _load(ACTION_FILE)

    new_actions = []

    for s in signals:
        action = GrowthAction(
            action_id=str(uuid4()),
            client_id=s["client_id"],
            action_type="UPGRADE_RECOMMENDATION",
            priority=1,
            recommendation=f"Recommend premium automation tier to {s['client_id']}",
            created_at=datetime.utcnow()
        ).dict()

        new_actions.append(action)

    actions.extend(new_actions)
    _save(ACTION_FILE, actions)

    return new_actions


# -----------------------------
# EXECUTION (ADMIN CONTROLLED)
# -----------------------------
def execute_approved_actions():
    actions = _load(ACTION_FILE)

    for action in actions:
        if action["approved"] and not action["executed"]:
            print(f"Executing growth action for {action['client_id']}")
            action["executed"] = True

    _save(ACTION_FILE, actions)
    return actions