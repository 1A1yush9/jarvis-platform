from typing import Dict

from .strategy_signal_aggregator import StrategySignalAggregator
from .governance_strategy_model import GovernanceStrategyModel


class GovernanceAutonomousStrategyEngine:
    """
    Stage-124.0

    Produces deterministic long-horizon governance strategies.
    """

    def __init__(self):

        self.aggregator = StrategySignalAggregator()
        self.model = GovernanceStrategyModel()

    def evaluate(
        self,
        evolution_report: Dict,
        resilience_report: Dict,
        oversight_report: Dict,
        risk_forecast: Dict
    ) -> Dict:

        signals = self.aggregator.aggregate(
            evolution_report,
            resilience_report,
            oversight_report,
            risk_forecast
        )

        strategies = self.model.evaluate(signals)

        return {
            "strategy_signals": signals,
            "governance_strategy": strategies
        }