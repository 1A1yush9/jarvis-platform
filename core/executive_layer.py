"""
Jarvis Executive Decision Layer
Stage-14.5

Transforms cognitive outputs into
executive-level strategic briefings.

SAFE MODE:
Advisory synthesis only.
No execution authority.
"""

from typing import Dict, Any
from datetime import datetime


class ExecutiveDecisionLayer:

    def __init__(self):
        self.last_briefing: Dict[str, Any] = {}

    # ---------------------------------------------------
    # EXECUTIVE SYNTHESIS
    # ---------------------------------------------------

    def synthesize(
        self,
        signals: Dict[str, Any],
        context: Dict[str, Any],
        prediction: Dict[str, Any],
        priority: Dict[str, Any]
    ) -> Dict[str, Any]:

        top_priority = priority.get("top_priority", "balanced")
        risk = prediction.get("risk_outlook", "LOW")
        context_label = context.get("context_label", "stable_operations")

        summary = self._generate_summary(
            top_priority,
            context_label,
            risk
        )

        briefing = {
            "timestamp": datetime.utcnow().isoformat(),
            "executive_summary": summary,
            "focus_area": top_priority,
            "risk_level": risk,
            "recommended_posture": self._posture(top_priority, risk),
        }

        self.last_briefing = briefing
        return briefing

    # ---------------------------------------------------

    def _generate_summary(self, priority, context, risk):

        return (
            f"System operating under '{context}' conditions. "
            f"Primary strategic focus should shift toward "
            f"'{priority}'. Current assessed risk level is {risk}."
        )

    # ---------------------------------------------------

    def _posture(self, priority, risk):

        if risk in ["ELEVATED", "MEDIUM"]:
            return "stabilize_and_optimize"

        if priority in ["expansion", "acquisition"]:
            return "growth_acceleration"

        if priority == "delivery":
            return "capacity_protection"

        if priority == "revenue":
            return "revenue_reinforcement"

        return "balanced_execution"

    # ---------------------------------------------------

    def status(self):
        return self.last_briefing


# Singleton
executive_layer = ExecutiveDecisionLayer()