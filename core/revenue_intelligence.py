# core/revenue_intelligence.py

"""
Stage-17.0 — Revenue Intelligence Layer
Tracks value-generation signals per client.
"""

from typing import Dict, Any
from datetime import datetime


class RevenueIntelligence:

    def __init__(self):
        self.client_revenue_state: Dict[str, Dict[str, Any]] = {}

    # --------------------------------------------------
    # Evaluate Opportunity
    # --------------------------------------------------
    def evaluate(self, client_id: str, signals: Dict[str, Any]):

        if client_id not in self.client_revenue_state:
            self.client_revenue_state[client_id] = {
                "interactions": 0,
                "opportunity_score": 0,
                "last_activity": None
            }

        state = self.client_revenue_state[client_id]

        # Simple scoring logic (safe baseline)
        engagement = len(signals.keys())

        state["interactions"] += 1
        state["opportunity_score"] += engagement
        state["last_activity"] = datetime.utcnow().isoformat()

        return {
            "client_id": client_id,
            "interactions": state["interactions"],
            "opportunity_score": state["opportunity_score"]
        }

    # --------------------------------------------------
    # Client Revenue Summary
    # --------------------------------------------------
    def summary(self, client_id: str):

        return self.client_revenue_state.get(
            client_id,
            {"status": "no_activity"}
        )