"""
Jarvis Platform — Stage-59.0
Strategic Entropy & Drift Suppression Engine

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Detects long-horizon entropy accumulation and gradual strategic drift
that may evade short-cycle safeguards.

This module:
- Tracks directional deviation across reasoning cycles
- Detects entropy expansion in strategic state space
- Emits advisory stabilization signals
- Never executes corrective action directly

Design Guarantees:
------------------
- Deterministic output
- No mutation of external modules
- Backward compatible
- Thread-safe
"""

import threading
import hashlib
from collections import deque
from typing import Dict, Any


class StrategicEntropyEngine:
    """
    Stage-59.0 Long-Horizon Drift Suppression

    Protects against:
    - Gradual strategic misalignment
    - Entropy expansion across cycles
    - Long-term deviation from executive intent baseline
    """

    VERSION = "59.0"

    BASELINE_WINDOW = 50
    ENTROPY_THRESHOLD = 0.35
    DRIFT_VARIANCE_THRESHOLD = 0.40

    def __init__(self):
        self._lock = threading.Lock()
        self._state_history = deque(maxlen=self.BASELINE_WINDOW)
        self._baseline_signature = None
        self._entropy_score = 0.0
        self._drift_score = 0.0
        self._containment_active = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def register_state(self, strategic_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Register a new strategic state snapshot.

        Parameters:
        -----------
        strategic_state : dict
            Deterministic strategic representation.

        Returns:
        --------
        Advisory entropy & drift report.
        """

        with self._lock:
            signature = self._hash_state(strategic_state)

            if not self._baseline_signature:
                self._baseline_signature = signature

            self._state_history.append(signature)

            self._entropy_score = self._calculate_entropy()
            self._drift_score = self._calculate_drift(signature)

            containment_reason = self._evaluate_containment()

            report = {
                "engine_version": self.VERSION,
                "entropy_score": round(self._entropy_score, 4),
                "drift_score": round(self._drift_score, 4),
                "history_depth": len(self._state_history),
                "containment_active": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._containment_active = containment_reason is not None

            return report

    # ------------------------------------------------------------------
    # Internal Computation
    # ------------------------------------------------------------------

    def _hash_state(self, state: Dict[str, Any]) -> str:
        """
        Deterministic hash of strategic state.
        """
        serialized = str(sorted(state.items()))
        return hashlib.sha256(serialized.encode()).hexdigest()

    def _calculate_entropy(self) -> float:
        """
        Measures uniqueness ratio across history window.
        """
        if not self._state_history:
            return 0.0

        unique_states = len(set(self._state_history))
        total_states = len(self._state_history)

        return unique_states / total_states

    def _calculate_drift(self, current_signature: str) -> float:
        """
        Measures deviation from baseline.
        """
        if not self._baseline_signature:
            return 0.0

        difference = sum(
            1 for a, b in zip(current_signature, self._baseline_signature)
            if a != b
        )

        return difference / len(current_signature)

    def _evaluate_containment(self) -> str | None:
        """
        Determines if advisory containment is required.
        """

        if self._entropy_score > self.ENTROPY_THRESHOLD:
            return "STRATEGIC_ENTROPY_EXPANSION"

        if self._drift_score > self.DRIFT_VARIANCE_THRESHOLD:
            return "LONG_HORIZON_DRIFT_DETECTED"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory only.
        """

        if reason == "STRATEGIC_ENTROPY_EXPANSION":
            return "INITIATE_STRATEGIC_BASELINE_RECALIBRATION"

        if reason == "LONG_HORIZON_DRIFT_DETECTED":
            return "REINFORCE_EXECUTIVE_INTENT_ALIGNMENT"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Baseline Reset (Advisory Controlled)
    # ------------------------------------------------------------------

    def reset_baseline(self):
        """
        Advisory-controlled baseline reset.
        """
        with self._lock:
            if self._state_history:
                self._baseline_signature = self._state_history[-1]

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "engine_version": self.VERSION,
            "entropy_score": round(self._entropy_score, 4),
            "drift_score": round(self._drift_score, 4),
            "history_depth": len(self._state_history),
            "containment_active": self._containment_active,
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_strategic_entropy_engine() -> StrategicEntropyEngine:
    """
    Backward compatible instantiation.
    """
    return StrategicEntropyEngine()