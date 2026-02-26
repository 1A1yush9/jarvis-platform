"""
Stage-24 — Executive Alignment Engine (EAE)

Purpose:
Ensure all strategic cognition remains aligned with
long-term executive intent.

Operating Mode:
Advisory ONLY (no execution authority)

Safe Design:
- Stateless evaluation
- Backward compatible
- Optional inputs supported
"""

from typing import Dict, Any
import math


class ExecutiveAlignmentEngine:
    def __init__(self):
        self.version = "24.0"
        self.alignment_threshold = 0.65

    # --------------------------------------------------
    # Core Alignment Evaluation
    # --------------------------------------------------
    def evaluate_alignment(
        self,
        strategic_context: Dict[str, Any],
        simulation_output: Dict[str, Any],
        narrative_output: Dict[str, Any],
    ) -> Dict[str, Any]:

        mission_vector = strategic_context.get("mission_priority", 0.7)
        growth_focus = strategic_context.get("growth_focus", 0.6)
        risk_tolerance = strategic_context.get("risk_tolerance", 0.5)

        simulated_aggressiveness = simulation_output.get(
            "aggressiveness_score", 0.5
        )

        narrative_bias = narrative_output.get(
            "strategic_bias_score", 0.5
        )

        # Alignment math (stable + interpretable)
        mission_alignment = 1 - abs(simulated_aggressiveness - mission_vector)
        growth_alignment = 1 - abs(narrative_bias - growth_focus)

        risk_alignment = 1 - abs(
            simulation_output.get("risk_level", 0.5) - risk_tolerance
        )

        alignment_score = (
            mission_alignment * 0.4
            + growth_alignment * 0.35
            + risk_alignment * 0.25
        )

        alignment_score = max(0.0, min(1.0, alignment_score))

        advisory = self._generate_advisory(alignment_score)

        return {
            "alignment_score": round(alignment_score, 3),
            "alignment_status": self._status(alignment_score),
            "executive_alignment_advisory": advisory,
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Advisory Generator
    # --------------------------------------------------
    def _generate_advisory(self, score: float) -> str:
        if score >= 0.8:
            return "Strategic direction strongly aligned with executive intent."
        elif score >= self.alignment_threshold:
            return "Moderate alignment detected. Monitor for gradual drift."
        elif score >= 0.45:
            return "Noticeable strategic deviation forming. Recommend executive review."
        else:
            return "Critical misalignment risk. Strategic recalibration advised."

    def _status(self, score: float) -> str:
        if score >= 0.8:
            return "ALIGNED"
        elif score >= self.alignment_threshold:
            return "STABLE"
        elif score >= 0.45:
            return "DRIFTING"
        return "MISALIGNED"