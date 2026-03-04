from typing import Dict


class ArchitectureRiskAnalyzer:
    """
    Determines governance architecture risk posture.
    """

    def analyze(self, signals: Dict) -> Dict:

        score = 0

        if signals["risk_level"] == "HIGH":
            score += 3

        if signals["risk_level"] == "MEDIUM":
            score += 1

        if signals["resilience_level"] == "MEDIUM":
            score += 1

        if signals["resilience_level"] == "HIGH":
            score += 2

        if signals["systemic_drift"]:
            score += 2

        level = "STABLE"

        if score >= 3:
            level = "WATCH"

        if score >= 6:
            level = "ARCHITECTURE_RISK"

        return {
            "architecture_risk_score": score,
            "architecture_risk_level": level
        }