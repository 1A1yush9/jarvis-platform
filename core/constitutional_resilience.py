"""
Jarvis Platform — Stage 54.0
Constitutional Resilience Layer

Purpose:
Isolate failures and guarantee safe degradation
without breaking advisory cognition.
"""

from datetime import datetime
from typing import Callable, Any, Dict


class ConstitutionalResilience:
    """
    Wraps governance pipeline stages with failure isolation.
    """

    def __init__(self, decision_trace=None):
        self.decision_trace = decision_trace

    # --------------------------------------------------

    def protect(
        self,
        stage_name: str,
        operation: Callable[[], Any],
        payload: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Execute a stage safely.
        """

        try:
            result = operation()
            return result

        except Exception as exc:
            failure_report = {
                "timestamp": datetime.utcnow().isoformat(),
                "failed_stage": stage_name,
                "error": str(exc),
                "degraded_mode": True,
            }

            self._record_failure(failure_report)

            # Safe degradation:
            payload.setdefault("resilience", {})
            payload["resilience"][stage_name] = failure_report

            return payload

    # --------------------------------------------------

    def _record_failure(self, report: Dict[str, Any]) -> None:
        if self.decision_trace:
            self.decision_trace.record({
                "timestamp": report["timestamp"],
                "event": "RESILIENCE_FAILURE_ISOLATED",
                "detail": report["failed_stage"],
                "layer": "ConstitutionalResilience",
            })