# core/executive_decision_engine.py

from typing import List, Dict, Any
from datetime import datetime


class ExecutiveDecisionEngine:
    """
    Stage-17.3
    Executive advisory layer.

    Converts proposal intelligence into
    prioritized executive decisions.
    """

    def __init__(self):
        self.engine_name = "Executive Decision Engine"
        self.version = "17.3"

    # --------------------------------------------------
    # MAIN ENTRY
    # --------------------------------------------------

    def evaluate_pipeline(
        self,
        tenant_id: str,
        proposals: List[Dict[str, Any]]
    ) -> Dict[str, Any]:

        ranked = []

        for proposal in proposals:
            score = self._decision_score(proposal)
            ranked.append({
                "decision_score": score,
                "proposal": proposal
            })

        ranked.sort(key=lambda x: x["decision_score"], reverse=True)

        priorities = self._assign_priority_labels(ranked)

        return {
            "tenant_id": tenant_id,
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "decisions": priorities,
            "executive_summary": self._executive_summary(priorities)
        }

    # --------------------------------------------------

    def _decision_score(self, proposal: Dict[str, Any]) -> float:

        summary = proposal.get("proposal_summary", {})

        confidence = summary.get("confidence_score", 0.5)
        risk = summary.get("risk_assessment", "Moderate")
        opportunity = summary.get("opportunity_level", "Medium")

        opportunity_weight = {
            "High": 1.0,
            "Medium": 0.8,
            "Early": 0.6
        }

        risk_modifier = {
            "Minimal": 1.0,
            "Moderate": 0.85,
            "Elevated": 0.65
        }

        base = confidence * opportunity_weight.get(opportunity, 0.7)
        return round(base * risk_modifier.get(risk, 0.8), 3)

    # --------------------------------------------------

    def _assign_priority_labels(self, ranked):

        output = []

        for index, item in enumerate(ranked):

            if index == 0:
                priority = "Primary Focus"
            elif index <= 2:
                priority = "High Priority"
            elif index <= 5:
                priority = "Maintain Momentum"
            else:
                priority = "Monitor"

            output.append({
                "priority": priority,
                "decision_score": item["decision_score"],
                "proposal": item["proposal"]
            })

        return output

    # --------------------------------------------------

    def _executive_summary(self, priorities):

        if not priorities:
            return "No active opportunities available."

        top = priorities[0]

        if top["decision_score"] > 0.7:
            return "Strong growth opportunity detected. Strategic focus recommended."

        if top["decision_score"] > 0.5:
            return "Balanced opportunity pipeline. Selective engagement advised."

        return "Pipeline quality emerging. Continue signal monitoring."