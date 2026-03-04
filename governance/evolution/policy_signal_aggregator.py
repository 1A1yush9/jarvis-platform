from typing import Dict


class PolicySignalAggregator:
    """
    Aggregates governance signals used for policy evolution analysis.
    """

    def aggregate(
        self,
        meta_resilience: Dict,
        risk_forecast: Dict,
        oversight: Dict
    ) -> Dict:

        resilience_level = meta_resilience.get(
            "resilience_assessment", {}
        ).get("resilience_level", "LOW")

        risk_level = risk_forecast.get(
            "risk_assessment", {}
        ).get("risk_level", "LOW")

        drift_detected = oversight.get(
            "strategic_analysis", {}
        ).get("systemic_drift_detected", False)

        return {
            "resilience_level": resilience_level,
            "risk_level": risk_level,
            "systemic_drift": drift_detected
        }