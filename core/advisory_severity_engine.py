"""
Jarvis Platform — Stage-73.0
Advisory Signal Severity Index & Priority Normalization Engine

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Normalizes advisory signals into deterministic severity index
to prevent escalation distortion.

This module:
- Consumes governance reports
- Assigns weighted severity scores
- Computes unified Advisory Severity Index (ASI)
- Classifies priority tier
- Never executes corrective action

Design Guarantees:
------------------
- Deterministic scoring
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
from typing import Dict, Any, List


class AdvisorySeverityEngine:
    """
    Stage-73.0 Severity Normalization Layer

    Severity Tiers:
    ---------------
    - LOW
    - MODERATE
    - HIGH
    - SEVERE
    - CRITICAL
    """

    VERSION = "73.0"

    def __init__(self):
        self._lock = threading.Lock()
        self._last_index = 0.0
        self._last_tier = "LOW"

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def evaluate(self, reports: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Compute Advisory Severity Index (ASI).
        """

        with self._lock:
            score = self._compute_score(reports)
            tier = self._classify_tier(score)
            advisory_action = self._recommended_action(tier)

            report = {
                "severity_engine_version": self.VERSION,
                "advisory_severity_index": round(score, 4),
                "severity_tier": tier,
                "advisory_action": advisory_action
            }

            self._last_index = score
            self._last_tier = tier

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _compute_score(self, reports: List[Dict[str, Any]]) -> float:
        """
        Deterministic weighted severity scoring.
        """

        total_weight = 0.0

        for r in reports:
            if r.get("integrity_violation"):
                total_weight += 0.4
            if r.get("domain_violation"):
                total_weight += 0.3
            if r.get("equilibrium_violation"):
                total_weight += 0.2
            if r.get("recovery_active"):
                total_weight += 0.2
            if r.get("chronic_instability_detected"):
                total_weight += 0.3
            if r.get("structural_violation"):
                total_weight += 0.4

        return min(1.0, total_weight)

    def _classify_tier(self, score: float) -> str:
        """
        Map score to severity tier.
        """

        if score >= 0.85:
            return "CRITICAL"
        if score >= 0.65:
            return "SEVERE"
        if score >= 0.45:
            return "HIGH"
        if score >= 0.25:
            return "MODERATE"
        return "LOW"

    def _recommended_action(self, tier: str) -> str:
        """
        Advisory-only priority guidance.
        """

        if tier == "CRITICAL":
            return "PRIORITIZE_IMMEDIATE_GOVERNANCE_ATTENTION"
        if tier == "SEVERE":
            return "ELEVATE_TO_EXECUTIVE_REVIEW_QUEUE"
        if tier == "HIGH":
            return "INCREASE_MONITORING_PRIORITY"
        if tier == "MODERATE":
            return "MAINTAIN_OBSERVATION"
        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "severity_engine_version": self.VERSION,
            "last_index": round(self._last_index, 4),
            "last_tier": self._last_tier
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_advisory_severity_engine() -> AdvisorySeverityEngine:
    """
    Backward compatible instantiation.
    """
    return AdvisorySeverityEngine()