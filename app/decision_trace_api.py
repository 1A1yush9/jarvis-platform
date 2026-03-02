"""
Stage-41.0 — Decision Trace API

Provides explainability endpoints for executive accountability.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional

from core.decision_trace_graph import decision_trace_graph

router = APIRouter(prefix="/decision-trace", tags=["Decision Trace"])


class DecisionCreate(BaseModel):
    title: str
    payload: Dict[str, Any]
    confidence: float
    parent_id: Optional[str] = None


class OversightAttach(BaseModel):
    decision_id: str
    oversight_id: str


class ConstitutionAttach(BaseModel):
    decision_id: str
    status: str


@router.post("/create")
def create_decision(data: DecisionCreate):
    return decision_trace_graph.create_node(
        title=data.title,
        payload=data.payload,
        confidence=data.confidence,
        parent_id=data.parent_id,
    )


@router.post("/attach-oversight")
def attach_oversight(data: OversightAttach):
    decision_trace_graph.attach_oversight(
        data.decision_id,
        data.oversight_id,
    )
    return {"status": "OVERSIGHT_LINKED"}


@router.post("/attach-constitution")
def attach_constitution(data: ConstitutionAttach):
    decision_trace_graph.attach_constitutional_status(
        data.decision_id,
        data.status,
    )
    return {"status": "CONSTITUTION_LINKED"}


@router.get("/trace/{decision_id}")
def get_trace(decision_id: str):
    trace = decision_trace_graph.get_trace(decision_id)

    if not trace:
        raise HTTPException(status_code=404, detail="Decision not found")

    return {"trace": trace}