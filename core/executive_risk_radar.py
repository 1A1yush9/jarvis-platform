"""
Jarvis Platform — Stage 22.5
Executive Risk Radar

Aggregates intelligence signals into a unified
executive risk assessment.

SAFE MODE:
Advisory-only risk modeling.
No execution authority.
"""

from datetime import datetime
from typing import Dict, Any


class ExecutiveRiskRadar:
    def __init__(self, predictive_engine, confidence_engine, prioritizer):
        self.engine_name = "Executive Risk Radar"
        self.version = "22.5"
        self.mode = "advisory_only"

        self.predictive_engine = predictive_engine
        self.confidence_engine = confidence_engine
        self.prioritizer = prioritizer

    # -----------------------------------------------------
    # Risk Evaluation
    # -----------------------------------------------------
    def evaluate_risk(self) -> Dict[str, Any]:

        forecast = self.predictive_engine.forecast()
        confidence = self.confidence_engine.evaluate_confidence()
        priorities = self.prioritizer.prioritize().get("priorities", [])

        risk_score = 0.0
        factors = []

        # Predictive instability contribution
        instability = forecast.get("predicted_instability_risk")

        if instability == "high":
            risk_score += 0.5
            factors.append("High instability forecast detected")
        elif instability == "medium":
            risk_score += 0.3
            factors.append("Emerging instability trend")

        # Confidence penalty
        confidence_score = confidence.get("confidence_score", 1.0)
        if confidence_score < 0.5:
            risk_score += 0.3
            factors.append("Low intelligence confidence")

        # Priority pressure
        critical_count = len(
            [p for p in priorities if p.get("priority") == 1]
        )

        if critical_count > 0:
            risk_score += 0.2
            factors.append("Critical executive signals present")

        risk_score = min(risk_score, 1.0)

        if risk_score >= 0.7:
            level = "high"
        elif risk_score >= 0.4:
            level = "moderate"
        else:
            level = "low"

        return {
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "risk_score": round(risk_score, 2),
            "risk_level": level,
            "risk_factors": factors,
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