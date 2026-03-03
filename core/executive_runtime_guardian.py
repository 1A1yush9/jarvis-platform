"""
Jarvis Platform — Stage-58.0
Executive Runtime Guardian (Hot-Loop & Recursive Safety Shield)

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Prevents runaway cognitive recursion, hot-loop amplification,
or unstable meta-coordination feedback cycles.

This module DOES NOT block execution.
It emits advisory containment signals only.

Design Guarantees:
------------------
- Deterministic behavior
- No mutation of external systems
- Backward compatible
- Zero side-effects outside advisory signal return
"""

import time
import threading
from collections import deque
from typing import Dict, Any


class ExecutiveRuntimeGuardian:
    """
    Stage-58.0 Runtime Safety Shield

    Protects system from:
    - Recursive escalation loops
    - Meta-coordination hot cycles
    - Temporal burst overload
    - Self-referential runaway reasoning
    """

    VERSION = "58.0"
    MAX_RECURSION_DEPTH = 25
    MAX_EVENTS_PER_WINDOW = 120
    WINDOW_SECONDS = 5
    MAX_IDENTICAL_SIGNAL_CHAIN = 12

    def __init__(self):
        self._lock = threading.Lock()

        self._recursion_depth = 0
        self._event_window = deque()
        self._signal_chain = deque(maxlen=self.MAX_IDENTICAL_SIGNAL_CHAIN)

        self._last_signal_signature = None
        self._containment_active = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def register_cycle(self, signal_signature: str) -> Dict[str, Any]:
        """
        Registers a reasoning cycle.

        Parameters:
        -----------
        signal_signature : str
            Deterministic hash / signature of reasoning state.

        Returns:
        --------
        Advisory containment report.
        """

        with self._lock:
            current_time = time.time()

            self._track_event(current_time)
            self._track_recursion()
            self._track_signal_chain(signal_signature)

            containment_reason = self._evaluate_containment()

            report = {
                "guardian_version": self.VERSION,
                "recursion_depth": self._recursion_depth,
                "events_in_window": len(self._event_window),
                "signal_chain_length": len(self._signal_chain),
                "containment_active": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            if containment_reason:
                self._containment_active = True
            else:
                self._containment_active = False

            return report

    def reset_cycle_depth(self):
        """
        Should be called by orchestrator
        after successful reasoning completion.
        """
        with self._lock:
            self._recursion_depth = 0
            self._signal_chain.clear()

    # ------------------------------------------------------------------
    # Internal Tracking
    # ------------------------------------------------------------------

    def _track_recursion(self):
        self._recursion_depth += 1

    def _track_event(self, current_time: float):
        self._event_window.append(current_time)

        # Remove stale events
        while self._event_window and (
            current_time - self._event_window[0] > self.WINDOW_SECONDS
        ):
            self._event_window.popleft()

    def _track_signal_chain(self, signal_signature: str):
        if signal_signature == self._last_signal_signature:
            self._signal_chain.append(signal_signature)
        else:
            self._signal_chain.clear()
            self._signal_chain.append(signal_signature)

        self._last_signal_signature = signal_signature

    # ------------------------------------------------------------------
    # Containment Logic
    # ------------------------------------------------------------------

    def _evaluate_containment(self) -> str | None:
        """
        Returns containment reason if unstable.
        """

        if self._recursion_depth > self.MAX_RECURSION_DEPTH:
            return "RECURSION_DEPTH_EXCEEDED"

        if len(self._event_window) > self.MAX_EVENTS_PER_WINDOW:
            return "TEMPORAL_BURST_OVERLOAD"

        if len(self._signal_chain) >= self.MAX_IDENTICAL_SIGNAL_CHAIN:
            return "RECURSIVE_SIGNAL_LOOP_DETECTED"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory-only suggested action.
        """

        if reason == "RECURSION_DEPTH_EXCEEDED":
            return "HALT_META_COORDINATION_AND_RESET_DEPTH"

        if reason == "TEMPORAL_BURST_OVERLOAD":
            return "THROTTLE_REASONING_CYCLE"

        if reason == "RECURSIVE_SIGNAL_LOOP_DETECTED":
            return "FORCE_CONTEXTUAL_DIVERGENCE"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Status Interface
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        """
        Returns guardian runtime health snapshot.
        """

        return {
            "guardian_version": self.VERSION,
            "recursion_depth": self._recursion_depth,
            "events_in_window": len(self._event_window),
            "signal_chain_length": len(self._signal_chain),
            "containment_active": self._containment_active,
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_runtime_guardian() -> ExecutiveRuntimeGuardian:
    """
    Backward compatible instantiation layer.
    """
    return ExecutiveRuntimeGuardian()