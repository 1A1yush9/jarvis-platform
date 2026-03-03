"""
Jarvis Platform — Stage-66.0
Failure Domain Isolation & Containment Zoning Engine

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Implements deterministic failure domain zoning across governance stack.

This module:
- Groups governance engines into logical domains
- Detects clustered violations within a domain
- Detects cross-domain contamination risk
- Emits advisory isolation signals
- Never performs corrective action

Design Guarantees:
------------------
- Deterministic logic
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
from typing import Dict, Any, List


class FailureDomainIsolation:
    """
    Stage-66.0 Governance Domain Isolation Layer

    Domains:
    --------
    STABILITY_DOMAIN:
        Runtime Guardian (58)
        Entropy Engine (59)
        Convergence Monitor (62)

    STRUCTURAL_DOMAIN:
        Snapshot Sentinel (60)
        Evolution Gate (65)

    GOVERNANCE_DOMAIN:
        Causal Validator (61)
        Arbitration Layer (63)
        Telemetry Aggregator (64)
    """

    VERSION = "66.0"

    DOMAIN_THRESHOLD = 2
    CROSS_DOMAIN_THRESHOLD = 2

    def __init__(self):
        self._lock = threading.Lock()
        self._last_report = None
        self._domain_violation = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def evaluate(self, categorized_reports: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """
        Evaluate domain-based containment clustering.

        Parameters:
        -----------
        categorized_reports : dict
            {
                "stability": [...],
                "structural": [...],
                "governance": [...]
            }

        Returns:
        --------
        Domain isolation advisory report.
        """

        with self._lock:
            domain_scores = {
                domain: self._count_domain_violations(reports)
                for domain, reports in categorized_reports.items()
            }

            cross_domain_active = sum(
                1 for score in domain_scores.values()
                if score >= self.DOMAIN_THRESHOLD
            )

            containment_reason = self._evaluate_isolation(
                domain_scores,
                cross_domain_active
            )

            report = {
                "isolation_version": self.VERSION,
                "domain_scores": domain_scores,
                "cross_domain_clusters": cross_domain_active,
                "domain_violation": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._last_report = report
            self._domain_violation = containment_reason is not None

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _count_domain_violations(self, reports: List[Dict[str, Any]]) -> int:
        """
        Count violations within a domain.
        """
        count = 0
        for r in reports:
            if (
                r.get("containment_active")
                or r.get("integrity_violation")
                or r.get("equilibrium_violation")
                or r.get("saturation_detected")
                or r.get("meta_violation")
                or r.get("evolution_violation")
            ):
                count += 1
        return count

    def _evaluate_isolation(
        self,
        domain_scores: Dict[str, int],
        cross_domain_active: int
    ) -> str | None:
        """
        Determine isolation requirement.
        """

        for domain, score in domain_scores.items():
            if score >= self.DOMAIN_THRESHOLD:
                return f"{domain.upper()}_DOMAIN_CLUSTER_DETECTED"

        if cross_domain_active >= self.CROSS_DOMAIN_THRESHOLD:
            return "CROSS_DOMAIN_CONTAMINATION_RISK"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory-only recommended action.
        """

        if reason and "DOMAIN_CLUSTER" in reason:
            return "ISOLATE_AFFECTED_DOMAIN_AND_LIMIT_PROPAGATION"

        if reason == "CROSS_DOMAIN_CONTAMINATION_RISK":
            return "INITIATE_SYSTEM_WIDE_STABILITY_LOCKDOWN_REVIEW"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "isolation_version": self.VERSION,
            "domain_violation": self._domain_violation,
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_failure_domain_isolation() -> FailureDomainIsolation:
    """
    Backward compatible instantiation.
    """
    return FailureDomainIsolation()