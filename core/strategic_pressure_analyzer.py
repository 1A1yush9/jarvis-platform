"""
Stage-26.5 — Strategic Pressure Analyzer (SPA)

Purpose:
Detect hidden systemic pressure forming across
executive cognition layers.

Design:
- Advisory only
- Non-intervention
- Backward compatible
"""

from typing import Dict, Any


class StrategicPressureAnalyzer:
    def __init__(self):
        self.version = "26.5"

    # --------------------------------------------------
    # Pressure Evaluation
    # --------------------------------------------------
    def analyze_pressure(
        self,
        alignment: Dict[str, Any],
        intent: Dict[str, Any],
        consistency: Dict[str, Any],
        foresight: Dict[str, Any],
    ) -> Dict[str, Any]:

        alignment_score = alignment.get("alignment_score", 0.5)
        consistency_score = consistency.get("consistency_score", 0.5)

        intent_vector = intent.get("intent_vector", {})
        volatility = intent_vector.get("behavioral_volatility", 0.1)

        future_alignment = foresight.get("long_horizon_alignment", 0.5)

        # Pressure logic
        alignment_pressure = 1 - alignment_score
        consistency_pressure = 1 - consistency_score
        foresight_pressure = max(0, alignment_score - future_alignment)

        volatility_pressure = min(1.0, volatility * 2)

        pressure_score = (
            alignment_pressure * 0.3
            + consistency_pressure * 0.25
            + foresight_pressure * 0.25
            + volatility_pressure * 0.2
        )

        pressure_score = max(0.0, min(1.0, pressure_score))

        return {
            "pressure_score": round(pressure_score, 3),
            "pressure_status": self._status(pressure_score),
            "executive_pressure_advisory":
                self._generate_advisory(pressure_score),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Status + Advisory
    # --------------------------------------------------
    def _status(self, score: float) -> str:
        if score < 0.3:
            return "LOW_PRESSURE"
        elif score < 0.55:
            return "BUILDING_PRESSURE"
        elif score < 0.75:
            return "ELEVATED_PRESSURE"
        return "CRITICAL_PRESSURE"

    def _generate_advisory(self, score: float) -> str:
        if score < 0.3:
            return "Strategic system operating under stable conditions."
        elif score < 0.55:
            return "Early pressure signals detected. Monitor closely."
        elif score < 0.75:
            return "Strategic stress accumulating across cognition layers."
        return "Critical systemic pressure detected. Executive review advised."