"""
Jarvis Platform — Stage-64.0
Unified Stability Telemetry & Audit Aggregator

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Aggregates stability and governance reports into a single
deterministic telemetry index and audit snapshot.

This module:
- Consolidates cross-layer reports
- Computes unified stability index
- Generates deterministic audit fingerprints
- Emits advisory meta-health signals
- Never executes corrective actions

Design Guarantees:
------------------
- Deterministic logic
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
import hashlib
from typing import Dict, Any, List


class UnifiedStabilityTelemetry:
    """
    Stage-64.0 Stability Observability Layer

    Aggregates:
    - Containment states
    - Integrity violations
    - Equilibrium violations
    - Arbitration states
    """

    VERSION = "64.0"

    def __init__(self):
        self._lock = threading.Lock()
        self._last_snapshot = None
        self._last_index = 1.0  # 1.0 = fully stable
        self._meta_violation = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def aggregate(self, reports: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Aggregate governance layer reports.

        Parameters:
        -----------
        reports : list of dict

        Returns:
        --------
        Unified telemetry report.
        """

        with self._lock:
            violation_count = self._count_total_violations(reports)
            total_reports = len(reports) if reports else 1

            stability_index = self._compute_stability_index(
                violation_count,
                total_reports
            )

            audit_fingerprint = self._generate_audit_fingerprint(reports)

            containment_reason = self._evaluate_meta_health(stability_index)

            report = {
                "telemetry_version": self.VERSION,
                "total_reports": total_reports,
                "violation_count": violation_count,
                "stability_index": round(stability_index, 4),
                "audit_fingerprint": audit_fingerprint,
                "meta_violation": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._last_snapshot = report
            self._last_index = stability_index
            self._meta_violation = containment_reason is not None

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _count_total_violations(self, reports: List[Dict[str, Any]]) -> int:
        """
        Count all active violations across reports.
        """
        count = 0

        for r in reports:
            if (
                r.get("containment_active")
                or r.get("integrity_violation")
                or r.get("equilibrium_violation")
                or r.get("saturation_detected")
            ):
                count += 1

        return count

    def _compute_stability_index(
        self,
        violations: int,
        total: int
    ) -> float:
        """
        Computes normalized stability index.
        """
        return max(0.0, 1.0 - (violations / total))

    def _generate_audit_fingerprint(self, reports: List[Dict[str, Any]]) -> str:
        """
        Deterministic fingerprint of aggregated reports.
        """
        serialized = str(sorted([
            sorted(r.items()) for r in reports
        ]))
        return hashlib.sha256(serialized.encode()).hexdigest()

    def _evaluate_meta_health(self, stability_index: float) -> str | None:
        """
        Determine if meta-health violation exists.
        """
        if stability_index < 0.5:
            return "SYSTEMIC_STABILITY_DEGRADATION"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory-only recommended action.
        """
        if reason == "SYSTEMIC_STABILITY_DEGRADATION":
            return "INITIATE_GLOBAL_GOVERNANCE_REVIEW"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "telemetry_version": self.VERSION,
            "last_stability_index": round(self._last_index, 4),
            "meta_violation": self._meta_violation,
            "last_snapshot": self._last_snapshot
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_unified_stability_telemetry() -> UnifiedStabilityTelemetry:
    """
    Backward compatible instantiation.
    """
    return UnifiedStabilityTelemetry()