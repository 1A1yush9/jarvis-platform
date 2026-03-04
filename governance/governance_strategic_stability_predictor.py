"""
Jarvis Platform
Stage-128.0 — Governance Strategic Stability Predictor

Purpose
-------
Forecast future governance stability by analyzing deterministic
trends across historical telemetry signals.

This module evaluates whether governance stability is improving,
stable, or degrading.

Key Guarantees
--------------
• Deterministic forecasting
• Read-only telemetry consumption
• Append-only ledger reporting
• No execution authority
• No mutation authority
"""

import hashlib
import json
import time
from typing import Dict, Any, List


class GovernanceStrategicStabilityPredictor:

    MODULE = "governance_strategic_stability_predictor"
    STAGE = "128.0"

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

    def _compute_trend(self, history: List[float]) -> float:
        """
        Deterministic linear trend approximation.
        Positive = improving stability
        Negative = degrading stability
        """

        if len(history) < 2:
            return 0.0

        first = history[0]
        last = history[-1]

        return round((last - first) / len(history), 6)

    # ---------------------------------------------------------

    def forecast(self, telemetry_history: Dict[str, List[float]]) -> Dict[str, Any]:

        normalized_history: Dict[str, List[float]] = {}

        for module, values in telemetry_history.items():
            normalized_history[module] = [self._normalize(v) for v in values]

        trends = {}

        for module, values in normalized_history.items():
            trends[module] = self._compute_trend(values)

        if trends:
            stability_projection = round(sum(trends.values()) / len(trends), 6)
        else:
            stability_projection = 0.0

        verdict = "STABLE"

        if stability_projection < -0.02:
            verdict = "DEGRADING"

        if stability_projection < -0.05:
            verdict = "CRITICAL_DECLINE"

        if stability_projection > 0.02:
            verdict = "IMPROVING"

        report = {
            "module": self.MODULE,
            "stage": self.STAGE,
            "timestamp": int(time.time()),
            "trend_vectors": trends,
            "projection_score": stability_projection,
            "verdict": verdict
        }

        report["hash"] = self._hash(report)

        self.ledger.append(report)

        return report