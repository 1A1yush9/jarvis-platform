from typing import Dict


class ResilienceSignalCollector:
    """
    Collects signals used to evaluate governance resilience.
    """

    def collect(
        self,
        cluster_stability: Dict,
        security_report: Dict,
        risk_forecast: Dict,
        oversight_report: Dict
    ) -> Dict:

        stability_state = cluster_stability.get("cluster_stability", "STABLE")

        anomalies = security_report.get("anomaly_summary", {}).get("anomaly_count", 0)

        risk_level = risk_forecast.get(
            "risk_assessment", {}
        ).get("risk_level", "LOW")

        drift = oversight_report.get(
            "strategic_analysis", {}
        ).get("systemic_drift_detected", False)

        return {
            "stability_state": stability_state,
            "anomaly_count": anomalies,
            "risk_level": risk_level,
            "systemic_drift": drift
        }