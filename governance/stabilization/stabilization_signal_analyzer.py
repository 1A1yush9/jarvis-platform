from typing import Dict


class StabilizationSignalAnalyzer:
    """
    Converts governance signals into stabilization triggers.
    """

    def analyze(
        self,
        risk_forecast: Dict,
        cluster_stability: Dict
    ) -> Dict:

        risk = risk_forecast.get("risk_assessment", {})
        risk_level = risk.get("risk_level", "LOW")

        stability_state = cluster_stability.get("cluster_stability", "STABLE")

        trigger = False

        if risk_level in ["MEDIUM", "HIGH"]:
            trigger = True

        if stability_state != "STABLE":
            trigger = True

        return {
            "risk_level": risk_level,
            "stability_state": stability_state,
            "stabilization_required": trigger
        }