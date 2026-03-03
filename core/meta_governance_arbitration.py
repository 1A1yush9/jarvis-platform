"""
Jarvis Platform — Stage-63.0
Meta-Governance Continuity & Failsafe Arbitration Layer

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Provides final arbitration across governance stack to prevent
containment cascade amplification and governance saturation.

This module:
- Monitors number of simultaneous violations
- Detects escalation chains
- Prevents advisory amplification storms
- Emits calm-state restoration advisory
- Never executes corrective action

Design Guarantees:
------------------
- Deterministic behavior
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
from typing import Dict, Any, List


class MetaGovernanceArbitration:
    """
    Stage-63.0 Governance Failsafe Arbitration

    Protects against:
    - Multi-engine containment cascade
    - Governance saturation
    - Escalation amplification loops
    """

    VERSION = "63.0"

    SATURATION_THRESHOLD = 4
    ESCALATION_THRESHOLD = 3

    def __init__(self):
        self._lock = threading.Lock()
        self._last_report = None
        self._saturation_detected = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def arbitrate(self, governance_reports: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Perform arbitration across governance layer reports.

        Parameters:
        -----------
        governance_reports : list of dict
            Reports from all active governance engines.

        Returns:
        --------
        Arbitration advisory report.
        """

        with self._lock:
            violation_count = self._count_violations(governance_reports)
            escalation_chain = self._detect_escalation(governance_reports)

            containment_reason = self._evaluate_arbitration(
                violation_count,
                escalation_chain
            )

            report = {
                "arbitration_version": self.VERSION,
                "violation_count": violation_count,
                "escalation_chain_detected": escalation_chain,
                "saturation_detected": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._saturation_detected = containment_reason is not None
            self._last_report = report

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _count_violations(self, reports: List[Dict[str, Any]]) -> int:
        """
        Counts active violations across engines.
        """
        count = 0
        for r in reports:
            if r.get("containment_active") or \
               r.get("integrity_violation") or \
               r.get("equilibrium_violation"):
                count += 1
        return count

    def _detect_escalation(self, reports: List[Dict[str, Any]]) -> bool:
        """
        Detects escalating advisory actions (non-PROCEED stacking).
        """
        escalation_count = 0

        for r in reports:
            action = r.get("advisory_action")
            if action and action != "PROCEED":
                escalation_count += 1

        return escalation_count >= self.ESCALATION_THRESHOLD

    def _evaluate_arbitration(
        self,
        violation_count: int,
        escalation_chain: bool
    ) -> str | None:
        """
        Determines if meta-governance arbitration required.
        """

        if violation_count >= self.SATURATION_THRESHOLD:
            return "GOVERNANCE_SATURATION_DETECTED"

        if escalation_chain:
            return "ESCALATION_CHAIN_DETECTED"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory-only recommendation.
        """

        if reason == "GOVERNANCE_SATURATION_DETECTED":
            return "INITIATE_CALM_STATE_RESTORATION_PROTOCOL"

        if reason == "ESCALATION_CHAIN_DETECTED":
            return "TRIGGER_META_GOVERNANCE_REVIEW"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "arbitration_version": self.VERSION,
            "saturation_detected": self._saturation_detected,
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_meta_governance_arbitration() -> MetaGovernanceArbitration:
    """
    Backward compatible instantiation.
    """
    return MetaGovernanceArbitration()