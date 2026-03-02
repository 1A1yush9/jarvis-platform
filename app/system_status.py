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
        "adaptive_load_regulator": True,
        "constitutional_resilience": True,
        "meta_governance_sentinel": True,
        "cognitive_integrity_monitor": True,
        "stage": "55.0",
        "timestamp": datetime.utcnow().isoformat(),
    }