import json
import os
from uuid import uuid4
from datetime import datetime

from .prediction_models import Prediction

DATA_PATH = "app/database"
PREDICTION_FILE = f"{DATA_PATH}/predictions.json"
GROWTH_FILE = f"{DATA_PATH}/growth_actions.json"


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
# PREDICTIVE ANALYSIS
# --------------------------------
def generate_predictions():
    actions = _load(GROWTH_FILE)
    predictions = _load(PREDICTION_FILE)

    new_predictions = []

    client_activity = {}

    for action in actions:
        cid = action["client_id"]
        client_activity[cid] = client_activity.get(cid, 0) + 1

    for client_id, count in client_activity.items():

        if count >= 3:
            prediction = Prediction(
                prediction_id=str(uuid4()),
                client_id=client_id,
                prediction_type="HIGH_GROWTH_PROBABILITY",
                probability=0.80,
                explanation="Repeated growth actions indicate scaling client",
                created_at=datetime.utcnow()
            ).dict()

        else:
            prediction = Prediction(
                prediction_id=str(uuid4()),
                client_id=client_id,
                prediction_type="CHURN_RISK_LOW",
                probability=0.30,
                explanation="Low activity variation detected",
                created_at=datetime.utcnow()
            ).dict()

        new_predictions.append(prediction)

    predictions.extend(new_predictions)
    _save(PREDICTION_FILE, predictions)

    return new_predictions