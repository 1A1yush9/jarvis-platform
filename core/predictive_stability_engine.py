"""
Jarvis Platform — Stage 18.5
Predictive Strategic Stability Engine

Purpose:
Forecast future strategic stability using historical alignment data.

SAFE MODE:
Advisory only.
Deterministic forecasting.
No execution authority.
"""

from typing import Dict, Any, List
from datetime import datetime
import json
import os


class PredictiveStabilityEngine:
    def __init__(self, memory_path: str = "memory_alignment.json"):
        self.engine_name = "Predictive Strategic Stability Engine"
        self.version = "18.5"
        self.mode = "advisory_only"
        self.memory_path = memory_path

    # -----------------------------------------------------
    # Memory Loader
    # -----------------------------------------------------
    def _load_memory(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.memory_path):
            return []

        with open(self.memory_path, "r") as f:
            return json.load(f)

    # -----------------------------------------------------
    # Forecast Stability
    # -----------------------------------------------------
    def forecast(self) -> Dict[str, Any]:

        memory = self._load_memory()

        if len(memory) < 3:
            return {
                "engine": self.engine_name,
                "version": self.version,
                "message": "Insufficient historical data for prediction.",
                "mode": self.mode,
            }

        scores = [m.get("alignment_score", 0) for m in memory]

        # recent window
        recent = scores[-5:] if len(scores) >= 5 else scores

        trend_velocity = recent[-1] - recent[0]

        instability_risk = "low"
        advisory = []

        if trend_velocity < -0.15:
            instability_risk = "medium"
            advisory.append(
                "Alignment declining. Monitor executive decisions."
            )

        if trend_velocity < -0.30:
            instability_risk = "high"
            advisory.append(
                "Rapid strategic degradation predicted."
            )

        if instability_risk == "high":
            advisory.append(
                "Executive strategic reassessment recommended."
            )

        return {
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "trend_velocity": round(trend_velocity, 3),
            "predicted_instability_risk": instability_risk,
            "advisory": advisory,
            "mode": self.mode,
        }

    # -----------------------------------------------------
    # Status
    # -----------------------------------------------------
    def status(self) -> Dict[str, Any]:
        return {
            "engine": self.engine_name,
            "version": self.version,
            "status": "operational",
            "mode": self.mode,
        }