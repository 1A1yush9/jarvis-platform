"""
Stage-28.5 — Strategic Awareness Loop (SAL)

Purpose:
Maintain continuous executive awareness by tracking
confidence evolution across cycles.

Design:
- Advisory only
- Persistence-based observation
- Backward compatible
"""

from typing import Dict, Any, List
import json
import os
from datetime import datetime


class StrategicAwarenessLoop:
    def __init__(self, awareness_file: str = "awareness_history.json"):
        self.awareness_file = awareness_file
        self.max_records = 200
        self.version = "28.5"
        self._ensure_storage()

    # --------------------------------------------------
    # Storage Handling
    # --------------------------------------------------
    def _ensure_storage(self):
        if not os.path.exists(self.awareness_file):
            with open(self.awareness_file, "w") as f:
                json.dump([], f)

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.awareness_file, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self, data: List[Dict[str, Any]]):
        with open(self.awareness_file, "w") as f:
            json.dump(data[-self.max_records:], f, indent=2)

    # --------------------------------------------------
    # Awareness Update
    # --------------------------------------------------
    def update_awareness(self, calibration: Dict[str, Any]) -> Dict[str, Any]:

        history = self._load()

        confidence = calibration.get("calibrated_confidence", 0.5)

        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "confidence": confidence,
        }

        history.append(snapshot)
        self._save(history)

        momentum = self._calculate_momentum(history)

        return {
            "awareness_records": len(history),
            "awareness_momentum": momentum,
            "awareness_state": self._state(momentum),
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Momentum Analysis
    # --------------------------------------------------
    def _calculate_momentum(self, history: List[Dict[str, Any]]) -> float:

        if len(history) < 6:
            return 0.0

        recent = history[-6:]
        delta = recent[-1]["confidence"] - recent[0]["confidence"]
        return round(delta, 3)

    def _state(self, momentum: float) -> str:
        if momentum > 0.05:
            return "STRENGTHENING_AWARENESS"
        elif momentum < -0.05:
            return "DECLINING_AWARENESS"
        return "STABLE_AWARENESS"