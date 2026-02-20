from fastapi import APIRouter
from .production_monitor import production_monitor

router = APIRouter(prefix="/ops", tags=["Operations"])


@router.get("/status")
def system_status():
    return production_monitor.build_status()
