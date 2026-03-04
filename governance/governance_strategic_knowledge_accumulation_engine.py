"""
Jarvis Platform
Stage-137.0 — Governance Strategic Knowledge Accumulation Engine

Purpose
-------
Accumulate evaluated governance strategy outcomes into a deterministic
strategic knowledge base used by higher-order governance intelligence
layers.

Key Guarantees
--------------
• Deterministic knowledge aggregation
• Read-only evaluation ingestion
• Append-only ledger reporting
• No execution authority
• No mutation authority
"""

import hashlib
import json
import time
from typing import Dict, Any, List


class GovernanceStrategicKnowledgeAccumulationEngine:

    MODULE = "governance_strategic_knowledge_accumulation_engine"
    STAGE = "137.0"

    def __init__(self, ledger):
        self.ledger = ledger

    # -----------------------------------------------------

    def _hash(self, payload: Dict[str, Any]) -> str:
        encoded = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    # -----------------------------------------------------

    def accumulate(
        self,
        strategy_evaluations: List[Dict[str, Any]]
    ) -> Dict[str, Any]:

        strategy_profiles: Dict[str, Dict[str, Any]] = {}

        for entry in strategy_evaluations:

            name = entry["strategy"]
            effectiveness = entry["effectiveness"]

            if name not in strategy_profiles:
                strategy_profiles[name] = {
                    "strategy": name,
                    "observations": 0,
                    "total_effectiveness": 0.0
                }

            strategy_profiles[name]["observations"] += 1
            strategy_profiles[name]["total_effectiveness"] += effectiveness

        for strategy in strategy_profiles.values():

            if strategy["observations"] > 0:
                strategy["average_effectiveness"] = round(
                    strategy["total_effectiveness"] / strategy["observations"],
                    6
                )
            else:
                strategy["average_effectiveness"] = 0.0

        knowledge_snapshot = {
            "module": self.MODULE,
            "stage": self.STAGE,
            "timestamp": int(time.time()),
            "strategy_profiles": list(strategy_profiles.values())
        }

        knowledge_snapshot["hash"] = self._hash(knowledge_snapshot)

        self.ledger.append(knowledge_snapshot)

        return knowledge_snapshot