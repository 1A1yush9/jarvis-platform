"""
Jarvis Contextual Reasoning Layer
Stage-14.2

Transforms raw signals into contextual intelligence.

This layer explains WHY system conditions exist,
not just WHAT values are observed.

SAFE MODE:
Read-only reasoning.
No execution authority.
"""

from typing import Dict, Any
from datetime import datetime


class ContextualReasoner:

    def __init__(self):
        self.last_context: Dict[str, Any] = {}

    # ---------------------------------------------------
    # CONTEXT ANALYSIS
    # ---------------------------------------------------

    def analyze(self, signals: Dict[str, Any]) -> Dict[str, Any]:

        clients = signals.get("clients_active", 0)
        load = signals.get("execution_load", 0.0)
        revenue = signals.get("revenue_velocity", 0.0)
        market = signals.get("market_opportunity_score", 0.0)

        context_label = "stable_operations"
        explanation = "System operating within normal parameters."

        # Growth pressure detection
        if load > 0.75 and clients > 3:
            context_label = "growth_pressure"
            explanation = (
                "Execution demand increasing due to client growth."
            )

        # Revenue concern
        if revenue < 0.25:
            context_label = "revenue_risk"
            explanation = (
                "Revenue velocity declining relative to activity."
            )

        # Opportunity window
        if market > 0.7 and load < 0.7:
            context_label = "expansion_window"
            explanation = (
                "Market opportunity available with execution capacity."
            )

        context = {
            "timestamp": datetime.utcnow().isoformat(),
            "context_label": context_label,
            "explanation": explanation,
            "confidence": self._confidence_score(signals)
        }

        self.last_context = context
        return context

    # ---------------------------------------------------

    def _confidence_score(self, signals: Dict[str, Any]) -> float:
        """
        Simple deterministic confidence model.
        Can evolve later via learning engine.
        """
        values = list(signals.values())
        if not values:
            return 0.0

        avg = sum(values) / len(values)
        return round(min(1.0, 0.5 + avg / 2), 2)

    # ---------------------------------------------------

    def status(self):
        return self.last_context


# Singleton
context_reasoner = ContextualReasoner()