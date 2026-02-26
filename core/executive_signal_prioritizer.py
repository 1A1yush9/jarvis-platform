"""
Jarvis Platform — Stage 21.0
Executive Signal Prioritization Engine

Ranks intelligence signals by urgency and importance.

SAFE MODE:
Advisory-only prioritization.
No execution authority.
"""

from typing import Dict, Any, List
from datetime import datetime


class ExecutiveSignalPrioritizer:
    def __init__(self, cycle_engine):
        self.engine_name = "Executive Signal Prioritizer"
        self.version = "21.0"
        self.mode = "advisory_only"
        self.cycle_engine = cycle_engine

    # -----------------------------------------------------
    # Priority Scoring
    # -----------------------------------------------------
    def prioritize(self) -> Dict[str, Any]:

        state = self.cycle_engine.get_state().get("state", {})
        insights = state.get("insights", {}).get("insights", [])
        forecast = state.get("forecast", {})

        prioritized: List[Dict[str, Any]] = []

        risk = forecast.get("predicted_instability_risk")

        # Forecast priority
        if risk == "high":
            prioritized.append({
                "priority": 1,
                "type": "stability_risk",
                "message": "High instability risk predicted."
            })

        elif risk == "medium":
            prioritized.append({
                "priority": 2,
                "type": "stability_warning",
                "message": "Alignment degradation emerging."
            })

        # Insight priorities
        for insight in insights:
            score = 3
            if "Low alignment" in insight:
                score = 1
            elif "Moderate" in insight:
                score = 2

            prioritized.append({
                "priority": score,
                "type": "executive_insight",
                "message": insight
            })

        prioritized.sort(key=lambda x: x["priority"])

        return {
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "priorities": prioritized,
            "mode": self.mode,
        }

    # -----------------------------------------------------
    # Status
    # -----------------------------------------------------
    def status(self):
        return {
            "engine": self.engine_name,
            "version": self.version,
            "status": "operational",
            "mode": self.mode,
        }