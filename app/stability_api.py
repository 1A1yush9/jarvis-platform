"""
Stage-46.0 — Cognitive Stability API
Provides advisory monitoring of system cognitive load.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

from core.cognitive_load_balancer import cognitive_load_balancer

router = APIRouter(prefix="/stability", tags=["Cognitive Stability"])


class LoadEvaluation(BaseModel):
    signals: Dict[str, Any]


@router.post("/evaluate")
def evaluate_load(data: LoadEvaluation):
    return cognitive_load_balancer.evaluate_load(data.signals)


@router.get("/history")
def stability_history():
    return cognitive_load_balancer.get_history()