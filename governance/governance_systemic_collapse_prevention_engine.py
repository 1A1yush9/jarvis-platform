"""
Jarvis Platform
Stage-130.0 — Governance Systemic Collapse Prevention Engine

Purpose
-------
Detect systemic governance collapse trajectories using combined
risk, trend, causal, and coherence signals.

This module emits deterministic containment advisories when
multi-layer instability indicates potential systemic failure.

Key Guarantees
--------------
• Deterministic evaluation
• Read-only telemetry consumption
• Append-only ledger reporting
• No execution authority
• No mutation authority
"""

import hashlib
import json
import time
from typing import Dict, Any


class GovernanceSystemicCollapsePreventionEngine:

    MODULE = "governance_systemic_collapse_prevention_engine"
    STAGE = "130.0"

    def __init__(self, ledger):
        self.ledger = ledger

    # ---------------------------------------------------------

    def _hash(self, payload: Dict[str, Any]) -> str:
        encoded = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    # ---------------------------------------------------------

    def _normalize(self, value: float) -> float:

        if value < 0:
            return 0.0

        if value > 1:
            return 1.0

        return round(value, 6)

    # ---------------------------------------------------------

    def evaluate(
        self,
        coherence_index: float,
        risk_score: float,
        projection_score: float,
        causal_root_count: int
    ) -> Dict[str, Any]:

        coherence_index = self._normalize(coherence_index)
        risk_score = self._normalize(risk_score)

        collapse_probability = 0.0

        # Combined systemic stress calculation
        collapse_probability += (1 - coherence_index) * 0.35
        collapse_probability += risk_score * 0.35

        if projection_score < 0:
            collapse_probability += abs(projection_score) * 0.2

        collapse_probability += min(causal_root_count / 10, 1) * 0.1

        collapse_probability = round(min(collapse_probability, 1), 6)

        advisory_level = "STABLE"

        if collapse_probability > 0.20:
            advisory_level = "WATCH"

        if collapse_probability > 0.40:
            advisory_level = "CONCERN"

        if collapse_probability > 0.60:
            advisory_level = "CRITICAL"

        if collapse_probability > 0.80:
            advisory_level = "SYSTEMIC_COLLAPSE_RISK"

        report = {
            "module": self.MODULE,
            "stage": self.STAGE,
            "timestamp": int(time.time()),
            "coherence_index": coherence_index,
            "risk_score": risk_score,
            "projection_score": projection_score,
            "causal_root_count": causal_root_count,
            "collapse_probability": collapse_probability,
            "advisory_level": advisory_level
        }

        report["hash"] = self._hash(report)

        self.ledger.append(report)

        return report