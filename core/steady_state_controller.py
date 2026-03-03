"""
Jarvis Platform — Stage-70.0
Steady-State Certification & Adaptive Freeze Controller

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Detects sustained governance stability and certifies steady-state mode.
Prevents unnecessary adaptive churn when system is stable.

This module:
- Tracks resilience posture history
- Detects sustained OPTIMAL/STABLE conditions
- Certifies steady-state governance
- Emits advisory freeze/thaw signals
- Never executes corrective action

Design Guarantees:
------------------
- Deterministic logic
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
from collections import deque
from typing import Dict, Any


class SteadyStateController:
    """
    Stage-70.0 Governance Stability Certification Layer

    Steady-State Conditions:
    ------------------------
    - Sustained OPTIMAL or STABLE posture
    - No audit integrity violations
    - No domain violations
    """

    VERSION = "70.0"

    HISTORY_WINDOW = 15
    REQUIRED_STABLE_COUNT = 12

    def __init__(self):
        self._lock = threading.Lock()
        self._posture_history = deque(maxlen=self.HISTORY_WINDOW)
        self._steady_state_active = False
        self._last_report = None

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def evaluate(
        self,
        resilience_report: Dict[str, Any],
        audit_report: Dict[str, Any],
        isolation_report: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Evaluate steady-state eligibility.
        """

        with self._lock:
            posture = resilience_report.get("stability_posture", "UNKNOWN")
            self._posture_history.append(posture)

            stable_count = self._count_stable_states()

            eligibility = self._check_eligibility(
                stable_count,
                audit_report,
                isolation_report
            )

            advisory_action = self._recommended_action(eligibility)

            report = {
                "steady_state_version": self.VERSION,
                "history_depth": len(self._posture_history),
                "stable_count": stable_count,
                "steady_state_active": eligibility,
                "advisory_action": advisory_action
            }

            self._steady_state_active = eligibility
            self._last_report = report

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _count_stable_states(self) -> int:
        """
        Count OPTIMAL/STABLE postures in history.
        """
        return sum(
            1 for p in self._posture_history
            if p in ("OPTIMAL", "STABLE")
        )

    def _check_eligibility(
        self,
        stable_count: int,
        audit_report: Dict[str, Any],
        isolation_report: Dict[str, Any]
    ) -> bool:
        """
        Determine steady-state eligibility.
        """

        if stable_count < self.REQUIRED_STABLE_COUNT:
            return False

        if audit_report.get("integrity_violation"):
            return False

        if isolation_report.get("domain_violation"):
            return False

        return True

    def _recommended_action(self, steady: bool) -> str:
        """
        Advisory-only freeze/thaw signal.
        """

        if steady:
            return "CERTIFY_STEADY_STATE_AND_FREEZE_ADAPTIVE_ESCALATION"

        return "CONTINUE_ADAPTIVE_MONITORING"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "steady_state_version": self.VERSION,
            "steady_state_active": self._steady_state_active,
            "history_depth": len(self._posture_history),
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_steady_state_controller() -> SteadyStateController:
    """
    Backward compatible instantiation.
    """
    return SteadyStateController()