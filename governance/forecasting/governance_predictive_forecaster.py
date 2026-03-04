from typing import Dict

from .risk_signal_aggregator import RiskSignalAggregator
from .governance_risk_model import GovernanceRiskModel


class GovernancePredictiveForecaster:
    """
    Stage-119.0

    Forecasts governance instability using deterministic signals.
    """

    def __init__(self):

        self.aggregator = RiskSignalAggregator()
        self.model = GovernanceRiskModel()

    def evaluate(
        self,
        replication_result: Dict,
        security_report: Dict,
        fault_domain_status: Dict
    ) -> Dict:

        signals = self.aggregator.aggregate(
            replication_result,
            security_report,
            fault_domain_status
        )

        risk = self.model.score(signals)

        return {
            "risk_signals": signals,
            "risk_assessment": risk
        }