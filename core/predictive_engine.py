"""
Jarvis Predictive Reasoning Engine
Stage-14.3

Produces short-horizon forecasts based on
current signals and contextual reasoning.

SAFE MODE:
Prediction only.
No execution authority.
"""

from typing import Dict, Any
from datetime import datetime


class PredictiveReasoningEngine:

    def __init__(self):
        self.last_prediction: Dict[str, Any] = {}

    # ---------------------------------------------------
    # PREDICTION LOGIC
    # ---------------------------------------------------

    def forecast(
        self,
        signals: Dict[str, Any],
        context: Dict[str, Any]
    ) -> Dict[str, Any]:

        load = signals.get("execution_load", 0.0)
        revenue = signals.get("revenue_velocity", 0.0)
        market = signals.get("market_opportunity_score", 0.0)

        context_label = context.get("context_label", "stable")

        load_trend = "stable"
        revenue_trend = "stable"
        risk_outlook = "LOW"

        # Load trajectory
        if context_label == "growth_pressure":
            load_trend = "increasing"

        if load > 0.8:
            risk_outlook = "MEDIUM"

        # Revenue trajectory
        if revenue < 0.3:
            revenue_trend = "declining"
            risk_outlook = "ELEVATED"

        elif market > 0.7:
            revenue_trend = "likely_growth"

        # Expansion probability
        expansion_probability = round(
            min(1.0, (market * 0.6 + (1 - load) * 0.4)),
            2
        )

        prediction = {
            "timestamp": datetime.utcnow().isoformat(),
            "load_trend": load_trend,
            "revenue_trend": revenue_trend,
            "risk_outlook": risk_outlook,
            "expansion_probability": expansion_probability,
            "confidence": self._confidence(signals)
        }

        self.last_prediction = prediction
        return prediction

    # ---------------------------------------------------

    def _confidence(self, signals: Dict[str, Any]) -> float:
        vals = list(signals.values())
        if not vals:
            return 0.0
        avg = sum(vals) / len(vals)
        return round(min(1.0, 0.55 + avg / 2), 2)

    # ---------------------------------------------------

    def status(self):
        return self.last_prediction


# Singleton
predictive_engine = PredictiveReasoningEngine()