"""
Jarvis Platform — Stage-75.0
Governance Quorum Validator & Consensus Integrity Engine

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Validates advisory consensus quorum across governance layers.

This module:
- Aggregates final advisory actions
- Computes consensus ratio
- Detects dominance or fragmentation
- Emits quorum integrity advisory signals
- Never executes corrective action

Design Guarantees:
------------------
- Deterministic consensus validation
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
from typing import Dict, Any, List


class GovernanceQuorumValidator:
    """
    Stage-75.0 Consensus Integrity Layer

    Protects against:
    - Single-layer dominance
    - Advisory fragmentation
    - False consensus assumptions
    """

    VERSION = "75.0"

    MIN_CONSENSUS_RATIO = 0.6
    DOMINANCE_THRESHOLD = 0.85

    def __init__(self):
        self._lock = threading.Lock()
        self._last_report = None
        self._quorum_violation = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def validate(self, advisory_actions: List[str]) -> Dict[str, Any]:
        """
        Validate governance quorum integrity.
        """

        with self._lock:
            if not advisory_actions:
                return self._neutral_report()

            action_counts = self._count_actions(advisory_actions)
            total = len(advisory_actions)

            dominant_action, dominant_ratio = self._compute_dominance(action_counts, total)
            consensus_ok = dominant_ratio >= self.MIN_CONSENSUS_RATIO

            containment_reason = self._evaluate_quorum(
                dominant_ratio,
                consensus_ok
            )

            report = {
                "quorum_validator_version": self.VERSION,
                "total_signals": total,
                "action_distribution": action_counts,
                "dominant_action": dominant_action,
                "dominant_ratio": round(dominant_ratio, 4),
                "quorum_violation": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._last_report = report
            self._quorum_violation = containment_reason is not None

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _count_actions(self, actions: List[str]) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for action in actions:
            counts[action] = counts.get(action, 0) + 1
        return counts

    def _compute_dominance(
        self,
        counts: Dict[str, int],
        total: int
    ) -> (str, float):

        dominant_action = max(counts, key=counts.get)
        dominant_ratio = counts[dominant_action] / total
        return dominant_action, dominant_ratio

    def _evaluate_quorum(
        self,
        dominant_ratio: float,
        consensus_ok: bool
    ) -> str | None:

        if not consensus_ok:
            return "INSUFFICIENT_CONSENSUS"

        if dominant_ratio >= self.DOMINANCE_THRESHOLD:
            return "SINGLE_LAYER_DOMINANCE_RISK"

        return None

    def _recommended_action(self, reason: str | None) -> str:

        if reason == "INSUFFICIENT_CONSENSUS":
            return "INITIATE_CONSENSUS_REBALANCING_REVIEW"

        if reason == "SINGLE_LAYER_DOMINANCE_RISK":
            return "VERIFY_MULTI_LAYER_VALIDATION"

        return "PROCEED"

    def _neutral_report(self) -> Dict[str, Any]:
        return {
            "quorum_validator_version": self.VERSION,
            "total_signals": 0,
            "action_distribution": {},
            "dominant_action": None,
            "dominant_ratio": 0.0,
            "quorum_violation": False,
            "containment_reason": None,
            "advisory_action": "PROCEED"
        }

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "quorum_validator_version": self.VERSION,
            "quorum_violation": self._quorum_violation,
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_governance_quorum_validator() -> GovernanceQuorumValidator:
    """
    Backward compatible instantiation.
    """
    return GovernanceQuorumValidator()