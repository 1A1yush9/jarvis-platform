"""
Jarvis Platform
Stage-133.0 — Governance Global Intelligence State Engine

Purpose
-------
Transforms fused governance telemetry signals into a deterministic
global governance intelligence state.

Defines a controlled governance state machine used by higher layers
for advisory diagnostics.

Key Guarantees
--------------
• Deterministic state transitions
• Read-only telemetry ingestion
• Append-only ledger reporting
• No execution authority
• No mutation authority
"""

import hashlib
import json
import time
from typing import Dict, Any


class GovernanceGlobalIntelligenceStateEngine:

    MODULE = "governance_global_intelligence_state_engine"
    STAGE = "133.0"

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

    def _determine_state(self, fusion_score: float) -> str:

        if fusion_score >= 0.90:
            return "STABLE"

        if fusion_score >= 0.75:
            return "WATCH"

        if fusion_score >= 0.60:
            return "DEGRADED"

        if fusion_score >= 0.40:
            return "CRITICAL"

        return "SYSTEMIC_RISK"

    # ---------------------------------------------------------

    def evaluate(self, fusion_score: float) -> Dict[str, Any]:

        fusion_score = self._normalize(fusion_score)

        state = self._determine_state(fusion_score)

        report = {
            "module": self.MODULE,
            "stage": self.STAGE,
            "timestamp": int(time.time()),
            "fusion_score": fusion_score,
            "global_governance_state": state
        }

        report["hash"] = self._hash(report)

        self.ledger.append(report)

        return report