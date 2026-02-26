"""
Stage-27.0 — Executive Equilibrium Engine (EEE)

Purpose:
Evaluate whether strategic systems operate in a
balanced executive state between growth, risk,
and stability.

Design:
- Advisory only
- Non-intervention
- Backward compatible
"""

from typing import Dict, Any


class ExecutiveEquilibriumEngine:
    def __init__(self):
        self.version = "27.0"

    # --------------------------------------------------
    # Equilibrium Evaluation
    # --------------------------------------------------
    def evaluate_equilibrium(
        self,
        alignment: Dict[str, Any],
        consistency: Dict[str, Any],
        foresight: Dict[str, Any],
        pressure: Dict[str, Any],
    ) -> Dict[str, Any]:

        alignment_score = alignment.get("alignment_score", 0.5)
        consistency_score = consistency.get("consistency_score", 0.5)
        future_alignment = foresight.get("long_horizon_alignment", 0.5)
        pressure_score = pressure.get("pressure_score", 0.5)

        stability_component = (alignment_score + consistency_score) / 2
        sustainability_component = future_alignment
        stress_penalty = pressure_score

        equilibrium_score = (
            (stability_component * 0.45)
            + (sustainability_component * 0.4)
            - (stress_penalty * 0.35)
        )

        equilibrium_score = max(0.0, min(1.0, equilibrium_score))

        return {
            "equilibrium_score": round(equilibrium_score, 3),
            "equilibrium_state": self._state(equilibrium_score),
            "executive_equilibrium_advisory":
                self._generate_advisory(equilibrium_score),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # State Classification
    # --------------------------------------------------
    def _state(self, score: float) -> str:
        if score >= 0.75:
            return "OPTIMAL_BALANCE"
        elif score >= 0.55:
            return "STABLE_BALANCE"
        elif score >= 0.4:
            return "FRAGILE_BALANCE"
        return "IMBALANCED"

    def _generate_advisory(self, score: float) -> str:
        if score >= 0.75:
            return "Strategic system operating at executive equilibrium."
        elif score >= 0.55:
            return "Balanced trajectory maintained with monitoring advised."
        elif score >= 0.4:
            return "Balance weakening. Strategic adjustments may be required."
        return "Strategic imbalance detected. Executive reassessment recommended."