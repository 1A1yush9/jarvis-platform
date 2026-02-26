"""
Jarvis Platform — Stage 23.0
Strategic Drift Explanation Engine

Explains WHY strategic risk or instability is emerging.

SAFE MODE:
Deterministic explanation logic.
No execution authority.
"""

from datetime import datetime
from typing import Dict, Any, List


class StrategicDriftExplainer:
    def __init__(
        self,
        memory_engine,
        predictive_engine,
        confidence_engine,
        risk_radar,
    ):
        self.engine_name = "Strategic Drift Explainer"
        self.version = "23.0"
        self.mode = "advisory_only"

        self.memory_engine = memory_engine
        self.predictive_engine = predictive_engine
        self.confidence_engine = confidence_engine
        self.risk_radar = risk_radar

    # -----------------------------------------------------
    # Drift Explanation
    # -----------------------------------------------------
    def explain(self) -> Dict[str, Any]:

        memory = self.memory_engine.analyze_trends()
        forecast = self.predictive_engine.forecast()
        confidence = self.confidence_engine.evaluate_confidence()
        risk = self.risk_radar.evaluate_risk()

        explanations: List[str] = []

        # Memory trend reasoning
        avg_alignment = memory.get("average_alignment_score")
        if avg_alignment is not None and avg_alignment < 0.6:
            explanations.append(
                "Historical alignment trends indicate gradual strategic degradation."
            )

        # Predictive reasoning
        instability = forecast.get("predicted_instability_risk")
        if instability == "medium":
            explanations.append(
                "Recent trajectory shows declining stability momentum."
            )
        elif instability == "high":
            explanations.append(
                "Rapid negative trajectory detected in strategic indicators."
            )

        # Confidence reasoning
        if confidence.get("confidence_level") == "low":
            explanations.append(
                "Limited intelligence confidence increases uncertainty risk."
            )

        # Risk confirmation
        if risk.get("risk_level") == "high":
            explanations.append(
                "Multiple intelligence layers converge on elevated risk conditions."
            )

        if not explanations:
            explanations.append(
                "No significant strategic drift detected."
            )

        return {
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "drift_explanations": explanations,
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