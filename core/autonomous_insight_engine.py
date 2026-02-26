"""
Jarvis Platform — Stage 20.0
Autonomous Insight Generation Layer

Generates proactive executive insights
from existing intelligence systems.

SAFE MODE:
Advisory-only synthesis.
No execution authority.
"""

from typing import Dict, Any, List
from datetime import datetime


class AutonomousInsightEngine:
    def __init__(self, memory_engine, predictive_engine):
        self.engine_name = "Autonomous Insight Engine"
        self.version = "20.0"
        self.mode = "advisory_only"

        self.memory_engine = memory_engine
        self.predictive_engine = predictive_engine

    # -----------------------------------------------------
    # Insight Generator
    # -----------------------------------------------------
    def generate_insights(self) -> Dict[str, Any]:

        memory_analysis = self.memory_engine.analyze_trends()
        forecast = self.predictive_engine.forecast()

        insights: List[str] = []

        avg_score = memory_analysis.get("average_alignment_score")
        instability = forecast.get("predicted_instability_risk")

        # Strategic Health Insight
        if avg_score is not None:
            if avg_score >= 0.75:
                insights.append(
                    "Strategic alignment operating within optimal range."
                )
            elif avg_score >= 0.5:
                insights.append(
                    "Moderate alignment detected. Optimization opportunities present."
                )
            else:
                insights.append(
                    "Low alignment trend detected. Strategic review advised."
                )

        # Predictive Risk Insight
        if instability == "medium":
            insights.append(
                "Early instability signals emerging from strategic trajectory."
            )

        if instability == "high":
            insights.append(
                "High probability of strategic degradation if trajectory continues."
            )

        if not insights:
            insights.append(
                "No critical executive insights detected at this time."
            )

        return {
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "insights": insights,
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