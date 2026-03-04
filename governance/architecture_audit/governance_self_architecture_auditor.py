from typing import Dict

from .architecture_signal_collector import ArchitectureSignalCollector
from .architecture_risk_analyzer import ArchitectureRiskAnalyzer


class GovernanceSelfArchitectureAuditor:
    """
    Stage-125.0

    Evaluates the governance system architecture itself.

    Responsibilities

    - Collect architecture signals
    - Analyze structural governance risks
    - Produce architecture improvement advisory
    """

    def __init__(self):

        self.collector = ArchitectureSignalCollector()
        self.analyzer = ArchitectureRiskAnalyzer()

    def evaluate(
        self,
        strategy_report: Dict,
        evolution_report: Dict,
        resilience_report: Dict,
        oversight_report: Dict,
        risk_report: Dict
    ) -> Dict:

        signals = self.collector.collect(
            strategy_report,
            evolution_report,
            resilience_report,
            oversight_report,
            risk_report
        )

        risk = self.analyzer.analyze(signals)

        recommendations = []

        if risk["architecture_risk_level"] == "ARCHITECTURE_RISK":
            recommendations.append("REVIEW_GOVERNANCE_SYSTEM_ARCHITECTURE")

        if risk["architecture_risk_level"] == "WATCH":
            recommendations.append("MONITOR_GOVERNANCE_ARCHITECTURE")

        if not recommendations:
            recommendations.append("ARCHITECTURE_STABLE")

        return {
            "architecture_signals": signals,
            "architecture_assessment": risk,
            "architecture_recommendations": recommendations
        }