from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
async def status():
    return {
        "jarvis": "online",
        "core": "stable",
        "mode": "safe-stage-1"
    }