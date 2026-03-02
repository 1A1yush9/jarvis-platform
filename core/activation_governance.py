"""
Stage-38.0 — Controlled Activation Governance Layer

Determines if activation could EVER be allowed.
Does NOT activate the system.
Advisory cognition ONLY.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class ActivationGovernanceState:
    activation_state: str
    governance_score: float
    governance_reasons: List[str]
    activation_permitted: bool = False


class ControlledActivationGovernance:

    def __init__(self):
        self.last_score = 0.0

    # -------------------------------------
    # Governance Evaluation
    # -------------------------------------
    def evaluate(
        self,
        readiness: Dict,
        shadow: Dict,
        adaptive: Dict,
        containment: Dict
    ) -> ActivationGovernanceState:

        reasons: List[str] = []

        readiness_score = readiness.get("readiness_score", 0.0)
        simulation_state = shadow.get("simulation_state", "UNSTABLE")
        adaptive_confidence = adaptive.get("adaptive_confidence", 0.0)
        containment_state = containment.get("containment_state", "LOCKDOWN")

        governance_score = (
            readiness_score * 0.35 +
            adaptive_confidence * 0.35 +
            (1.0 if simulation_state == "STABLE" else 0.4) * 0.15 +
            (1.0 if containment_state == "CONTAINED" else 0.3) * 0.15
        )

        # --- Governance Rules ---
        if readiness_score < 0.75:
            reasons.append("Operational readiness insufficient")

        if simulation_state != "STABLE":
            reasons.append("Shadow operations not stable")

        if adaptive_confidence < 0.7:
            reasons.append("Adaptive learning maturity too low")

        if containment_state != "CONTAINED":
            reasons.append("Containment safety not satisfied")

        # --- Decision ---
        if governance_score >= 0.85 and not reasons:
            state = "ELIGIBLE"
        elif governance_score >= 0.65:
            state = "REVIEW"
        else:
            state = "DENIED"

        self.last_score = governance_score

        return ActivationGovernanceState(
            activation_state=state,
            governance_score=round(governance_score, 4),
            governance_reasons=reasons,
            activation_permitted=False
        )

    # -------------------------------------
    def export(self, readiness, shadow, adaptive, containment) -> Dict:
        return asdict(
            self.evaluate(readiness, shadow, adaptive, containment)
        )