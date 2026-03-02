"""
Stage-48.0 — Strategic Awareness API

Provides cross-system intelligence linking endpoints.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from core.strategic_awareness_graph import strategic_awareness_graph

router = APIRouter(prefix="/awareness", tags=["Strategic Awareness"])


class NodeCreate(BaseModel):
    node_type: str
    reference_id: str
    metadata: Dict[str, Any]


class LinkCreate(BaseModel):
    source_node_id: str
    target_node_id: str
    relation: str


@router.post("/node")
def create_node(data: NodeCreate):
    return strategic_awareness_graph.create_node(
        data.node_type,
        data.reference_id,
        data.metadata,
    )


@router.post("/link")
def link_nodes(data: LinkCreate):
    result = strategic_awareness_graph.link_nodes(
        data.source_node_id,
        data.target_node_id,
        data.relation,
    )

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result


@router.get("/snapshot")
def snapshot():
    return strategic_awareness_graph.snapshot()