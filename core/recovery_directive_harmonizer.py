"""
Jarvis Platform — Stage-67.0
Coordinated Recovery Orchestration & Directive Harmonizer

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Harmonizes recovery directives emitted by governance layers
into a single deterministic advisory output.

This module:
- Collects advisory actions
- Categorizes recovery intent
- Prevents directive conflicts
- Emits one unified recovery directive
- Never executes corrective action

Design Guarantees:
------------------
- Deterministic logic
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
from typing import Dict, Any, List


class RecoveryDirectiveHarmonizer:
    """
    Stage-67.0 Recovery Coordination Layer

    Recovery Categories:
    --------------------
    - CALM_STATE
    - GOVERNANCE_REVIEW
    - ALIGNMENT_REINFORCEMENT
    - STABILITY_LOCKDOWN
    - VERSION_REALIGNMENT
    """

    VERSION = "67.0"

    def __init__(self):
        self._lock = threading.Lock()
        self._last_report = None
        self._recovery_active = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def harmonize(self, reports: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Harmonize advisory recovery actions.

        Parameters:
        -----------
        reports : list of governance reports

        Returns:
        --------
        Unified recovery directive report.
        """

        with self._lock:
            actions = [
                r.get("advisory_action")
                for r in reports
                if r.get("advisory_action") and r.get("advisory_action") != "PROCEED"
            ]

            categorized = self._categorize_actions(actions)
            unified_directive = self._resolve_directive(categorized)

            report = {
                "harmonizer_version": self.VERSION,
                "detected_actions": actions,
                "categorized_actions": categorized,
                "recovery_active": unified_directive is not None,
                "containment_reason": "RECOVERY_COORDINATION_REQUIRED" if unified_directive else None,
                "advisory_action": unified_directive if unified_directive else "PROCEED"
            }

            self._last_report = report
            self._recovery_active = unified_directive is not None

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _categorize_actions(self, actions: List[str]) -> Dict[str, int]:
        """
        Normalize actions into recovery categories.
        """
        categories = {
            "CALM_STATE": 0,
            "GOVERNANCE_REVIEW": 0,
            "ALIGNMENT_REINFORCEMENT": 0,
            "STABILITY_LOCKDOWN": 0,
            "VERSION_REALIGNMENT": 0
        }

        for action in actions:
            if not action:
                continue

            if "CALM" in action:
                categories["CALM_STATE"] += 1
            elif "REVIEW" in action:
                categories["GOVERNANCE_REVIEW"] += 1
            elif "ALIGN" in action:
                categories["ALIGNMENT_REINFORCEMENT"] += 1
            elif "LOCKDOWN" in action:
                categories["STABILITY_LOCKDOWN"] += 1
            elif "VERSION" in action or "ALIGNMENT" in action:
                categories["VERSION_REALIGNMENT"] += 1
            else:
                categories["GOVERNANCE_REVIEW"] += 1

        return categories

    def _resolve_directive(self, categorized: Dict[str, int]) -> str | None:
        """
        Resolve highest-priority recovery directive.
        Priority order is deterministic.
        """

        if categorized["STABILITY_LOCKDOWN"] > 0:
            return "EXECUTE_STABILITY_LOCKDOWN_REVIEW"

        if categorized["CALM_STATE"] > 0:
            return "INITIATE_CALM_STATE_PROTOCOL"

        if categorized["VERSION_REALIGNMENT"] > 0:
            return "PERFORM_VERSION_REALIGNMENT_AUDIT"

        if categorized["ALIGNMENT_REINFORCEMENT"] > 0:
            return "REINFORCE_EXECUTIVE_ALIGNMENT"

        if categorized["GOVERNANCE_REVIEW"] > 0:
            return "INITIATE_COMPREHENSIVE_GOVERNANCE_REVIEW"

        return None

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "harmonizer_version": self.VERSION,
            "recovery_active": self._recovery_active,
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_recovery_directive_harmonizer() -> RecoveryDirectiveHarmonizer:
    """
    Backward compatible instantiation.
    """
    return RecoveryDirectiveHarmonizer()