"""
Risk Horizon Model

Deterministic classification logic for civilizational risk horizons.
"""

from typing import Dict


class RiskHorizonModel:

    def classify(
        self,
        normalized_vector: Dict[str, float],
        cascade_risk_score: float
    ) -> str:

        long_term = normalized_vector.get("long_term", 0.0)

        if cascade_risk_score <= 0.05 and long_term >= 0.33:
            return "LONG_STABLE"

        if cascade_risk_score <= 0.12:
            return "TRANSITIONAL"

        return "FRAGMENTING"