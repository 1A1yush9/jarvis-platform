"""
Jarvis Strategic Priority Intelligence
Stage-14.4

Determines which strategic domain currently
deserves highest system attention.

SAFE MODE:
Advisory prioritization only.
No execution authority.
"""

from typing import Dict, Any
from datetime import datetime


class StrategicPriorityIntelligence:

    def __init__(self):
        self.last_priority: Dict[str, Any] = {}

    # ---------------------------------------------------
    # PRIORITY SCORING
    # ---------------------------------------------------

    def evaluate(
        self,
        signals: Dict[str, Any],
        context: Dict[str, Any],
        prediction: Dict[str, Any]
    ) -> Dict[str, Any]:

        priorities = {
            "acquisition": 0.5,
            "delivery": 0.5,
            "revenue": 0.5,
            "expansion": 0.5,
            "risk_management": 0.5,
        }

        context_label = context.get("context_label", "")
        risk_outlook = prediction.get("risk_outlook", "LOW")
        expansion_prob = prediction.get("expansion_probability", 0.0)

        # Context influence
        if context_label == "growth_pressure":
            priorities["delivery"] += 0.4

        if context_label == "revenue_risk":
            priorities["revenue"] += 0.6
            priorities["risk_management"] += 0.3

        if context_label == "expansion_window":
            priorities["expansion"] += 0.5
            priorities["acquisition"] += 0.3

        # Prediction influence
        if risk_outlook in ["MEDIUM", "ELEVATED"]:
            priorities["risk_management"] += 0.5

        if expansion_prob > 0.7:
            priorities["expansion"] += 0.4

        # Rank priorities
        ranked = sorted(
            priorities.items(),
            key=lambda x: x[1],
            reverse=True
        )

        result = {
            "timestamp": datetime.utcnow().isoformat(),
            "top_priority": ranked[0][0],
            "priority_scores": priorities,
            "ranking": ranked
        }

        self.last_priority = result
        return result

    # ---------------------------------------------------

    def status(self):
        return self.last_priority


# Singleton
priority_intelligence = StrategicPriorityIntelligence()