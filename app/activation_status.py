"""
Stage-38.0 Activation Governance API
"""

from fastapi import APIRouter

from core.operational_readiness import ExecutiveOperationalReadiness
from core.shadow_operations import ExecutiveShadowOperations
from core.adaptive_learning import AdaptiveOperationalLearning
from core.autonomy_containment import StrategicAutonomyContainment
from core.activation_governance import ControlledActivationGovernance

router = APIRouter()

readiness_engine = ExecutiveOperationalReadiness()
shadow_engine = ExecutiveShadowOperations()
adaptive_engine = AdaptiveOperationalLearning()
containment_engine = StrategicAutonomyContainment()
governance_engine = ControlledActivationGovernance()


@router.get("/activation-status")
def activation_status():

    readiness_snapshot = {
        "cognitive_stability": 0.78,
        "confidence_score": 0.80,
        "risk_level": 0.22,
        "strategic_drift": 0.18,
        "decision_convergence": 0.79,
        "calibration_health": 0.75,
    }

    readiness = readiness_engine.export(readiness_snapshot)

    shadow = shadow_engine.export({
        "confidence_score": readiness_snapshot["confidence_score"],
        "risk_level": readiness_snapshot["risk_level"],
        "decision_convergence": readiness_snapshot["decision_convergence"],
    })

    adaptive = adaptive_engine.export(shadow)

    containment = containment_engine.export(
        readiness, shadow, adaptive
    )

    return governance_engine.export(
        readiness, shadow, adaptive, containment
    )