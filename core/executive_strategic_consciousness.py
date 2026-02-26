"""
Stage-31.0 — Executive Strategic Consciousness Layer (ESCL)

Purpose:
Maintain a persistent strategic worldview derived
from long-term executive intelligence evolution.

Design:
- Advisory only
- Historical aggregation
- Backward compatible
"""

from typing import Dict, Any, List
import json
import os
from datetime import datetime


class ExecutiveStrategicConsciousness:
    def __init__(self, consciousness_file: str = "strategic_consciousness.json"):
        self.consciousness_file = consciousness_file
        self.max_records = 400
        self.version = "31.0"
        self._ensure_storage()

    # --------------------------------------------------
    # Storage Handling
    # --------------------------------------------------
    def _ensure_storage(self):
        if not os.path.exists(self.consciousness_file):
            with open(self.consciousness_file, "w") as f:
                json.dump([], f)

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.consciousness_file, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self, data: List[Dict[str, Any]]):
        with open(self.consciousness_file, "w") as f:
            json.dump(data[-self.max_records:], f, indent=2)

    # --------------------------------------------------
    # Consciousness Update
    # --------------------------------------------------
    def update_consciousness(
        self,
        executive_intelligence: Dict[str, Any],
        continuity: Dict[str, Any],
    ) -> Dict[str, Any]:

        history = self._load()

        intelligence_score = executive_intelligence.get(
            "executive_intelligence_score", 0.5
        )

        continuity_index = continuity.get("continuity_index", 0.5)

        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "intelligence_score": intelligence_score,
            "continuity_index": continuity_index,
        }

        history.append(snapshot)
        self._save(history)

        consciousness_index = self._calculate_consciousness(history)

        return {
            "consciousness_records": len(history),
            "strategic_consciousness_index": consciousness_index,
            "consciousness_state": self._state(consciousness_index),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Consciousness Calculation
    # --------------------------------------------------
    def _calculate_consciousness(self, history: List[Dict[str, Any]]) -> float:

        if len(history) < 12:
            return 0.5

        recent = history[-12:]

        avg_intelligence = sum(
            x["intelligence_score"] for x in recent
        ) / len(recent)

        avg_continuity = sum(
            x["continuity_index"] for x in recent
        ) / len(recent)

        consciousness = (avg_intelligence * 0.6) + (avg_continuity * 0.4)

        consciousness = max(0.0, min(1.0, consciousness))
        return round(consciousness, 3)

    def _state(self, score: float) -> str:
        if score >= 0.8:
            return "EXPANSIVE_WORLDVIEW"
        elif score >= 0.65:
            return "STABLE_WORLDVIEW"
        elif score >= 0.5:
            return "ADAPTING_WORLDVIEW"
        return "FRAGMENTED_WORLDVIEW"