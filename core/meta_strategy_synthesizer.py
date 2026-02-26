"""
Stage-27.5 — Meta-Strategy Synthesizer (MSS)

Purpose:
Unify all executive cognition outputs into a single
coherent strategic narrative.

Design:
- Advisory only
- Non-directive synthesis
- Backward compatible
"""

from typing import Dict, Any


class MetaStrategySynthesizer:
    def __init__(self):
        self.version = "27.5"

    # --------------------------------------------------
    # Synthesis Logic
    # --------------------------------------------------
    def synthesize(
        self,
        alignment: Dict[str, Any],
        intent: Dict[str, Any],
        consistency: Dict[str, Any],
        foresight: Dict[str, Any],
        pressure: Dict[str, Any],
        equilibrium: Dict[str, Any],
    ) -> Dict[str, Any]:

        alignment_score = alignment.get("alignment_score", 0.5)
        consistency_score = consistency.get("consistency_score", 0.5)
        future_alignment = foresight.get("long_horizon_alignment", 0.5)
        pressure_score = pressure.get("pressure_score", 0.5)
        equilibrium_score = equilibrium.get("equilibrium_score", 0.5)

        composite_signal = (
            alignment_score * 0.25
            + consistency_score * 0.2
            + future_alignment * 0.2
            + equilibrium_score * 0.25
            - pressure_score * 0.2
        )

        composite_signal = max(0.0, min(1.0, composite_signal))

        narrative = self._generate_narrative(composite_signal)

        return {
            "meta_strategy_score": round(composite_signal, 3),
            "meta_strategy_state": self._state(composite_signal),
            "executive_meta_narrative": narrative,
            "synthesis_confidence": round(
                (alignment_score + consistency_score + equilibrium_score) / 3, 3
            ),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Narrative Generation
    # --------------------------------------------------
    def _state(self, score: float) -> str:
        if score >= 0.75:
            return "STRATEGIC_MOMENTUM"
        elif score >= 0.55:
            return "CONTROLLED_PROGRESS"
        elif score >= 0.4:
            return "TRANSITION_PHASE"
        return "STRATEGIC_INSTABILITY"

    def _generate_narrative(self, score: float) -> str:
        if score >= 0.75:
            return "Strategic systems aligned with strong forward momentum and sustainable balance."
        elif score >= 0.55:
            return "Organization progressing under controlled strategic conditions with manageable risk."
        elif score >= 0.4:
            return "Strategic posture entering transitional phase requiring executive attention."
        return "Systemic instability emerging across strategic dimensions."