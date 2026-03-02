from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

SYSTEM_MODE = "ADVISORY_ONLY"

@router.get("/system/status")
def system_status():
    return {
        "status": "LIVE",
        "mode": SYSTEM_MODE,
        "execution_authority": False,
        "constitutional_resilience": True,
        "autonomy_boundary": True,
        "governance_self_audit": True,
        "cognitive_integrity_monitor": True,
        "meta_governance_sentinel": True,
        "stage": "54.0",
        "timestamp": datetime.utcnow().isoformat(),
    }