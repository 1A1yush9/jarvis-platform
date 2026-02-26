"""
Stage-28.0 — Executive Self-Calibration Engine (ESCE)

Purpose:
Dynamically calibrate confidence weighting across
executive cognition layers.

Design:
- Advisory only
- Non-intervention
- Backward compatible
"""

from typing import Dict, Any


class ExecutiveSelfCalibration:
    def __init__(self):
        self.version = "28.0"

    # --------------------------------------------------
    # Calibration Evaluation
    # --------------------------------------------------
    def calibrate(
        self,
        alignment: Dict[str, Any],
        consistency: Dict[str, Any],
        foresight: Dict[str, Any],
        pressure: Dict[str, Any],
        equilibrium: Dict[str, Any],
        meta_strategy: Dict[str, Any],
    ) -> Dict[str, Any]:

        alignment_score = alignment.get("alignment_score", 0.5)
        consistency_score = consistency.get("consistency_score", 0.5)
        foresight_score = foresight.get("long_horizon_alignment", 0.5)
        pressure_score = pressure.get("pressure_score", 0.5)
        equilibrium_score = equilibrium.get("equilibrium_score", 0.5)
        meta_score = meta_strategy.get("meta_strategy_score", 0.5)

        # Dynamic weighting logic
        stability_weight = (alignment_score + consistency_score) / 2
        foresight_weight = foresight_score
        pressure_weight = 1 - pressure_score

        calibrated_confidence = (
            stability_weight * 0.3
            + foresight_weight * 0.25
            + pressure_weight * 0.2
            + equilibrium_score * 0.15
            + meta_score * 0.1
        )

        calibrated_confidence = max(0.0, min(1.0, calibrated_confidence))

        return {
            "calibrated_confidence": round(calibrated_confidence, 3),
            "confidence_state": self._state(calibrated_confidence),
            "calibration_advisory":
                self._generate_advisory(calibrated_confidence),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # State Classification
    # --------------------------------------------------
    def _state(self, score: float) -> str:
        if score >= 0.8:
            return "HIGH_CONFIDENCE"
        elif score >= 0.6:
            return "CALIBRATED"
        elif score >= 0.45:
            return "UNCERTAIN"
        return "LOW_CONFIDENCE"

    def _generate_advisory(self, score: float) -> str:
        if score >= 0.8:
            return "Executive cognition operating with strong calibrated confidence."
        elif score >= 0.6:
            return "Confidence levels balanced across intelligence layers."
        elif score >= 0.45:
            return "Confidence dispersion detected. Increased monitoring advised."
        return "Low confidence environment detected across cognition layers."