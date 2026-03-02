from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

SYSTEM_MODE = "ADVISORY_ONLY"
AUTONOMY_BOUNDARY_ACTIVE = True
GOVERNANCE_AUDIT_ACTIVE = True


@router.get("/system/status")
def system_status():
    return {
        "status": "LIVE",
        "mode": SYSTEM_MODE,
        "execution_authority": False,
        "autonomy_boundary": AUTONOMY_BOUNDARY_ACTIVE,
        "governance_self_audit": GOVERNANCE_AUDIT_ACTIVE,
        "stage": "51.0",
        "timestamp": datetime.utcnow().isoformat(),
    }