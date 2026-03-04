from typing import List, Dict


class GovernanceDriftAnalyzer:
    """
    Detects long-term governance instability patterns.
    """

    def analyze(self, history: List[Dict]) -> Dict:

        instability_count = 0
        risk_accumulator = 0.0

        for entry in history:

            stability = entry.get("cluster_stability", "STABLE")
            risk = entry.get("risk_level", "LOW")

            if stability != "STABLE":
                instability_count += 1

            if risk == "MEDIUM":
                risk_accumulator += 1

            if risk == "HIGH":
                risk_accumulator += 2

        drift_detected = False

        if instability_count >= 5 or risk_accumulator >= 6:
            drift_detected = True

        return {
            "instability_events": instability_count,
            "risk_accumulator": risk_accumulator,
            "systemic_drift_detected": drift_detected
        }