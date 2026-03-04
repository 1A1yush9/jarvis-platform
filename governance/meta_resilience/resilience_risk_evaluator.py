from typing import Dict


class ResilienceRiskEvaluator:
    """
    Determines governance architecture resilience risk.
    """

    def evaluate(self, signals: Dict) -> Dict:

        score = 0

        if signals["stability_state"] != "STABLE":
            score += 2

        if signals["anomaly_count"] > 0:
            score += 1

        if signals["risk_level"] == "MEDIUM":
            score += 1

        if signals["risk_level"] == "HIGH":
            score += 2

        if signals["systemic_drift"]:
            score += 2

        level = "LOW"

        if score >= 3:
            level = "MEDIUM"

        if score >= 5:
            level = "HIGH"

        return {
            "resilience_score": score,
            "resilience_level": level
        }