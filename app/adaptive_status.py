"""
Stage-36.0 Adaptive Learning API
"""

from fastapi import APIRouter
from core.shadow_operations import ExecutiveShadowOperations
from core.adaptive_learning import AdaptiveOperationalLearning

router = APIRouter()

shadow_engine = ExecutiveShadowOperations()
adaptive_engine = AdaptiveOperationalLearning()


@router.get("/adaptive-status")
def adaptive_status():

    intelligence_snapshot = {
        "confidence_score": 0.76,
        "risk_level": 0.28,
        "decision_convergence": 0.74,
    }

    shadow_result = shadow_engine.export(intelligence_snapshot)

    return adaptive_engine.export(shadow_result)