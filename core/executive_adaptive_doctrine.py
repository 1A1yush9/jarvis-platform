"""
Stage-32.0 — Executive Adaptive Doctrine Engine (EADE)

Purpose:
Form stable strategic doctrine patterns from repeated
executive intelligence outcomes.

Design:
- Advisory only
- Historical pattern aggregation
- Backward compatible
"""

from typing import Dict, Any, List
import json
import os
from datetime import datetime


class ExecutiveAdaptiveDoctrine:
    def __init__(self, doctrine_file: str = "adaptive_doctrine.json"):
        self.doctrine_file = doctrine_file
        self.max_records = 500
        self.version = "32.0"
        self._ensure_storage()

    # --------------------------------------------------
    # Storage
    # --------------------------------------------------
    def _ensure_storage(self):
        if not os.path.exists(self.doctrine_file):
            with open(self.doctrine_file, "w") as f:
                json.dump([], f)

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.doctrine_file, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self, data: List[Dict[str, Any]]):
        with open(self.doctrine_file, "w") as f:
            json.dump(data[-self.max_records:], f, indent=2)

    # --------------------------------------------------
    # Doctrine Update
    # --------------------------------------------------
    def update_doctrine(
        self,
        executive_intelligence: Dict[str, Any],
        reality_alignment: Dict[str, Any],
    ) -> Dict[str, Any]:

        history = self._load()

        intelligence_score = executive_intelligence.get(
            "executive_intelligence_score", 0.5
        )

        reality_score = reality_alignment.get(
            "reality_alignment_index", 0.5
        )

        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "intelligence": intelligence_score,
            "reality_alignment": reality_score,
        }

        history.append(snapshot)
        self._save(history)

        doctrine_strength = self._calculate_doctrine(history)

        return {
            "doctrine_records": len(history),
            "doctrine_strength": doctrine_strength,
            "doctrine_state": self._state(doctrine_strength),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Doctrine Calculation
    # --------------------------------------------------
    def _calculate_doctrine(self, history: List[Dict[str, Any]]) -> float:

        if len(history) < 15:
            return 0.5

        recent = history[-15:]

        avg_intelligence = sum(x["intelligence"] for x in recent) / len(recent)
        avg_reality = sum(x["reality_alignment"] for x in recent) / len(recent)

        doctrine = (avg_intelligence * 0.6) + (avg_reality * 0.4)

        doctrine = max(0.0, min(1.0, doctrine))
        return round(doctrine, 3)

    def _state(self, score: float) -> str:
        if score >= 0.8:
            return "STRONG_DOCTRINE"
        elif score >= 0.65:
            return "EMERGING_DOCTRINE"
        elif score >= 0.5:
            return "FORMING_DOCTRINE"
        return "UNSTABLE_DOCTRINE"