# app/routes/executive.py

from fastapi import APIRouter
from core.executive_decision_engine import ExecutiveDecisionEngine

router = APIRouter()
engine = ExecutiveDecisionEngine()


@router.post("/executive/evaluate")
async def evaluate_pipeline(payload: dict):

    tenant_id = payload.get("tenant_id")
    proposals = payload.get("proposals", [])

    result = engine.evaluate_pipeline(
        tenant_id=tenant_id,
        proposals=proposals
    )

    return {
        "status": "executive_decision_generated",
        "data": result
    }