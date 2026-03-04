from typing import Dict

from .signal_history_buffer import SignalHistoryBuffer
from .governance_drift_analyzer import GovernanceDriftAnalyzer


class GovernanceStrategicOversightEngine:
    """
    Stage-121.0

    Strategic governance intelligence layer.

    Responsibilities

    - Record governance signals over time
    - Detect systemic governance drift
    - Produce long-horizon governance advisory signals

    No authority to mutate runtime systems.
    """

    def __init__(self):

        self.history = SignalHistoryBuffer()
        self.analyzer = GovernanceDriftAnalyzer()

    def evaluate(
        self,
        cluster_stability: Dict,
        risk_forecast: Dict
    ) -> Dict:

        risk = risk_forecast.get("risk_assessment", {})
        risk_level = risk.get("risk_level", "LOW")

        signal = {
            "cluster_stability": cluster_stability.get("cluster_stability", "STABLE"),
            "risk_level": risk_level
        }

        self.history.record(signal)

        drift = self.analyzer.analyze(self.history.snapshot())

        return {
            "governance_history_size": len(self.history.snapshot()),
            "strategic_analysis": drift
        }