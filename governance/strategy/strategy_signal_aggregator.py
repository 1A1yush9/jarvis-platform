from typing import Dict


class StrategySignalAggregator:
    """
    Aggregates governance intelligence signals for long-horizon strategy analysis.
    """

    def aggregate(
        self,
        evolution_report: Dict,
        resilience_report: Dict,
        oversight_report: Dict,
        risk_forecast: Dict
    ) -> Dict:

        policy_advice = evolution_report.get(
            "policy_evolution_advisory", {}
        ).get("policy_recommendations", [])

        resilience_level = resilience_report.get(
            "resilience_assessment", {}
        ).get("resilience_level", "LOW")

        drift = oversight_report.get(
            "strategic_analysis", {}
        ).get("systemic_drift_detected", False)

        risk_level = risk_forecast.get(
            "risk_assessment", {}
        ).get("risk_level", "LOW")

        return {
            "policy_advice": policy_advice,
            "resilience_level": resilience_level,
            "systemic_drift": drift,
            "risk_level": risk_level
        }