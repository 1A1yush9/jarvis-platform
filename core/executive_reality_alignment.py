"""
Stage-31.5 — Executive Reality Alignment Field (ERAF)

Purpose:
Evaluate alignment between internal strategic worldview
and current operational reality signals.

Design:
- Advisory only
- Drift detection
- Backward compatible
"""

from typing import Dict, Any


class ExecutiveRealityAlignment:
    def __init__(self):
        self.version = "31.5"

    # --------------------------------------------------
    # Reality Alignment Evaluation
    # --------------------------------------------------
    def evaluate_reality_alignment(
        self,
        alignment: Dict[str, Any],
        consciousness: Dict[str, Any],
        foresight: Dict[str, Any],
    ) -> Dict[str, Any]:

        alignment_score = alignment.get("alignment_score", 0.5)
        worldview_score = consciousness.get(
            "strategic_consciousness_index", 0.5
        )
        future_projection = foresight.get(
            "long_horizon_alignment", 0.5
        )

        # Drift between worldview and present reality
        worldview_gap = abs(worldview_score - alignment_score)

        # Drift between worldview and expected future
        projection_gap = abs(worldview_score - future_projection)

        reality_alignment_index = 1 - (
            worldview_gap * 0.6 + projection_gap * 0.4
        )

        reality_alignment_index = max(
            0.0, min(1.0, reality_alignment_index)
        )

        return {
            "reality_alignment_index": round(reality_alignment_index, 3),
            "reality_alignment_state":
                self._state(reality_alignment_index),
            "executive_reality_advisory":
                self._generate_advisory(reality_alignment_index),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # State + Advisory
    # --------------------------------------------------
    def _state(self, score: float) -> str:
        if score >= 0.85:
            return "REALITY_SYNCHRONIZED"
        elif score >= 0.65:
            return "REALITY_ALIGNED"
        elif score >= 0.5:
            return "REALITY_TENSION"
        return "REALITY_DRIFT"

    def _generate_advisory(self, score: float) -> str:
        if score >= 0.85:
            return "Strategic worldview strongly synchronized with operational reality."
        elif score >= 0.65:
            return "Worldview aligned with reality within acceptable variance."
        elif score >= 0.5:
            return "Emerging mismatch between internal strategy and external signals."
        return "Significant reality drift detected. Executive reassessment advised."