"""
Stage-45.0 — Executive Intent Alignment API
Provides monitoring endpoints for intent alignment.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from core.executive_intent_alignment import (
    executive_intent_alignment_monitor
)

router = APIRouter(prefix="/intent", tags=["Executive Intent Alignment"])


class IntentDefine(BaseModel):
    description: str
    objectives: Dict[str, Any]


class AlignmentCheck(BaseModel):
    advisory_payload: Dict[str, Any]


@router.post("/define")
def define_intent(data: IntentDefine):
    return executive_intent_alignment_monitor.define_intent(
        data.description,
        data.objectives,
    )


@router.post("/evaluate")
def evaluate_alignment(data: AlignmentCheck):
    result = executive_intent_alignment_monitor.evaluate_alignment(
        data.advisory_payload
    )

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result


@router.get("/history")
def alignment_history():
    return executive_intent_alignment_monitor.get_alignment_history()