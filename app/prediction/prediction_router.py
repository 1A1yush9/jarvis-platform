from fastapi import APIRouter
import json
import os

router = APIRouter(prefix="/admin/predictions", tags=["Predictions"])

DATA_PATH = "app/database"
PREDICTION_FILE = f"{DATA_PATH}/predictions.json"


@router.get("/")
def get_predictions():
    if not os.path.exists(PREDICTION_FILE):
        return {"predictions": []}

    with open(PREDICTION_FILE, "r") as f:
        data = json.load(f)

    return {"predictions": data}