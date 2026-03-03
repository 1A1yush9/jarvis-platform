"""
Jarvis Platform — Stage-62.0
Strategic Convergence & Equilibrium Monitor

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Detects oscillatory advisory behavior, stabilization loops,
and failure to reach equilibrium across governance stack.

This module:
- Tracks advisory action history
- Detects flip-flop oscillations
- Detects non-converging stabilization cycles
- Emits advisory convergence alerts
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


class StrategicConvergenceMonitor:
    """
    Stage-62.0 Convergence Stability Guard

    Protects against:
    - Advisory oscillation loops
    - Repeated stabilization attempts without convergence
    - Governance equilibrium instability
    """

    VERSION = "62.0"

    HISTORY_WINDOW = 20
    OSCILLATION_THRESHOLD = 6
    NON_CONVERGENCE_THRESHOLD = 10

    def __init__(self):
        self._lock = threading.Lock()
        self._advisory_history = deque(maxlen=self.HISTORY_WINDOW)
        self._equilibrium_violation = False
        self._last_report = None

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def register_advisory(self, advisory_action: str) -> Dict[str, Any]:
        """
        Register advisory action from governance layer.

        Parameters:
        -----------
        advisory_action : str

        Returns:
        --------
        Convergence monitoring report.
        """

        with self._lock:
            self._advisory_history.append(advisory_action)

            oscillation_score = self._detect_oscillation()
            non_convergence_score = self._detect_non_convergence()

            containment_reason = self._evaluate_equilibrium(
                oscillation_score,
                non_convergence_score
            )

            report = {
                "monitor_version": self.VERSION,
                "history_depth": len(self._advisory_history),
                "oscillation_score": oscillation_score,
                "non_convergence_score": non_convergence_score,
                "equilibrium_violation": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._equilibrium_violation = containment_reason is not None
            self._last_report = report

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _detect_oscillation(self) -> int:
        """
        Detects flip-flop behavior in advisory history.
        """
        if len(self._advisory_history) < 2:
            return 0

        oscillations = 0
        for i in range(1, len(self._advisory_history)):
            if self._advisory_history[i] != self._advisory_history[i - 1]:
                oscillations += 1

        return oscillations

    def _detect_non_convergence(self) -> int:
        """
        Detects repeated non-PROCEED advisories.
        """
        return sum(
            1 for action in self._advisory_history
            if action != "PROCEED"
        )

    def _evaluate_equilibrium(
        self,
        oscillation_score: int,
        non_convergence_score: int
    ) -> str | None:
        """
        Determines if equilibrium violation exists.
        """

        if oscillation_score >= self.OSCILLATION_THRESHOLD:
            return "ADVISORY_OSCILLATION_DETECTED"

        if non_convergence_score >= self.NON_CONVERGENCE_THRESHOLD:
            return "STABILIZATION_NON_CONVERGENCE"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory-only recommended action.
        """

        if reason == "ADVISORY_OSCILLATION_DETECTED":
            return "INITIATE_STRATEGIC_CONSENSUS_REBALANCE"

        if reason == "STABILIZATION_NON_CONVERGENCE":
            return "TRIGGER_GOVERNANCE_REVIEW_CYCLE"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "monitor_version": self.VERSION,
            "equilibrium_violation": self._equilibrium_violation,
            "history_depth": len(self._advisory_history),
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_strategic_convergence_monitor() -> StrategicConvergenceMonitor:
    """
    Backward compatible instantiation.
    """
    return StrategicConvergenceMonitor()