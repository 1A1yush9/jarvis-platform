from typing import Dict


class ArchitectureSignalCollector:
    """
    Collects governance signals used for architecture evaluation.
    """

    def collect(
        self,
        strategy_report: Dict,
        evolution_report: Dict,
        resilience_report: Dict,
        oversight_report: Dict,
        risk_report: Dict
    ) -> Dict:

        strategy = strategy_report.get(
            "governance_strategy", {}
        ).get("strategic_recommendations", [])

        policies = evolution_report.get(
            "policy_evolution_advisory", {}
        ).get("policy_recommendations", [])

        resilience_level = resilience_report.get(
            "resilience_assessment", {}
        ).get("resilience_level", "LOW")

        drift = oversight_report.get(
            "strategic_analysis", {}
        ).get("systemic_drift_detected", False)

        risk_level = risk_report.get(
            "risk_assessment", {}
        ).get("risk_level", "LOW")

        return {
            "strategy": strategy,
            "policy_recommendations": policies,
            "resilience_level": resilience_level,
            "systemic_drift": drift,
            "risk_level": risk_level
        }