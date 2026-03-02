from fastapi import APIRouter

router = APIRouter()

SYSTEM_MODE = "ADVISORY_ONLY"
AUTONOMY_BOUNDARY_ACTIVE = True


@router.get("/system/status")
def system_status():
    return {
        "status": "LIVE",
        "mode": SYSTEM_MODE,
        "execution_authority": False,
        "autonomy_boundary": AUTONOMY_BOUNDARY_ACTIVE,
        "stage": "50.0"
    }