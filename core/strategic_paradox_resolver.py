"""
Stage-32.5 — Strategic Paradox Resolver (SPR)

Purpose:
Detect and interpret simultaneous conflicting
strategic signals across executive cognition layers.

Design:
- Advisory only
- Conflict interpretation
- Backward compatible
"""

from typing import Dict, Any


class StrategicParadoxResolver:
    def __init__(self):
        self.version = "32.5"

    # --------------------------------------------------
    # Paradox Detection
    # --------------------------------------------------
    def evaluate_paradox(
        self,
        foresight: Dict[str, Any],
        pressure: Dict[str, Any],
        equilibrium: Dict[str, Any],
        doctrine: Dict[str, Any],
    ) -> Dict[str, Any]:

        future_alignment = foresight.get("long_horizon_alignment", 0.5)
        pressure_score = pressure.get("pressure_score", 0.5)
        equilibrium_score = equilibrium.get("equilibrium_score", 0.5)
        doctrine_strength = doctrine.get("doctrine_strength", 0.5)

        # Conflict measurements
        growth_vs_pressure = abs(future_alignment - (1 - pressure_score))
        doctrine_vs_equilibrium = abs(doctrine_strength - equilibrium_score)

        paradox_intensity = (
            growth_vs_pressure * 0.55
            + doctrine_vs_equilibrium * 0.45
        )

        paradox_intensity = max(0.0, min(1.0, paradox_intensity))

        return {
            "paradox_intensity": round(paradox_intensity, 3),
            "paradox_state": self._state(paradox_intensity),
            "paradox_type": self._type(
                growth_vs_pressure,
                doctrine_vs_equilibrium
            ),
            "executive_paradox_advisory":
                self._generate_advisory(paradox_intensity),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Classification
    # --------------------------------------------------
    def _state(self, score: float) -> str:
        if score < 0.3:
            return "LOW_PARADOX"
        elif score < 0.55:
            return "MANAGEABLE_PARADOX"
        elif score < 0.75:
            return "HIGH_PARADOX"
        return "CRITICAL_PARADOX"

    def _type(self, gvp: float, dve: float) -> str:
        if gvp > dve:
            return "GROWTH_PRESSURE_CONFLICT"
        return "DOCTRINE_BALANCE_CONFLICT"

    def _generate_advisory(self, score: float) -> str:
        if score < 0.3:
            return "Strategic signals largely coherent."
        elif score < 0.55:
            return "Competing strategic truths detected. Executive prioritization required."
        elif score < 0.75:
            return "High paradox environment. Avoid premature certainty."
        return "Critical strategic paradox detected. Multi-path evaluation advised."