"""
Stage-25.5 — Cognitive Consistency Governor (CCG)

Purpose:
Detect contradictions between cognitive subsystems
and evaluate advisory coherence.

Design:
- Advisory only
- Non-intervention architecture
- Backward compatible
"""

from typing import Dict, Any


class CognitiveConsistencyGovernor:
    def __init__(self):
        self.version = "25.5"

    # --------------------------------------------------
    # Consistency Evaluation
    # --------------------------------------------------
    def evaluate_consistency(
        self,
        alignment: Dict[str, Any],
        intent: Dict[str, Any],
        simulation_output: Dict[str, Any],
    ) -> Dict[str, Any]:

        alignment_score = alignment.get("alignment_score", 0.5)

        aggressiveness = simulation_output.get(
            "aggressiveness_score", 0.5
        )

        intent_vector = intent.get("intent_vector", {})
        strategic_bias = intent_vector.get("strategic_bias", "BALANCED_GROWTH")

        bias_expected = self._bias_expected_value(strategic_bias)

        bias_gap = abs(aggressiveness - bias_expected)
        alignment_gap = abs(alignment_score - bias_expected)

        consistency_score = 1 - ((bias_gap * 0.6) + (alignment_gap * 0.4))
        consistency_score = max(0.0, min(1.0, consistency_score))

        return {
            "consistency_score": round(consistency_score, 3),
            "consistency_status": self._status(consistency_score),
            "executive_consistency_advisory":
                self._generate_advisory(consistency_score),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Expected Bias Mapping
    # --------------------------------------------------
    def _bias_expected_value(self, bias: str) -> float:

        mapping = {
            "LONG_TERM_STABILITY": 0.4,
            "BALANCED_GROWTH": 0.6,
            "ADAPTIVE_EXPERIMENTATION": 0.75,
        }

        return mapping.get(bias, 0.6)

    # --------------------------------------------------
    # Status + Advisory
    # --------------------------------------------------
    def _status(self, score: float) -> str:
        if score >= 0.8:
            return "COHERENT"
        elif score >= 0.6:
            return "STABLE"
        elif score >= 0.45:
            return "TENSION_DETECTED"
        return "CONTRADICTION_RISK"

    def _generate_advisory(self, score: float) -> str:
        if score >= 0.8:
            return "Cognitive systems aligned with consistent executive logic."
        elif score >= 0.6:
            return "Minor divergence detected. Monitor advisory coherence."
        elif score >= 0.45:
            return "Strategic tension emerging between intelligence layers."
        return "High contradiction risk across cognitive outputs."