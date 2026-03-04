from typing import Dict

from .policy_signal_aggregator import PolicySignalAggregator
from .policy_adaptation_model import PolicyAdaptationModel


class GovernanceAdaptiveEvolutionEngine:
    """
    Stage-123.0

    Generates deterministic governance policy evolution recommendations.

    Responsibilities

    - Analyze resilience and risk signals
    - Detect need for governance policy adjustments
    - Produce adaptive governance advisory output

    No runtime mutation authority.
    """

    def __init__(self):

        self.aggregator = PolicySignalAggregator()
        self.model = PolicyAdaptationModel()

    def evaluate(
        self,
        meta_resilience: Dict,
        risk_forecast: Dict,
        oversight: Dict
    ) -> Dict:

        signals = self.aggregator.aggregate(
            meta_resilience,
            risk_forecast,
            oversight
        )

        recommendations = self.model.evaluate(signals)

        return {
            "policy_signals": signals,
            "policy_evolution_advisory": recommendations
        }