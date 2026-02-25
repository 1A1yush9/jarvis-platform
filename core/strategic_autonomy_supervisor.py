# core/strategic_autonomy_supervisor.py

from typing import Dict, Any, List
from datetime import datetime


class StrategicAutonomySupervisor:
    """
    Stage-17.4

    Supervises executive decisions to ensure
    long-term strategic stability.
    """

    def __init__(self):
        self.engine = "Strategic Autonomy Supervisor"
        self.version = "17.4"

    # --------------------------------------------------
    # MAIN ENTRY
    # --------------------------------------------------

    def supervise(
        self,
        tenant_id: str,
        decisions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:

        stability_score = self._calculate_stability(decisions)
        drift_signal = self._detect_strategy_drift(decisions)

        return {
            "tenant_id": tenant_id,
            "engine": self.engine,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "stability_score": stability_score,
            "strategy_drift": drift_signal,
            "supervisor_advice":
                self._generate_advice(stability_score, drift_signal)
        }

    # --------------------------------------------------

    def _calculate_stability(self, decisions):

        if not decisions:
            return 0.5

        scores = [
            d.get("decision_score", 0.5)
            for d in decisions
        ]

        variance = max(scores) - min(scores)

        stability = 1 - min(variance, 1)
        return round(stability, 2)

    # --------------------------------------------------

    def _detect_strategy_drift(self, decisions):

        elevated_risk_count = 0

        for d in decisions:
            proposal = d.get("proposal", {})
            summary = proposal.get("proposal_summary", {})
            if summary.get("risk_assessment") == "Elevated":
                elevated_risk_count += 1

        if elevated_risk_count >= 2:
            return "Potential Drift"

        return "Stable"

    # --------------------------------------------------

    def _generate_advice(self, stability, drift):

        if drift == "Potential Drift":
            return "Strategic deviation detected. Re-evaluate opportunity selection."

        if stability > 0.75:
            return "Strategic alignment strong. Maintain current direction."

        if stability > 0.5:
            return "Minor variation detected. Monitor decision consistency."

        return "High volatility detected. Stabilization recommended."