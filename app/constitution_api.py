"""
Stage-40.0 — Constitutional Governance API
Provides visibility into the Jarvis operating charter.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any

from core.constitutional_governance import constitutional_governance

router = APIRouter(prefix="/constitution", tags=["Constitutional Governance"])


class AdvisoryCheck(BaseModel):
    payload: Dict[str, Any]


@router.get("/")
def get_constitution():
    """
    Retrieve system constitution.
    """
    return constitutional_governance.get_constitution()


@router.post("/validate")
def validate_advisory(data: AdvisoryCheck):
    """
    Validate advisory output against constitutional doctrine.
    """
    return constitutional_governance.validate_advisory(
        advisory_payload=data.payload
    )