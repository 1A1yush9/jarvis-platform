"""
Jarvis Platform — Stage 51.0
Self-Audit & Governance Verification Engine

Purpose:
Continuously verify constitutional safety conditions.
This layer NEVER executes actions — audit only.
"""

from datetime import datetime
from typing import Dict, Any, Optional


class GovernanceSelfAudit:
    """
    Continuous governance verification engine.
    """

    def __init__(
        self,
        autonomy_boundary=None,
        decision_trace=None,
        stability_regulator=None,
    ):
        self.autonomy_boundary = autonomy_boundary
        self.decision_trace = decision_trace
        self.stability_regulator = stability_regulator

        self.last_audit = None

    # --------------------------------------------------

    def run_audit(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes passive governance verification.
        """

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "checks": {
                "advisory_mode": self._check_advisory_mode(),
                "autonomy_boundary_active": self._check_autonomy_boundary(),
                "cognitive_stability": self._check_stability(),
                "execution_authority": False,
            },
        }

        report["status"] = self._derive_status(report["checks"])

        self.last_audit = report
        self._record(report)

        payload["governance_audit"] = report
        return payload

    # --------------------------------------------------
    # CHECKS
    # --------------------------------------------------

    def _check_advisory_mode(self) -> bool:
        if not self.autonomy_boundary:
            return False
        return getattr(
            self.autonomy_boundary,
            "system_mode",
            None,
        ) == "ADVISORY_ONLY"

    def _check_autonomy_boundary(self) -> bool:
        return self.autonomy_boundary is not None

    def _check_stability(self) -> bool:
        if not self.stability_regulator:
            return True
        return not getattr(
            self.stability_regulator,
            "instability_detected",
            False,
        )

    # --------------------------------------------------

    def _derive_status(self, checks: Dict[str, bool]) -> str:
        if all(checks.values()):
            return "SAFE"
        return "ATTENTION_REQUIRED"

    # --------------------------------------------------

    def _record(self, report: Dict[str, Any]) -> None:
        if self.decision_trace:
            self.decision_trace.record({
                "timestamp": report["timestamp"],
                "event": "GOVERNANCE_SELF_AUDIT",
                "detail": report["status"],
                "layer": "GovernanceSelfAudit"
            })