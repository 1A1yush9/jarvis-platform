"""
Jarvis Platform — Stage-60.0
Constitutional State Snapshot & Rollback Sentinel

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Provides deterministic state fingerprinting and advisory rollback signaling.
Ensures architectural continuity and constitutional invariance.

This module:
- Captures governance-safe state snapshots
- Detects structural mutation or drift
- Emits advisory rollback signals
- Never performs rollback directly

Design Guarantees:
------------------
- Deterministic behavior
- Thread-safe
- No external side-effects
- Backward compatible
"""

import hashlib
import threading
from typing import Dict, Any


class ConstitutionalSnapshotSentinel:
    """
    Stage-60.0 Structural Integrity Guard

    Protects against:
    - Unauthorized architectural mutation
    - Cross-module instability propagation
    - Governance stack corruption
    """

    VERSION = "60.0"

    def __init__(self):
        self._lock = threading.Lock()
        self._baseline_snapshot = None
        self._last_snapshot = None
        self._integrity_violation = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def register_system_state(self, system_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registers a full governance-safe system state snapshot.

        Parameters:
        -----------
        system_state : dict
            Deterministic architectural representation.

        Returns:
        --------
        Advisory integrity report.
        """

        with self._lock:
            snapshot_hash = self._hash_state(system_state)
            self._last_snapshot = snapshot_hash

            if self._baseline_snapshot is None:
                self._baseline_snapshot = snapshot_hash

            integrity_delta = self._compare_snapshots(snapshot_hash)
            containment_reason = self._evaluate_integrity(integrity_delta)

            report = {
                "sentinel_version": self.VERSION,
                "baseline_hash": self._baseline_snapshot,
                "current_hash": snapshot_hash,
                "integrity_delta": integrity_delta,
                "integrity_violation": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._integrity_violation = containment_reason is not None

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _hash_state(self, state: Dict[str, Any]) -> str:
        """
        Deterministic hashing of system state.
        """
        serialized = str(sorted(state.items()))
        return hashlib.sha256(serialized.encode()).hexdigest()

    def _compare_snapshots(self, current_hash: str) -> float:
        """
        Computes normalized difference from baseline.
        """
        if not self._baseline_snapshot:
            return 0.0

        difference = sum(
            1 for a, b in zip(current_hash, self._baseline_snapshot)
            if a != b
        )

        return difference / len(current_hash)

    def _evaluate_integrity(self, delta: float) -> str | None:
        """
        Determines if advisory rollback is needed.
        """

        # Conservative structural mutation threshold
        if delta > 0.45:
            return "CONSTITUTIONAL_STRUCTURE_DEVIATION"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory-only recommended action.
        """

        if reason == "CONSTITUTIONAL_STRUCTURE_DEVIATION":
            return "RECOMMEND_ROLLBACK_TO_BASELINE_SNAPSHOT"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Controlled Baseline Update
    # ------------------------------------------------------------------

    def update_baseline(self):
        """
        Advisory-controlled baseline refresh.
        """
        with self._lock:
            if self._last_snapshot:
                self._baseline_snapshot = self._last_snapshot
                self._integrity_violation = False

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "sentinel_version": self.VERSION,
            "baseline_snapshot": self._baseline_snapshot,
            "last_snapshot": self._last_snapshot,
            "integrity_violation": self._integrity_violation
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_constitutional_snapshot_sentinel() -> ConstitutionalSnapshotSentinel:
    """
    Backward compatible instantiation.
    """
    return ConstitutionalSnapshotSentinel()