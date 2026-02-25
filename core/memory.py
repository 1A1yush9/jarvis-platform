# core/memory.py

"""
Jarvis Memory System
Safe Version — Render Compatible

Purpose:
Stores short-term cognitive records safely.
No external execution.
"""

from typing import Dict, Any, List

# --------------------------------------------------
# SAFE OPTIONAL IMPORTS
# (prevents boot crash if modules change)
# --------------------------------------------------

try:
    from core.memory_models import CampaignMemory
except Exception:
    CampaignMemory = None

try:
    from core.industry_brain import IndustryBrain
except Exception:
    IndustryBrain = None


# --------------------------------------------------
# MEMORY ENGINE
# --------------------------------------------------

class Memory:

    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    # ----------------------------------------------
    # Store Memory Record
    # ----------------------------------------------
    def store(self, signals: Dict[str, Any], awareness: Dict[str, Any]):

        record = {
            "signals": signals,
            "awareness": awareness
        }

        self.history.append(record)

        # keep bounded memory (safe for Render RAM)
        if len(self.history) > 100:
            self.history.pop(0)

        return {"status": "stored", "count": len(self.history)}

    # ----------------------------------------------
    # Memory Summary
    # ----------------------------------------------
    def summary(self):

        if not self.history:
            return {
                "total_records": 0,
                "status": "empty"
            }

        return {
            "total_records": len(self.history),
            "status": "active"
        }

    # ----------------------------------------------
    # Retrieve All
    # ----------------------------------------------
    def all(self):
        return self.history