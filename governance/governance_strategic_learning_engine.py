"""
Jarvis Platform
Stage-138.0 — Governance Strategic Learning Engine

Purpose
-------
Derive deterministic governance strategy intelligence from accumulated
historical strategy performance.

This module analyzes strategy effectiveness profiles and produces a
learned strategy preference ranking.

Key Guarantees
--------------
• Deterministic learning computation
• Read-only knowledge ingestion
• Append-only ledger reporting
• No execution authority
• No mutation authority
"""

import hashlib
import json
import time
from typing import Dict, Any, List


class GovernanceStrategicLearningEngine:

    MODULE = "governance_strategic_learning_engine"
    STAGE = "138.0"

    def __init__(self, ledger):
        self.ledger = ledger

    # -----------------------------------------------------

    def _hash(self, payload: Dict[str, Any]) -> str:
        encoded = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    # -----------------------------------------------------

    def _score_strategy(self, avg_effectiveness: float, observations: int) -> float:
        """
        Deterministic strategy confidence score.
        """
        confidence_weight = min(observations / 10, 1)
        score = avg_effectiveness * confidence_weight
        return round(score, 6)

    # -----------------------------------------------------

    def learn(
        self,
        strategy_profiles: List[Dict[str, Any]]
    ) -> Dict[str, Any]:

        learned_profiles = []

        for strategy in strategy_profiles:

            avg_effectiveness = strategy.get("average_effectiveness", 0.0)
            observations = strategy.get("observations", 0)

            score = self._score_strategy(avg_effectiveness, observations)

            learned_profiles.append({
                "strategy": strategy["strategy"],
                "observations": observations,
                "average_effectiveness": avg_effectiveness,
                "learned_score": score
            })

        learned_profiles.sort(
            key=lambda x: x["learned_score"],
            reverse=True
        )

        best_strategy = learned_profiles[0] if learned_profiles else None

        learning_report = {
            "module": self.MODULE,
            "stage": self.STAGE,
            "timestamp": int(time.time()),
            "learned_strategy_profiles": learned_profiles,
            "recommended_learned_strategy": best_strategy
        }

        learning_report["hash"] = self._hash(learning_report)

        self.ledger.append(learning_report)

        return learning_report