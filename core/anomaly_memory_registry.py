"""
Jarvis Platform — Stage-71.0
Anomaly Memory Registry & Recurrence Intelligence Engine

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Maintains deterministic memory of instability signatures
and detects recurrence patterns across time.

This module:
- Registers anomaly signatures
- Tracks recurrence frequency
- Identifies chronic instability
- Emits advisory recurrence signals
- Never executes corrective action

Design Guarantees:
------------------
- Deterministic logic
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
import hashlib
from collections import deque
from typing import Dict, Any


class AnomalyMemoryRegistry:
    """
    Stage-71.0 Long-Horizon Recurrence Intelligence Layer

    Protects against:
    - Repeating governance instability cycles
    - Chronic structural anomalies
    """

    VERSION = "71.0"

    MEMORY_WINDOW = 100
    RECURRENCE_THRESHOLD = 5

    def __init__(self):
        self._lock = threading.Lock()
        self._memory = deque(maxlen=self.MEMORY_WINDOW)
        self._recurrence_map: Dict[str, int] = {}
        self._chronic_detected = False
        self._last_report = None

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def register(self, governance_snapshot: Dict[str, Any]) -> Dict[str, Any]:
        """
        Register governance snapshot for recurrence analysis.
        """

        with self._lock:
            signature = self._generate_signature(governance_snapshot)

            self._memory.append(signature)
            self._recurrence_map[signature] = self._recurrence_map.get(signature, 0) + 1

            recurrence_count = self._recurrence_map[signature]

            containment_reason = self._evaluate_recurrence(recurrence_count)

            report = {
                "anomaly_registry_version": self.VERSION,
                "signature": signature,
                "recurrence_count": recurrence_count,
                "memory_depth": len(self._memory),
                "chronic_instability_detected": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._chronic_detected = containment_reason is not None
            self._last_report = report

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _generate_signature(self, snapshot: Dict[str, Any]) -> str:
        """
        Deterministic fingerprint of governance snapshot.
        """
        serialized = str(sorted(snapshot.items()))
        return hashlib.sha256(serialized.encode()).hexdigest()

    def _evaluate_recurrence(self, count: int) -> str | None:
        """
        Determine chronic instability.
        """

        if count >= self.RECURRENCE_THRESHOLD:
            return "CHRONIC_INSTABILITY_PATTERN_DETECTED"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory-only recurrence response.
        """

        if reason == "CHRONIC_INSTABILITY_PATTERN_DETECTED":
            return "INITIATE_LONG_HORIZON_GOVERNANCE_REASSESSMENT"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "anomaly_registry_version": self.VERSION,
            "memory_depth": len(self._memory),
            "unique_signatures": len(self._recurrence_map),
            "chronic_instability_detected": self._chronic_detected,
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_anomaly_memory_registry() -> AnomalyMemoryRegistry:
    """
    Backward compatible instantiation.
    """
    return AnomalyMemoryRegistry()