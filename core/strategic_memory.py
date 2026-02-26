"""
Stage-24.5 — Strategic Memory Consolidation Layer (SMCL)

Purpose:
Maintain long-term strategic awareness by storing
alignment history and detecting macro trends.

Design Principles:
- Advisory only
- Failure-safe storage
- Backward compatible
"""

from typing import Dict, Any, List
import json
import os
from datetime import datetime


class StrategicMemory:
    def __init__(self, memory_file: str = "strategic_memory.json"):
        self.memory_file = memory_file
        self.max_records = 200
        self.version = "24.5"

        self._ensure_memory()

    # --------------------------------------------------
    # Memory Initialization
    # --------------------------------------------------
    def _ensure_memory(self):
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump([], f)

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.memory_file, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self, data: List[Dict[str, Any]]):
        with open(self.memory_file, "w") as f:
            json.dump(data[-self.max_records:], f, indent=2)

    # --------------------------------------------------
    # Store Snapshot
    # --------------------------------------------------
    def store_snapshot(self, alignment_result: Dict[str, Any]) -> Dict[str, Any]:

        history = self._load()

        snapshot = {
            "timestamp": datetime.utcnow().isoformat(),
            "alignment_score": alignment_result.get("alignment_score", 0.5),
            "alignment_status": alignment_result.get("alignment_status", "UNKNOWN"),
        }

        history.append(snapshot)
        self._save(history)

        trend = self._calculate_trend(history)

        return {
            "memory_records": len(history),
            "alignment_trend": trend,
            "memory_version": self.version,
        }

    # --------------------------------------------------
    # Trend Analysis
    # --------------------------------------------------
    def _calculate_trend(self, history: List[Dict[str, Any]]) -> str:

        if len(history) < 5:
            return "INSUFFICIENT_DATA"

        recent = history[-5:]
        scores = [x["alignment_score"] for x in recent]

        delta = scores[-1] - scores[0]

        if delta > 0.08:
            return "IMPROVING"
        elif delta < -0.08:
            return "DEGRADING"
        else:
            return "STABLE"