# app/routes/supervisor.py

from fastapi import APIRouter
from core.strategic_autonomy_supervisor import StrategicAutonomySupervisor

router = APIRouter()
engine = StrategicAutonomySupervisor()


@router.post("/supervisor/analyze")
async def supervise(payload: dict):

    tenant_id = payload.get("tenant_id")
    decisions = payload.get("decisions", [])

    result = engine.supervise(
        tenant_id=tenant_id,
        decisions=decisions
    )

    return {
        "status": "supervision_complete",
        "data": result
    }