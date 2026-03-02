from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/system/status")
def system_status():
    return {
        "status": "LIVE",
        "mode": "ADVISORY_ONLY",
        "execution_authority": False,
        "system_coherence_layer": True,
        "predictive_stability_engine": True,
        "adaptive_load_regulator": True,
        "stage": "57.0",
        "timestamp": datetime.utcnow().isoformat(),
    }