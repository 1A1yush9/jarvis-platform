# core/proposal_engine.py

from datetime import datetime
from typing import Dict, Any, List


class ProposalIntelligenceEngine:
    """
    Stage-17.2
    Advisory-only proposal generation layer.

    Converts deal + revenue intelligence into
    executive-ready strategic proposals.
    """

    def __init__(self):
        self.version = "17.2"
        self.engine_name = "Proposal Intelligence Engine"

    # --------------------------------------------------
    # MAIN ENTRY
    # --------------------------------------------------

    def generate_proposal(
        self,
        tenant_id: str,
        deal_data: Dict[str, Any],
        revenue_data: Dict[str, Any],
        client_context: Dict[str, Any],
    ) -> Dict[str, Any]:

        opportunity_score = deal_data.get("opportunity_score", 0.5)
        revenue_potential = revenue_data.get("estimated_value", 0)

        services = self._recommend_services(
            opportunity_score,
            client_context
        )

        risk_level = self._risk_analysis(deal_data)

        positioning = self._value_positioning(
            revenue_potential,
            opportunity_score
        )

        confidence = self._confidence_score(
            opportunity_score,
            risk_level
        )

        return {
            "tenant_id": tenant_id,
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),

            "proposal_summary": {
                "opportunity_level": self._opportunity_label(opportunity_score),
                "recommended_services": services,
                "value_positioning": positioning,
                "risk_assessment": risk_level,
                "confidence_score": confidence,
            },

            "executive_recommendation":
                self._executive_advice(confidence, risk_level)
        }

    # --------------------------------------------------
    # INTERNAL INTELLIGENCE METHODS
    # --------------------------------------------------

    def _recommend_services(
        self,
        score: float,
        context: Dict[str, Any]
    ) -> List[str]:

        industry = context.get("industry", "general")

        services = []

        if score > 0.75:
            services.extend([
                "Full Funnel Digital Marketing",
                "Conversion Optimization",
                "Performance Advertising"
            ])
        elif score > 0.5:
            services.extend([
                "SEO Growth Strategy",
                "Content Marketing",
                "Lead Generation Setup"
            ])
        else:
            services.append("Market Position Audit")

        if industry == "local_business":
            services.append("Local SEO Optimization")

        return services

    # --------------------------------------------------

    def _risk_analysis(self, deal_data: Dict[str, Any]) -> str:
        competition = deal_data.get("competition_level", "medium")

        if competition == "high":
            return "Elevated"
        elif competition == "low":
            return "Minimal"

        return "Moderate"

    # --------------------------------------------------

    def _value_positioning(self, revenue: float, score: float) -> str:

        if revenue > 100000 and score > 0.7:
            return "High-value strategic client"

        if revenue > 25000:
            return "Growth-stage opportunity"

        return "Exploratory engagement"

    # --------------------------------------------------

    def _confidence_score(self, score: float, risk: str) -> float:

        risk_modifier = {
            "Minimal": 1.0,
            "Moderate": 0.85,
            "Elevated": 0.65
        }

        return round(score * risk_modifier.get(risk, 0.8), 2)

    # --------------------------------------------------

    def _opportunity_label(self, score: float) -> str:
        if score > 0.75:
            return "High"
        if score > 0.5:
            return "Medium"
        return "Early"

    # --------------------------------------------------

    def _executive_advice(self, confidence: float, risk: str) -> str:

        if confidence > 0.7:
            return "Strong recommendation to pursue proposal."

        if risk == "Elevated":
            return "Proceed cautiously with strategic differentiation."

        return "Validate client intent before resource allocation."