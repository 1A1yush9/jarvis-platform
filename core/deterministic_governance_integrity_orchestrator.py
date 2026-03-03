"""
Stage-90.0 — Deterministic Governance Integrity Orchestrator (DGIO)

Advisory-only cross-stage integrity synthesizer.
No execution authority.
No runtime mutation.
Deterministic integrity certification layer.
"""

import hashlib
import json
from typing import Dict, Any
from datetime import datetime


class DeterministicGovernanceIntegrityOrchestrator:
    """
    Deterministic Governance Integrity Orchestrator

    - Reconciles outputs from stages 80–89
    - Detects cross-layer contradictions
    - Computes global integrity score
    - Produces cryptographic integrity certificate
    """

    def __init__(self):
        pass

    # ------------------------------------------------------------------
    # Deterministic Hash Utility
    # ------------------------------------------------------------------

    def _hash_state(self, state: Dict[str, Any]) -> str:
        encoded = json.dumps(state, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    # ------------------------------------------------------------------
    # Integrity Evaluation
    # ------------------------------------------------------------------

    def evaluate_integrity(
        self,
        consensus_envelope: Dict[str, Any],
        stress_report: Dict[str, Any],
        recovery_report: Dict[str, Any],
        constraint_report: Dict[str, Any],
        stability_forecast: Dict[str, Any],
        attribution_report: Dict[str, Any]
    ) -> Dict[str, Any]:

        timestamp = datetime.utcnow().isoformat()

        checks = {}

        # Check 1: Consensus vs Stability Alignment
        consensus_level = consensus_envelope.get("consensus_level", "STABLE")
        stability_phase = stability_forecast.get("stability_phase", "STABLE")

        checks["consensus_stability_alignment"] = not (
            consensus_level == "CRITICAL" and stability_phase == "STABLE"
        )

        # Check 2: Constraint vs Recovery Coherence
        violation_detected = constraint_report.get("violation_detected", False)
        recovery_phase = recovery_report.get("recovery_phase", "STABLE_MONITORING")

        checks["constraint_recovery_coherence"] = not (
            violation_detected and recovery_phase == "STABLE_MONITORING"
        )

        # Check 3: Stress vs Attribution Alignment
        stressed_score = stress_report.get("stressed_score", 0.0)
        dominant_driver = attribution_report.get("dominant_driver", "")

        checks["stress_attribution_alignment"] = not (
            stressed_score > 0.7 and dominant_driver == ""
        )

        integrity_score = round(
            sum(1 for v in checks.values() if v) / len(checks),
            6
        )

        integrity_status = "CERTIFIED"
        if integrity_score < 0.66:
            integrity_status = "DEGRADED"
        if integrity_score < 0.33:
            integrity_status = "COMPROMISED"

        integrity_certificate = {
            "stage": "90.0",
            "timestamp": timestamp,
            "integrity_checks": checks,
            "integrity_score": integrity_score,
            "integrity_status": integrity_status,
            "advisory_mode": True,
            "execution_authority": False
        }

        integrity_certificate["integrity_seal"] = self._hash_state(integrity_certificate)

        return integrity_certificate