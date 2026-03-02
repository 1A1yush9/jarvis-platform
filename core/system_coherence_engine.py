"""
Jarvis Platform — Stage 57.0
System Coherence & Signal Harmonization Layer

Purpose:
Unify multi-engine signals into a coherent global state.
Advisory-only normalization.
"""

from datetime import datetime
from typing import Dict, Any


class SystemCoherenceEngine:
    """
    Harmonizes governance, pressure, and prediction signals.
    """

    def __init__(self, decision_trace=None):
        self.decision_trace = decision_trace
        self.last_state = "COHERENT"

    # --------------------------------------------------

    def harmonize(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        coherence_score = 0
        checks = {}

        # --- pressure signal ---
        pressure = payload.get("cognitive_pressure", {})
        checks["pressure_ok"] = pressure.get("state") != "HIGH"

        # --- governance consistency ---
        meta = payload.get("meta_governance", {})
        checks["governance_ok"] = (
            meta.get("meta_governance_state") != "INCONSISTENT"
        )

        # --- predictive stability ---
        prediction = payload.get("predictive_stability", {})
        checks["prediction_ok"] = (
            prediction.get("prediction_state") != "PRE_FAILURE_WARNING"
        )

        coherence_score = sum(1 for v in checks.values() if v)

        if coherence_score == len(checks):
            self.last_state = "COHERENT"
        elif coherence_score >= 1:
            self.last_state = "PARTIAL_STRESS"
        else:
            self.last_state = "SYSTEM_STRESS"

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "checks": checks,
            "coherence_state": self.last_state,
        }

        self._record(report)

        payload["system_coherence"] = report
        return payload

    # --------------------------------------------------

    def _record(self, report: Dict[str, Any]) -> None:
        if self.decision_trace:
            self.decision_trace.record({
                "timestamp": report["timestamp"],
                "event": "SYSTEM_COHERENCE_EVALUATED",
                "detail": report["coherence_state"],
                "layer": "SystemCoherenceEngine",
            })


# stable export
system_coherence_engine = SystemCoherenceEngine

__all__ = [
    "SystemCoherenceEngine",
    "system_coherence_engine",
]