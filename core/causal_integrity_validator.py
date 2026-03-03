"""
Jarvis Platform — Stage-61.0
Cross-Layer Consistency & Causal Integrity Validator

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Detects cross-layer advisory contradictions or causal misalignment
across governance and stability stack components.

This module:
- Validates advisory coherence across layers
- Detects containment disagreement
- Identifies conflicting stabilization signals
- Emits advisory integrity alerts
- Never performs corrective execution

Design Guarantees:
------------------
- Deterministic logic
- Thread-safe
- No mutation of external systems
- Fully backward compatible
"""

import threading
from typing import Dict, Any, List


class CausalIntegrityValidator:
    """
    Stage-61.0 Cross-Layer Consistency Guard

    Protects against:
    - Advisory signal contradictions
    - Governance layer desynchronization
    - Causal instability between modules
    """

    VERSION = "61.0"

    CONFLICT_THRESHOLD = 2  # number of conflicting advisories required

    def __init__(self):
        self._lock = threading.Lock()
        self._last_validation = None
        self._integrity_violation = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def validate(self, advisory_reports: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Validates coherence across multiple advisory engine reports.

        Parameters:
        -----------
        advisory_reports : list of dict
            Reports from Stage-52 through Stage-60 engines.

        Returns:
        --------
        Advisory integrity validation report.
        """

        with self._lock:
            containment_flags = [
                r.get("containment_active") or r.get("integrity_violation")
                for r in advisory_reports
            ]

            advisory_actions = [
                r.get("advisory_action")
                for r in advisory_reports
                if r.get("advisory_action") is not None
            ]

            conflict_score = self._detect_conflicts(advisory_actions)

            containment_disagreement = self._detect_containment_disagreement(containment_flags)

            containment_reason = self._evaluate_integrity(
                conflict_score,
                containment_disagreement
            )

            report = {
                "validator_version": self.VERSION,
                "conflict_score": conflict_score,
                "containment_disagreement": containment_disagreement,
                "integrity_violation": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._last_validation = report
            self._integrity_violation = containment_reason is not None

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _detect_conflicts(self, actions: List[str]) -> int:
        """
        Detects contradictory advisory actions.
        """
        unique_actions = set(actions)

        if "PROCEED" in unique_actions and len(unique_actions) > 1:
            return len(unique_actions)

        return 0

    def _detect_containment_disagreement(self, flags: List[bool]) -> bool:
        """
        Detects disagreement between engines on containment necessity.
        """
        return any(flags) and not all(flags)

    def _evaluate_integrity(self, conflict_score: int, disagreement: bool) -> str | None:
        """
        Determines if cross-layer integrity violation exists.
        """

        if conflict_score >= self.CONFLICT_THRESHOLD:
            return "ADVISORY_ACTION_CONFLICT"

        if disagreement:
            return "CONTAINMENT_STATE_DESYNCHRONIZATION"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory-only recommended action.
        """

        if reason == "ADVISORY_ACTION_CONFLICT":
            return "INITIATE_GOVERNANCE_RECONCILIATION_PROTOCOL"

        if reason == "CONTAINMENT_STATE_DESYNCHRONIZATION":
            return "SYNCHRONIZE_STABILITY_ENGINES"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "validator_version": self.VERSION,
            "integrity_violation": self._integrity_violation,
            "last_validation": self._last_validation
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_causal_integrity_validator() -> CausalIntegrityValidator:
    """
    Backward compatible instantiation.
    """
    return CausalIntegrityValidator()