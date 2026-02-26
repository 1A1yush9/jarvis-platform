"""
Stage-30.5 — Executive Continuity Kernel (ECK)

Purpose:
Maintain long-term continuity of executive intelligence
across operational cycles.

Design:
- Advisory only
- Persistence-based identity tracking
- Backward compatible
"""

from typing import Dict, Any, List
import json
import os
from datetime import datetime


class ExecutiveContinuityKernel:
    def __init__(self, continuity_file: str = "executive_continuity.json"):
        self.continuity_file = continuity_file
        self.max_records = 300
        self.version = "30.5"
        self._ensure_storage()

    # --------------------------------------------------
    # Storage Management
    # --------------------------------------------------
    def _ensure_storage(self):
        if not os.path.exists(self.continuity_file):
            with open(self.continuity_file, "w") as f:
                json.dump([], f)

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.continuity_file, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self, data: List[Dict[str, Any]]):
        with open(self.continuity_file, "w") as f:
            json.dump(data[-self.max_records:], f, indent=2)

    # --------------------------------------------------
    # Continuity Update
    # --------------------------------------------------
    def update_continuity(
        self,
        executive_intelligence: Dict[str, Any]
    ) -> Dict[str, Any]:

        history = self._load()

        intelligence_score = executive_intelligence.get(
            "executive_intelligence_score", 0.5
        )

        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "intelligence_score": intelligence_score,
        }

        history.append(snapshot)
        self._save(history)

        continuity_index = self._calculate_continuity(history)

        return {
            "continuity_records": len(history),
            "continuity_index": continuity_index,
            "continuity_state": self._state(continuity_index),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Continuity Calculation
    # --------------------------------------------------
    def _calculate_continuity(self, history: List[Dict[str, Any]]) -> float:

        if len(history) < 10:
            return 0.5

        recent = history[-10:]
        scores = [x["intelligence_score"] for x in recent]

        mean = sum(scores) / len(scores)
        drift = max(scores) - min(scores)

        continuity = 1 - drift
        continuity = max(0.0, min(1.0, continuity))

        return round(continuity, 3)

    def _state(self, continuity: float) -> str:
        if continuity >= 0.85:
            return "STRONG_CONTINUITY"
        elif continuity >= 0.65:
            return "STABLE_IDENTITY"
        elif continuity >= 0.45:
            return "ADAPTING_IDENTITY"
        return "IDENTITY_DRIFT"