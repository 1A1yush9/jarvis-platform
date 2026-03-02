"""
Jarvis Platform — Stage 53.0
Meta-Governance Sentinel

Purpose:
Verify internal governance layers remain present,
ordered, and constitutionally consistent.

Audit-only supervisory system.
"""

from datetime import datetime
from typing import Dict, Any, List


class MetaGovernanceSentinel:
    """
    Supervises governance self-consistency.
    """

    REQUIRED_MARKERS: List[str] = [
        "autonomy_boundary",
        "governance_audit",
        "cognitive_integrity",
    ]

    def __init__(self, decision_trace=None):
        self.decision_trace = decision_trace
        self.last_status = "UNKNOWN"

    # --------------------------------------------------

    def supervise(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate governance consistency markers.
        """

        checks = {
            marker: marker in payload
            for marker in self.REQUIRED_MARKERS
        }

        consistent = all(checks.values())

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "governance_markers_present": checks,
            "meta_governance_state": (
                "CONSISTENT" if consistent else "INCONSISTENT"
            ),
        }

        self.last_status = report["meta_governance_state"]

        self._record(report)

        payload["meta_governance"] = report
        return payload

    # --------------------------------------------------

    def _record(self, report: Dict[str, Any]) -> None:
        if self.decision_trace:
            self.decision_trace.record({
                "timestamp": report["timestamp"],
                "event": "META_GOVERNANCE_CHECK",
                "detail": report["meta_governance_state"],
                "layer": "MetaGovernanceSentinel",
            })