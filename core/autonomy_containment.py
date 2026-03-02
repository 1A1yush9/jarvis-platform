"""
Stage-37.0 — Strategic Autonomy Containment Protocol

Permanent safety boundary preventing unsafe autonomy.
Advisory cognition ONLY.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class ContainmentState:
    containment_state: str
    safety_score: float
    alerts: List[str]
    execution_permitted: bool = False


class StrategicAutonomyContainment:

    def __init__(self):
        self.last_score = 1.0

    # -------------------------------------
    # Containment Evaluation
    # -------------------------------------
    def evaluate(
        self,
        readiness: Dict,
        shadow: Dict,
        adaptive: Dict
    ) -> ContainmentState:

        alerts: List[str] = []

        readiness_score = readiness.get("readiness_score", 0.0)
        simulation_state = shadow.get("simulation_state", "UNSTABLE")
        adaptive_confidence = adaptive.get("adaptive_confidence", 0.0)
        regression = adaptive.get("regression_detected", True)

        safety_score = (
            readiness_score * 0.4 +
            adaptive_confidence * 0.4 +
            (1.0 if simulation_state == "STABLE" else 0.5) * 0.2
        )

        # --- Safety Checks ---
        if readiness_score < 0.6:
            alerts.append("Operational readiness below safe threshold")

        if simulation_state != "STABLE":
            alerts.append("Shadow simulations unstable")

        if regression:
            alerts.append("Adaptive regression detected")

        if adaptive_confidence < 0.6:
            alerts.append("Adaptive confidence insufficient")

        # --- Containment Decision ---
        if safety_score >= 0.8 and not alerts:
            state = "CONTAINED"
        elif safety_score >= 0.6:
            state = "GUARDED"
        else:
            state = "LOCKDOWN"

        self.last_score = safety_score

        return ContainmentState(
            containment_state=state,
            safety_score=round(safety_score, 4),
            alerts=alerts,
            execution_permitted=False
        )

    # -------------------------------------
    def export(self, readiness, shadow, adaptive) -> Dict:
        return asdict(self.evaluate(readiness, shadow, adaptive))