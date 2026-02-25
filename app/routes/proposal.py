# app/routes/proposal.py

from fastapi import APIRouter
from core.proposal_engine import ProposalIntelligenceEngine

router = APIRouter()
engine = ProposalIntelligenceEngine()


@router.post("/proposal/generate")
async def generate_proposal(payload: dict):

    tenant_id = payload.get("tenant_id")

    proposal = engine.generate_proposal(
        tenant_id=tenant_id,
        deal_data=payload.get("deal_data", {}),
        revenue_data=payload.get("revenue_data", {}),
        client_context=payload.get("client_context", {}),
    )

    return {
        "status": "proposal_generated",
        "data": proposal
    }