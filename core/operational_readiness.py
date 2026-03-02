"""
Stage-34.0 — Executive Operational Readiness Engine

Advisory cognition ONLY.
Determines if system is safe to begin operational execution.
NO ACTION EXECUTION PERMITTED.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class OperationalReadinessState:
    operational_state: str
    readiness_score: float
    blocking_factors: List[str]
    advisory_mode: bool = True


class ExecutiveOperationalReadiness:
    """
    Evaluates system-wide cognitive readiness.
    """

    def __init__(self):
        self.last_score = 0.0

    # -----------------------------
    # Core Evaluation
    # -----------------------------
    def evaluate(self, intelligence_snapshot: Dict) -> OperationalReadinessState:

        blocking: List[str] = []

        stability = intelligence_snapshot.get("cognitive_stability", 0.0)
        confidence = intelligence_snapshot.get("confidence_score", 0.0)
        risk = intelligence_snapshot.get("risk_level", 1.0)
        drift = intelligence_snapshot.get("strategic_drift", 1.0)
        convergence = intelligence_snapshot.get("decision_convergence", 0.0)
        calibration = intelligence_snapshot.get("calibration_health", 0.0)

        score = (
            stability * 0.20
            + confidence * 0.25
            + (1 - risk) * 0.20
            + (1 - drift) * 0.15
            + convergence * 0.10
            + calibration * 0.10
        )

        # --- Blocking Analysis ---
        if stability < 0.7:
            blocking.append("Cognitive stability insufficient")

        if confidence < 0.75:
            blocking.append("Confidence convergence incomplete")

        if risk > 0.4:
            blocking.append("Risk radar elevated")

        if drift > 0.3:
            blocking.append("Strategic drift detected")

        if convergence < 0.7:
            blocking.append("Decision simulations not convergent")

        if calibration < 0.65:
            blocking.append("Self-calibration unstable")

        # --- State Determination ---
        if score >= 0.85 and not blocking:
            state = "OPERATIONAL_READY"
        elif score >= 0.65:
            state = "SHADOW_READY"
        else:
            state = "NOT_READY"

        self.last_score = score

        return OperationalReadinessState(
            operational_state=state,
            readiness_score=round(score, 4),
            blocking_factors=blocking,
            advisory_mode=True,
        )

    # -----------------------------
    # Export Safe Dict
    # -----------------------------
    def export(self, intelligence_snapshot: Dict) -> Dict:
        result = self.evaluate(intelligence_snapshot)
        return asdict(result)