"""
Jarvis Platform — Stage 18.0
Adaptive Strategy Memory Loop
Advisory-only persistent alignment memory.
"""

from datetime import datetime
from typing import Dict, Any, List
import json
import os


class AdaptiveStrategyMemory:
    def __init__(self, storage_path: str = "memory_alignment.json"):
        self.engine_name = "Adaptive Strategy Memory Loop"
        self.version = "18.0"
        self.mode = "advisory_only"
        self.storage_path = storage_path

        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w") as f:
                json.dump([], f)

    def _load_memory(self) -> List[Dict[str, Any]]:
        with open(self.storage_path, "r") as f:
            return json.load(f)

    def _save_memory(self, data: List[Dict[str, Any]]):
        with open(self.storage_path, "w") as f:
            json.dump(data, f, indent=2)

    def record_alignment_event(self, alignment_result: Dict[str, Any]):

        memory = self._load_memory()

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "alignment_score": alignment_result.get("alignment_score"),
            "drift_flags_count": len(
                alignment_result.get("drift_flags", [])
            ),
        }

        memory.append(entry)
        self._save_memory(memory)

        return {
            "status": "recorded",
            "total_records": len(memory),
            "mode": self.mode,
        }

    def analyze_trends(self):

        memory = self._load_memory()

        if not memory:
            return {
                "message": "No historical data available.",
                "mode": self.mode,
            }

        scores = [m["alignment_score"] for m in memory if m["alignment_score"]]

        avg_score = round(sum(scores) / len(scores), 2) if scores else 0.0

        return {
            "records_analyzed": len(memory),
            "average_alignment_score": avg_score,
            "mode": self.mode,
        }

    def status(self):
        return {
            "engine": self.engine_name,
            "version": self.version,
            "status": "operational",
            "mode": self.mode,
        }