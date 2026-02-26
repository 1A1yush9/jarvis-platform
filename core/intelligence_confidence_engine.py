"""
Jarvis Platform — Stage 22.0
Intelligence Confidence Scoring Layer

Evaluates reliability of generated intelligence.

SAFE MODE:
Deterministic scoring only.
No execution authority.
"""

from datetime import datetime
from typing import Dict, Any


class IntelligenceConfidenceEngine:
    def __init__(self, memory_engine, predictive_engine, cycle_engine):
        self.engine_name = "Intelligence Confidence Engine"
        self.version = "22.0"
        self.mode = "advisory_only"

        self.memory_engine = memory_engine
        self.predictive_engine = predictive_engine
        self.cycle_engine = cycle_engine

    # -----------------------------------------------------
    # Confidence Evaluation
    # -----------------------------------------------------
    def evaluate_confidence(self) -> Dict[str, Any]:

        memory_analysis = self.memory_engine.analyze_trends()
        forecast = self.predictive_engine.forecast()
        cycle_state = self.cycle_engine.get_state()

        score = 1.0
        factors = []

        # Memory depth
        records = memory_analysis.get("records_analyzed", 0)
        if records < 3:
            score -= 0.3
            factors.append("Limited historical memory depth")

        # Forecast availability
        if "predicted_instability_risk" not in forecast:
            score -= 0.3
            factors.append("Insufficient predictive data")

        # Cycle freshness
        if not cycle_state.get("state", {}).get("last_run"):
            score -= 0.2
            factors.append("Continuous monitoring not yet stabilized")

        score = max(score, 0.1)

        if score >= 0.75:
            level = "high"
        elif score >= 0.5:
            level = "moderate"
        else:
            level = "low"

        return {
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "confidence_score": round(score, 2),
            "confidence_level": level,
            "factors": factors,
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