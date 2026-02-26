"""
Stage-33.0 — Executive Strategic Compass (ESC)

Purpose:
Provide directional strategic orientation derived
from executive cognition signals.

Design:
- Advisory only
- Directional interpretation
- Backward compatible
"""

from typing import Dict, Any


class ExecutiveStrategicCompass:
    def __init__(self):
        self.version = "33.0"

    # --------------------------------------------------
    # Compass Evaluation
    # --------------------------------------------------
    def evaluate_direction(
        self,
        foresight: Dict[str, Any],
        pressure: Dict[str, Any],
        equilibrium: Dict[str, Any],
        doctrine: Dict[str, Any],
        paradox: Dict[str, Any],
    ) -> Dict[str, Any]:

        foresight_score = foresight.get("long_horizon_alignment", 0.5)
        pressure_score = pressure.get("pressure_score", 0.5)
        equilibrium_score = equilibrium.get("equilibrium_score", 0.5)
        doctrine_strength = doctrine.get("doctrine_strength", 0.5)
        paradox_intensity = paradox.get("paradox_intensity", 0.5)

        expansion_signal = foresight_score * (1 - pressure_score)
        stabilization_signal = equilibrium_score * (1 - paradox_intensity)
        consolidation_signal = doctrine_strength * pressure_score
        exploration_signal = paradox_intensity * (1 - doctrine_strength)

        signals = {
            "EXPAND": expansion_signal,
            "STABILIZE": stabilization_signal,
            "CONSOLIDATE": consolidation_signal,
            "EXPLORE": exploration_signal,
        }

        direction = max(signals, key=signals.get)
        confidence = signals[direction]

        return {
            "strategic_direction": direction,
            "direction_confidence": round(confidence, 3),
            "direction_state": self._state(confidence),
            "executive_direction_advisory":
                self._generate_advisory(direction, confidence),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # State + Advisory
    # --------------------------------------------------
    def _state(self, confidence: float) -> str:
        if confidence >= 0.75:
            return "STRONG_ORIENTATION"
        elif confidence >= 0.55:
            return "CLEAR_ORIENTATION"
        elif confidence >= 0.4:
            return "WEAK_ORIENTATION"
        return "UNSTABLE_ORIENTATION"

    def _generate_advisory(self, direction: str, confidence: float) -> str:
        if direction == "EXPAND":
            return "Conditions favor strategic expansion under current intelligence signals."
        elif direction == "STABILIZE":
            return "System conditions suggest maintaining stability and balance."
        elif direction == "CONSOLIDATE":
            return "Strategic consolidation indicated to reinforce established doctrine."
        return "Exploratory posture recommended due to unresolved strategic paradox."