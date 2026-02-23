# app/opportunity_engine.py

import time
import uuid
from typing import Dict, List

class OpportunityEngine:
    """
    Stage-6.3
    Opportunity Discovery Engine

    Converts predictive awareness signals into
    monetizable opportunities per client.
    """

    def __init__(self):
        self.client_opportunities: Dict[str, List[dict]] = {}

    # -----------------------------
    # Opportunity Scoring Model
    # -----------------------------
    def _score_signal(self, signal: dict) -> float:
        """
        Basic scoring formula:
        score = trend_strength * urgency * monetization
        """

        trend = signal.get("trend_strength", 0.5)
        urgency = signal.get("urgency", 0.5)
        monetization = signal.get("monetization", 0.5)

        score = round((trend * urgency * monetization) * 100, 2)
        return score

    # -----------------------------
    # Opportunity Builder
    # -----------------------------
    def generate_opportunity(self, client_id: str, signal: dict) -> dict:

        score = self._score_signal(signal)

        opportunity = {
            "opportunity_id": str(uuid.uuid4()),
            "client_id": client_id,
            "title": signal.get("title", "Emerging Market Opportunity"),
            "description": signal.get(
                "description",
                "AI detected a potential growth opportunity."
            ),
            "score": score,
            "priority": self._priority_label(score),
            "created_at": time.time(),
            "status": "active"
        }

        self.client_opportunities.setdefault(client_id, []).append(opportunity)
        return opportunity

    # -----------------------------
    # Priority Classification
    # -----------------------------
    def _priority_label(self, score: float) -> str:
        if score >= 70:
            return "HIGH"
        elif score >= 40:
            return "MEDIUM"
        return "LOW"

    # -----------------------------
    # Public Accessors
    # -----------------------------
    def get_client_opportunities(self, client_id: str) -> List[dict]:
        return self.client_opportunities.get(client_id, [])

    def system_snapshot(self):
        total = sum(len(v) for v in self.client_opportunities.values())
        return {
            "engine": "Opportunity Discovery Engine",
            "total_opportunities": total,
            "clients_active": len(self.client_opportunities)
        }