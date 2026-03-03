"""
Jarvis Platform — Stage-79.0
Deterministic Governance State Entropy Equalizer

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Detects advisory signal distribution imbalance over time
and identifies systemic entropy skew.

This module:
- Tracks advisory category distribution
- Computes normalized entropy score
- Detects imbalance bias
- Emits advisory-only entropy stabilization signals
- Never mutates system state

Design Guarantees:
------------------
- Deterministic entropy computation
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
import math
from collections import deque
from typing import Dict, Any


class GovernanceEntropyEqualizer:
    """
    Stage-79.0 Advisory Entropy Balancing Layer

    Protects against:
    - Long-term advisory dominance bias
    - Stabilization skew
    - Systemic signal imbalance
    """

    VERSION = "79.0"

    WINDOW_SIZE = 100
    ENTROPY_THRESHOLD = 0.4  # normalized entropy minimum

    def __init__(self):
        self._lock = threading.Lock()
        self._action_history = deque(maxlen=self.WINDOW_SIZE)
        self._entropy_violation = False
        self._last_report = None

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def register(self, advisory_action: str) -> Dict[str, Any]:
        """
        Register advisory action for entropy evaluation.
        """

        with self._lock:
            if advisory_action:
                self._action_history.append(advisory_action)

            entropy_score = self._compute_entropy()
            imbalance_detected = entropy_score < self.ENTROPY_THRESHOLD

            report = {
                "entropy_equalizer_version": self.VERSION,
                "window_size": len(self._action_history),
                "normalized_entropy": round(entropy_score, 4),
                "imbalance_detected": imbalance_detected,
                "advisory_action": self._recommended_action(imbalance_detected)
            }

            self._entropy_violation = imbalance_detected
            self._last_report = report

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _compute_entropy(self) -> float:
        """
        Compute normalized Shannon entropy.
        """
        if not self._action_history:
            return 1.0

        counts: Dict[str, int] = {}
        for action in self._action_history:
            counts[action] = counts.get(action, 0) + 1

        total = len(self._action_history)
        probabilities = [count / total for count in counts.values()]

        entropy = -sum(p * math.log(p, 2) for p in probabilities if p > 0)

        max_entropy = math.log(len(counts), 2) if len(counts) > 1 else 1
        normalized_entropy = entropy / max_entropy if max_entropy > 0 else 1.0

        return normalized_entropy

    def _recommended_action(self, imbalance: bool) -> str:
        if imbalance:
            return "REBALANCE_ADVISORY_SIGNAL_DISTRIBUTION"
        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "entropy_equalizer_version": self.VERSION,
            "window_size": len(self._action_history),
            "entropy_violation": self._entropy_violation,
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_governance_entropy_equalizer() -> GovernanceEntropyEqualizer:
    """
    Backward compatible instantiation.
    """
    return GovernanceEntropyEqualizer()