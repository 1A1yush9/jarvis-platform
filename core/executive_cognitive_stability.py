"""
Stage-29.5 — Executive Cognitive Stability Field (ECSF)

Purpose:
Evaluate long-cycle stability of executive cognition
by tracking meta-reasoning evolution.

Design:
- Advisory only
- Persistence-based observation
- Backward compatible
"""

from typing import Dict, Any, List
import json
import os
from datetime import datetime


class ExecutiveCognitiveStability:
    def __init__(self, stability_file: str = "cognitive_stability.json"):
        self.stability_file = stability_file
        self.max_records = 200
        self.version = "29.5"
        self._ensure_storage()

    # --------------------------------------------------
    # Storage
    # --------------------------------------------------
    def _ensure_storage(self):
        if not os.path.exists(self.stability_file):
            with open(self.stability_file, "w") as f:
                json.dump([], f)

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.stability_file, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self, data: List[Dict[str, Any]]):
        with open(self.stability_file, "w") as f:
            json.dump(data[-self.max_records:], f, indent=2)

    # --------------------------------------------------
    # Stability Update
    # --------------------------------------------------
    def update_stability(self, meta_reasoning: Dict[str, Any]) -> Dict[str, Any]:

        history = self._load()

        score = meta_reasoning.get("meta_reasoning_score", 0.5)

        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "score": score,
        }

        history.append(snapshot)
        self._save(history)

        stability_index = self._calculate_stability(history)

        return {
            "stability_records": len(history),
            "cognitive_stability_index": stability_index,
            "stability_state": self._state(stability_index),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Stability Calculation
    # --------------------------------------------------
    def _calculate_stability(self, history: List[Dict[str, Any]]) -> float:

        if len(history) < 8:
            return 0.5

        recent = history[-8:]
        scores = [x["score"] for x in recent]

        mean = sum(scores) / len(scores)
        variance = sum((s - mean) ** 2 for s in scores) / len(scores)

        stability = 1 - variance
        stability = max(0.0, min(1.0, stability))

        return round(stability, 3)

    def _state(self, stability: float) -> str:
        if stability >= 0.85:
            return "HIGH_STABILITY"
        elif stability >= 0.65:
            return "STABLE"
        elif stability >= 0.45:
            return "OSCILLATING"
        return "UNSTABLE"