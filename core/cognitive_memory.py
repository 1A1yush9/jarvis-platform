# core/cognitive_memory.py

"""
Stage-14.7 — Cognitive Memory Formation

Purpose:
Stores structured reasoning experiences so Jarvis
can reference historical cognitive performance.

Advisory cognition only.
No autonomous learning or execution authority.
"""

from typing import Dict, Any, List
from datetime import datetime


class CognitiveMemory:

    def __init__(self, max_memory: int = 100):
        self.version = "14.7"
        self.mode = "advisory"
        self.max_memory = max_memory
        self.memory_store: List[Dict[str, Any]] = []

    # --------------------------------------------------
    # Store Cognitive Event
    # --------------------------------------------------
    def store_memory(
        self,
        signals: Dict[str, Any],
        awareness_report: Dict[str, Any],
    ) -> Dict[str, Any]:

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "signal_size": len(signals),
            "confidence_score": awareness_report.get("confidence_score"),
            "risk_flags": awareness_report.get("risk_flags", []),
            "advisory_strength": awareness_report.get("advisory_strength"),
            "reasoning_quality": awareness_report.get("reasoning_quality"),
        }

        self.memory_store.append(record)

        # Maintain bounded memory
        if len(self.memory_store) > self.max_memory:
            self.memory_store.pop(0)

        return {
            "status": "stored",
            "memory_count": len(self.memory_store)
        }

    # --------------------------------------------------
    # Memory Summary
    # --------------------------------------------------
    def summarize_memory(self) -> Dict[str, Any]:

        if not self.memory_store:
            return {
                "status": "empty",
                "patterns_detected": False
            }

        avg_confidence = sum(
            m["confidence_score"] for m in self.memory_store
        ) / len(self.memory_store)

        high_risk_events = sum(
            1 for m in self.memory_store if m["risk_flags"]
        )

        return {
            "total_memories": len(self.memory_store),
            "average_confidence": round(avg_confidence, 2),
            "high_risk_events": high_risk_events,
            "patterns_detected": high_risk_events > 3
        }

    # --------------------------------------------------
    # Retrieve Recent Memories
    # --------------------------------------------------
    def recent(self, limit: int = 5) -> List[Dict[str, Any]]:
        return self.memory_store[-limit:]