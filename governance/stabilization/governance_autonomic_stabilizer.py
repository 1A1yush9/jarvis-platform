from typing import Dict

from .stabilization_signal_analyzer import StabilizationSignalAnalyzer
from .influence_rebalance_model import InfluenceRebalanceModel


class GovernanceAutonomicStabilizer:
    """
    Stage-120.0

    Generates deterministic governance stabilization actions.
    """

    def __init__(self):

        self.signal_analyzer = StabilizationSignalAnalyzer()
        self.rebalance_model = InfluenceRebalanceModel()

    def evaluate(
        self,
        risk_forecast: Dict,
        cluster_stability: Dict,
        fault_domain_status: Dict
    ) -> Dict:

        signals = self.signal_analyzer.analyze(
            risk_forecast,
            cluster_stability
        )

        rebalance = self.rebalance_model.rebalance(
            signals,
            fault_domain_status
        )

        return {
            "stabilization_signals": signals,
            "stabilization_strategy": rebalance
        }