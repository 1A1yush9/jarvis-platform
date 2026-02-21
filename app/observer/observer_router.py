from fastapi import APIRouter
from .observer_engine import observer_brain

router = APIRouter(prefix="/observer", tags=["Observer Brain"])


@router.get("/report")
def observer_report():
    return observer_brain.observe()