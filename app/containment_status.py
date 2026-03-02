"""
Stage-37.0 Containment Status API
"""

from fastapi import APIRouter

from core.operational_readiness import ExecutiveOperationalReadiness
from core.shadow_operations import ExecutiveShadowOperations
from core.adaptive_learning import AdaptiveOperationalLearning
from core.autonomy_containment import StrategicAutonomyContainment

router = APIRouter()

readiness_engine = ExecutiveOperationalReadiness()
shadow_engine = ExecutiveShadowOperations()
adaptive_engine = AdaptiveOperationalLearning()
containment_engine = StrategicAutonomyContainment()


@router.get("/containment-status")
def containment_status():

    readiness_snapshot = {
        "cognitive_stability": 0.75,
        "confidence_score": 0.78,
        "risk_level": 0.25,
        "strategic_drift": 0.20,
        "decision_convergence": 0.76,
        "calibration_health": 0.72,
    }

    readiness = readiness_engine.export(readiness_snapshot)

    shadow = shadow_engine.export({
        "confidence_score": readiness_snapshot["confidence_score"],
        "risk_level": readiness_snapshot["risk_level"],
        "decision_convergence": readiness_snapshot["decision_convergence"],
    })

    adaptive = adaptive_engine.export(shadow)

    return containment_engine.export(readiness, shadow, adaptive)