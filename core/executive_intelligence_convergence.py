"""
Stage-30.0 — Executive Intelligence Convergence Layer (EICL)

Purpose:
Unify all executive cognition outputs into a single
intelligence state representation.

Design:
- Advisory only
- Aggregation-based convergence
- Backward compatible
"""

from typing import Dict, Any


class ExecutiveIntelligenceConvergence:
    def __init__(self):
        self.version = "30.0"

    # --------------------------------------------------
    # Convergence Evaluation
    # --------------------------------------------------
    def converge(
        self,
        alignment: Dict[str, Any],
        consistency: Dict[str, Any],
        foresight: Dict[str, Any],
        pressure: Dict[str, Any],
        equilibrium: Dict[str, Any],
        meta_strategy: Dict[str, Any],
        calibration: Dict[str, Any],
        meta_reasoning: Dict[str, Any],
        stability: Dict[str, Any],
    ) -> Dict[str, Any]:

        alignment_score = alignment.get("alignment_score", 0.5)
        consistency_score = consistency.get("consistency_score", 0.5)
        foresight_score = foresight.get("long_horizon_alignment", 0.5)
        pressure_score = pressure.get("pressure_score", 0.5)
        equilibrium_score = equilibrium.get("equilibrium_score", 0.5)
        meta_score = meta_strategy.get("meta_strategy_score", 0.5)
        confidence = calibration.get("calibrated_confidence", 0.5)
        reasoning_score = meta_reasoning.get("meta_reasoning_score", 0.5)
        stability_index = stability.get("cognitive_stability_index", 0.5)

        convergence_score = (
            alignment_score * 0.12
            + consistency_score * 0.1
            + foresight_score * 0.12
            + equilibrium_score * 0.14
            + meta_score * 0.14
            + confidence * 0.12
            + reasoning_score * 0.13
            + stability_index * 0.13
            - pressure_score * 0.1
        )

        convergence_score = max(0.0, min(1.0, convergence_score))

        return {
            "executive_intelligence_score": round(convergence_score, 3),
            "intelligence_state": self._state(convergence_score),
            "executive_intelligence_advisory":
                self._generate_advisory(convergence_score),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # State Classification
    # --------------------------------------------------
    def _state(self, score: float) -> str:
        if score >= 0.8:
            return "EXECUTIVE_SYNCHRONY"
        elif score >= 0.65:
            return "COHERENT_INTELLIGENCE"
        elif score >= 0.5:
            return "PARTIAL_CONVERGENCE"
        return "SYSTEMIC_DIVERGENCE"

    def _generate_advisory(self, score: float) -> str:
        if score >= 0.8:
            return "Executive cognition operating in synchronized intelligence state."
        elif score >= 0.65:
            return "Executive intelligence coherent with manageable variance."
        elif score >= 0.5:
            return "Partial convergence detected. Strategic monitoring advised."
        return "Divergence across cognition layers detected."