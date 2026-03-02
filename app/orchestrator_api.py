"""
Stage-49.0 — Executive Reasoning Orchestrator API
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from core.executive_reasoning_orchestrator import (
    executive_reasoning_orchestrator
)

router = APIRouter(prefix="/orchestrator", tags=["Executive Orchestrator"])


class CycleStart(BaseModel):
    inputs: Dict[str, Any]


@router.post("/start")
def start_cycle(data: CycleStart):
    return executive_reasoning_orchestrator.start_cycle(
        data.inputs
    )


@router.get("/{cycle_id}")
def get_cycle(cycle_id: str):
    result = executive_reasoning_orchestrator.get_cycle(cycle_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result


@router.get("/")
def overview():
    return executive_reasoning_orchestrator.overview()