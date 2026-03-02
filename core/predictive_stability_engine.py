"""
Jarvis Platform — Stage 56.0
Predictive Stability & Pre-Failure Anticipation Engine

Governance-Scoped Predictive Supervisor
(Non-executing, advisory-only)

IMPORTANT:
This engine DOES NOT overlap with predictive_engine.py.
It evaluates governance stability only.
"""

from datetime import datetime
from typing import Dict, Any, List


class PredictiveStabilityEngine:
    """
    Predicts governance instability trends.
    Passive supervisory component.
    """

    HISTORY_LIMIT = 40
    WARNING_THRESHOLD = 0.6

    def __init__(self, decision_trace=None):
        self.decision_trace = decision_trace
        self.signal_history: List[int] = []
        self.state = "STABLE"

    # --------------------------------------------------

    def evaluate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Governance-only prediction layer.
        """

        score = self._compute_signal_score(payload)

        self.signal_history.append(score)

        if len(self.signal_history) > self.HISTORY_LIMIT:
            self.signal_history.pop(0)

        trend = sum(self.signal_history) / len(self.signal_history)

        self.state = (
            "PRE_FAILURE_WARNING"
            if trend >= self.WARNING_THRESHOLD
            else "STABLE"
        )

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "trend_score": round(trend, 3),
            "prediction_state": self.state,
            "scope": "GOVERNANCE_STABILITY",
        }

        self._record(report)

        payload["predictive_stability"] = report
        return payload

    # --------------------------------------------------

    def _compute_signal_score(self, payload: Dict[str, Any]) -> int:
        score = 0

        # resilience degradation
        if payload.get("resilience"):
            score += 1

        # pressure regulation active
        pressure = payload.get("cognitive_pressure", {})
        if pressure.get("regulated"):
            score += 1

        # governance inconsistency
        meta = payload.get("meta_governance", {})
        if meta.get("meta_governance_state") == "INCONSISTENT":
            score += 1

        return score

    # --------------------------------------------------

    def _record(self, report: Dict[str, Any]) -> None:
        if self.decision_trace:
            self.decision_trace.record({
                "timestamp": report["timestamp"],
                "event": "PREDICTIVE_STABILITY_CHECK",
                "detail": report["prediction_state"],
                "layer": "PredictiveStabilityEngine",
            })


# Stable explicit export (prevents loader ambiguity)
predictive_stability_engine = PredictiveStabilityEngine

__all__ = [
    "PredictiveStabilityEngine",
    "predictive_stability_engine",
]