from typing import Dict


class GovernanceRiskModel:
    """
    Deterministic risk scoring model.
    """

    MISMATCH_WEIGHT = 0.5
    ANOMALY_WEIGHT = 0.3
    ISOLATION_WEIGHT = 0.2

    def score(self, signals: Dict) -> Dict:

        mismatch_score = signals["mismatch_count"] * self.MISMATCH_WEIGHT
        anomaly_score = signals["anomaly_count"] * self.ANOMALY_WEIGHT
        isolation_score = signals["isolated_nodes"] * self.ISOLATION_WEIGHT

        total = mismatch_score + anomaly_score + isolation_score

        risk_level = "LOW"

        if total >= 2:
            risk_level = "MEDIUM"

        if total >= 4:
            risk_level = "HIGH"

        return {
            "risk_score": round(total, 4),
            "risk_level": risk_level
        }