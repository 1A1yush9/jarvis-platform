"""
Jarvis Platform
Stage-136.0 — Governance Meta-Strategy Evaluation Engine

Purpose
-------
Evaluate historical governance stabilization strategies to determine
their effectiveness over time.

This module compares governance metrics before and after advisory
strategy decisions to compute deterministic performance indicators.

Key Guarantees
--------------
• Deterministic evaluation
• Read-only historical analysis
• Append-only ledger reporting
• No execution authority
• No mutation authority
"""

import hashlib
import json
import time
from typing import Dict, Any, List


class GovernanceMetaStrategyEvaluationEngine:

    MODULE = "governance_meta_strategy_evaluation_engine"
    STAGE = "136.0"

    def __init__(self, ledger):
        self.ledger = ledger

    # -----------------------------------------------------

    def _hash(self, payload: Dict[str, Any]) -> str:
        encoded = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    # -----------------------------------------------------

    def _normalize(self, value: float) -> float:

        if value < 0:
            return 0.0

        if value > 1:
            return 1.0

        return round(value, 6)

    # -----------------------------------------------------

    def _calculate_effectiveness(self, before: float, after: float) -> float:
        """
        Deterministic improvement metric.
        """
        return round(after - before, 6)

    # -----------------------------------------------------

    def evaluate(
        self,
        evaluations: List[Dict[str, Any]]
    ) -> Dict[str, Any]:

        results = []

        for entry in evaluations:

            before_score = self._normalize(entry["before_fusion_score"])
            after_score = self._normalize(entry["after_fusion_score"])

            effectiveness = self._calculate_effectiveness(
                before_score,
                after_score
            )

            results.append({
                "strategy": entry["strategy"],
                "before_score": before_score,
                "after_score": after_score,
                "effectiveness": effectiveness
            })

        # Determine best historical strategy
        best_strategy = None

        if results:
            best_strategy = max(results, key=lambda x: x["effectiveness"])

        report = {
            "module": self.MODULE,
            "stage": self.STAGE,
            "timestamp": int(time.time()),
            "evaluated_strategies": results,
            "best_historical_strategy": best_strategy
        }

        report["hash"] = self._hash(report)

        self.ledger.append(report)

        return report