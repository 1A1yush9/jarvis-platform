"""
Jarvis Platform — Stage-69.0
Systemic Resilience Index & Adaptive Stability Posture Engine

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Computes unified Systemic Resilience Index (SRI) from governance stack
and classifies global stability posture.

This module:
- Aggregates governance meta-health signals
- Computes deterministic resilience score
- Classifies stability posture
- Emits advisory posture guidance
- Never executes corrective action

Design Guarantees:
------------------
- Deterministic scoring
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
from typing import Dict, Any


class SystemicResilienceEngine:
    """
    Stage-69.0 Global Stability Posture Layer

    Resilience Tiers:
    -----------------
    - OPTIMAL
    - STABLE
    - ELEVATED_RISK
    - HIGH_RISK
    - CRITICAL
    """

    VERSION = "69.0"

    def __init__(self):
        self._lock = threading.Lock()
        self._last_index = 1.0
        self._last_posture = "OPTIMAL"

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def evaluate(
        self,
        telemetry_report: Dict[str, Any],
        isolation_report: Dict[str, Any],
        recovery_report: Dict[str, Any],
        audit_report: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Evaluate systemic resilience posture.

        Returns:
        --------
        Resilience evaluation report.
        """

        with self._lock:
            sri = self._compute_resilience_index(
                telemetry_report,
                isolation_report,
                recovery_report,
                audit_report
            )

            posture = self._classify_posture(sri)
            advisory_action = self._recommended_action(posture)

            report = {
                "resilience_version": self.VERSION,
                "systemic_resilience_index": round(sri, 4),
                "stability_posture": posture,
                "advisory_action": advisory_action
            }

            self._last_index = sri
            self._last_posture = posture

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _compute_resilience_index(
        self,
        telemetry: Dict[str, Any],
        isolation: Dict[str, Any],
        recovery: Dict[str, Any],
        audit: Dict[str, Any]
    ) -> float:
        """
        Deterministic weighted scoring.
        """

        base_score = telemetry.get("stability_index", 1.0)

        isolation_penalty = 0.2 if isolation.get("domain_violation") else 0.0
        recovery_penalty = 0.2 if recovery.get("recovery_active") else 0.0
        audit_penalty = 0.4 if audit.get("integrity_violation") else 0.0

        sri = base_score - isolation_penalty - recovery_penalty - audit_penalty

        return max(0.0, min(1.0, sri))

    def _classify_posture(self, sri: float) -> str:
        """
        Classify resilience posture.
        """

        if sri >= 0.9:
            return "OPTIMAL"
        if sri >= 0.75:
            return "STABLE"
        if sri >= 0.55:
            return "ELEVATED_RISK"
        if sri >= 0.35:
            return "HIGH_RISK"
        return "CRITICAL"

    def _recommended_action(self, posture: str) -> str:
        """
        Advisory-only posture guidance.
        """

        if posture == "OPTIMAL":
            return "PROCEED"

        if posture == "STABLE":
            return "MAINTAIN_MONITORING"

        if posture == "ELEVATED_RISK":
            return "INCREASE_STABILITY_SURVEILLANCE"

        if posture == "HIGH_RISK":
            return "INITIATE_STRUCTURED_GOVERNANCE_REVIEW"

        if posture == "CRITICAL":
            return "INITIATE_SYSTEM_WIDE_RESILIENCE_REASSESSMENT"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "resilience_version": self.VERSION,
            "last_index": round(self._last_index, 4),
            "last_posture": self._last_posture
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_systemic_resilience_engine() -> SystemicResilienceEngine:
    """
    Backward compatible instantiation.
    """
    return SystemicResilienceEngine()