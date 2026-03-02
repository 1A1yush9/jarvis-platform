"""
Stage-47.0 — Executive Memory API

Provides advisory knowledge persistence endpoints.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

from core.executive_memory_index import executive_memory_index

router = APIRouter(prefix="/memory", tags=["Executive Memory"])


class MemoryCreate(BaseModel):
    title: str
    content: Dict[str, Any]
    tags: List[str]


@router.post("/store")
def store_memory(data: MemoryCreate):
    return executive_memory_index.store_memory(
        data.title,
        data.content,
        data.tags,
    )


@router.get("/{memory_id}")
def get_memory(memory_id: str):
    result = executive_memory_index.get_memory(memory_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result


@router.get("/tag/{tag}")
def search_tag(tag: str):
    return executive_memory_index.search_by_tag(tag)


@router.get("/")
def overview():
    return executive_memory_index.overview()