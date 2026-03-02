"""
Stage-44.0 — Strategic Consensus API
Creates unified advisory recommendations from forecasts.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

from core.strategic_consensus_engine import strategic_consensus_engine

router = APIRouter(prefix="/consensus", tags=["Strategic Consensus"])


class ConsensusBuild(BaseModel):
    timeline_set_id: str
    forecasts: List[Dict[str, Any]]


@router.post("/build")
def build_consensus(data: ConsensusBuild):
    result = strategic_consensus_engine.build_consensus(
        data.timeline_set_id,
        data.forecasts,
    )

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result


@router.get("/{consensus_id}")
def get_consensus(consensus_id: str):
    result = strategic_consensus_engine.get_consensus(consensus_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result