from fastapi import APIRouter
from .brain_service import brain_service

router = APIRouter(prefix="/brain", tags=["Brain Monitor"])


@router.get("/status")
def brain_status():
    return brain_service.status()


@router.get("/plans")
def brain_plans():
    return brain_service.plans()


@router.get("/agents")
def brain_agents():
    return brain_service.agents()


@router.get("/intuition")
def brain_intuition():
    return brain_service.intuition()
