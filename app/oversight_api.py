"""
Stage-39.0 — Oversight API Interface

Provides human authority endpoints.
Advisory only. No execution pathways.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional

from core.executive_oversight import executive_oversight

router = APIRouter(prefix="/oversight", tags=["Executive Oversight"])


# ---------------------------------------------------------
# Request Models
# ---------------------------------------------------------

class AdvisorySubmission(BaseModel):
    payload: Dict[str, Any]
    confidence: float
    risk_level: str


class HumanDecision(BaseModel):
    oversight_id: str
    decision: str
    reviewer: str
    notes: Optional[str] = None


# ---------------------------------------------------------
# Routes
# ---------------------------------------------------------

@router.post("/submit")
def submit_for_oversight(data: AdvisorySubmission):
    """
    Submit advisory intelligence for human supervision.
    """

    result = executive_oversight.submit_for_review(
        advisory_payload=data.payload,
        confidence_score=data.confidence,
        risk_level=data.risk_level,
    )

    return result


@router.post("/decision")
def apply_human_authority(decision: HumanDecision):
    """
    Apply human authority decision.
    """

    try:
        return executive_oversight.apply_human_decision(
            oversight_id=decision.oversight_id,
            decision=decision.decision,
            reviewer=decision.reviewer,
            notes=decision.notes,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/audit")
def oversight_audit_log():
    """
    Retrieve oversight audit trail.
    """

    return executive_oversight.get_oversight_log()