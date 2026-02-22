from fastapi import APIRouter
import json
import os

router = APIRouter(prefix="/admin/strategy", tags=["Strategy"])

DATA_PATH = "app/database"
INSIGHT_FILE = f"{DATA_PATH}/strategy_insights.json"


@router.get("/insights")
def get_strategy_insights():
    if not os.path.exists(INSIGHT_FILE):
        return {"insights": []}

    with open(INSIGHT_FILE, "r") as f:
        data = json.load(f)

    return {"insights": data}