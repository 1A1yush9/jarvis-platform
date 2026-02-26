"""
Stage-29.0 — Executive Meta-Reasoning Layer (EMRL)

Purpose:
Evaluate the integrity and stability of Jarvis'
own reasoning process across executive cognition layers.

Design:
- Advisory only
- Non-intervention
- Backward compatible
"""

from typing import Dict, Any


class ExecutiveMetaReasoning:
    def __init__(self):
        self.version = "29.0"

    # --------------------------------------------------
    # Meta-Reasoning Evaluation
    # --------------------------------------------------
    def evaluate_reasoning(
        self,
        meta_strategy: Dict[str, Any],
        calibration: Dict[str, Any],
        awareness: Dict[str, Any],
    ) -> Dict[str, Any]:

        meta_score = meta_strategy.get("meta_strategy_score", 0.5)
        confidence = calibration.get("calibrated_confidence", 0.5)

        awareness_state = awareness.get("awareness_state", "STABLE_AWARENESS")
        momentum = awareness.get("awareness_momentum", 0.0)

        agreement_gap = abs(meta_score - confidence)

        awareness_factor = self._awareness_factor(awareness_state)

        reasoning_integrity = (
            (1 - agreement_gap) * 0.5
            + confidence * 0.3
            + awareness_factor * 0.2
        )

        reasoning_integrity = max(0.0, min(1.0, reasoning_integrity))

        return {
            "meta_reasoning_score": round(reasoning_integrity, 3),
            "reasoning_state": self._state(reasoning_integrity, momentum),
            "meta_reasoning_advisory":
                self._generate_advisory(reasoning_integrity),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Awareness Interpretation
    # --------------------------------------------------
    def _awareness_factor(self, state: str) -> float:
        mapping = {
            "STRENGTHENING_AWARENESS": 0.9,
            "STABLE_AWARENESS": 0.7,
            "DECLINING_AWARENESS": 0.4,
        }
        return mapping.get(state, 0.6)

    # --------------------------------------------------
    # State + Advisory
    # --------------------------------------------------
    def _state(self, score: float, momentum: float) -> str:
        if score >= 0.8:
            return "HIGH_REASONING_INTEGRITY"
        elif score >= 0.6:
            return "STABLE_REASONING"
        elif score >= 0.45:
            return "REASONING_TENSION"
        return "REASONING_INSTABILITY"

    def _generate_advisory(self, score: float) -> str:
        if score >= 0.8:
            return "Executive reasoning pathways operating with strong integrity."
        elif score >= 0.6:
            return "Reasoning coherence stable across cognition layers."
        elif score >= 0.45:
            return "Minor reasoning divergence detected. Monitoring advised."
        return "Reasoning instability detected across executive cognition."