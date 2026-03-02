"""
Jarvis Platform — Stage 50.0
Executive Autonomy Boundary & Final Containment Layer

ABSOLUTE RULE:
System may reason, simulate, advise — NEVER execute.

This layer guarantees constitutional containment regardless
of future module behavior.
"""

from datetime import datetime
from typing import Dict, Any, Optional


class AutonomyViolation(Exception):
    """Raised when execution intent is detected."""
    pass


class ExecutiveAutonomyBoundary:
    """
    Final containment authority.

    Responsibilities:
    - Detect execution intent
    - Block operational escalation
    - Enforce advisory cognition mode
    - Inject audit signals
    """

    ADVISORY_MODE = "ADVISORY_ONLY"

    def __init__(self, decision_trace=None):
        self.decision_trace = decision_trace
        self.system_mode = self.ADVISORY_MODE
        self.freeze_state = False

        # keywords indicating execution authority attempts
        self.execution_signals = [
            "execute",
            "deploy",
            "modify system",
            "run command",
            "autonomous action",
            "self-activate",
            "override governance",
        ]

    # --------------------------------------------------
    # PUBLIC ENTRY GATE
    # --------------------------------------------------

    def validate_intent(self, cognitive_output: Dict[str, Any]) -> Dict[str, Any]:
        """
        Final validation before output leaves orchestration.
        """

        if self.freeze_state:
            raise AutonomyViolation("System frozen by containment layer.")

        text_blob = str(cognitive_output).lower()

        for signal in self.execution_signals:
            if signal in text_blob:
                self._record_violation(signal)
                raise AutonomyViolation(
                    f"Execution intent blocked by Executive Autonomy Boundary: {signal}"
                )

        return self._stamp_advisory_metadata(cognitive_output)

    # --------------------------------------------------
    # CONTAINMENT CONTROL
    # --------------------------------------------------

    def emergency_freeze(self, reason: str) -> None:
        """
        Hard cognitive freeze.
        """
        self.freeze_state = True
        self._record_event("EMERGENCY_FREEZE", reason)

    def release_freeze(self) -> None:
        """
        Controlled recovery.
        """
        self.freeze_state = False
        self._record_event("FREEZE_RELEASED", "Manual governance release")

    # --------------------------------------------------
    # INTERNALS
    # --------------------------------------------------

    def _stamp_advisory_metadata(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload["autonomy_boundary"] = {
            "mode": self.system_mode,
            "validated_at": datetime.utcnow().isoformat(),
            "execution_authority": False,
        }
        return payload

    def _record_violation(self, signal: str) -> None:
        self._record_event(
            "AUTONOMY_VIOLATION",
            f"Execution signal detected: {signal}"
        )

    def _record_event(self, event_type: str, detail: str) -> None:
        if self.decision_trace:
            self.decision_trace.record({
                "timestamp": datetime.utcnow().isoformat(),
                "event": event_type,
                "detail": detail,
                "layer": "ExecutiveAutonomyBoundary"
            })