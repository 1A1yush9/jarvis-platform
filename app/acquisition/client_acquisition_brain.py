# ==========================================================
# JARVIS AI — CLIENT ACQUISITION BRAIN
# Stage 11.4
# ==========================================================

from datetime import datetime


class ClientAcquisitionBrain:
    """
    Identifies and recommends new client acquisition opportunities.
    """

    def __init__(self):
        self.opportunity_log = []

    # ------------------------------------------------------
    # Analyze Market Signals
    # ------------------------------------------------------
    def analyze_market(self, industry, demand_score, competition_score):

        opportunity_score = demand_score - competition_score

        result = {
            "industry": industry,
            "demand_score": demand_score,
            "competition_score": competition_score,
            "opportunity_score": opportunity_score,
            "timestamp": datetime.utcnow()
        }

        self.opportunity_log.append(result)

        return result

    # ------------------------------------------------------
    # Recommend Acquisition Target
    # ------------------------------------------------------
    def recommend_target(self, analysis):

        if analysis["opportunity_score"] > 5:
            return {
                "action": "target_industry",
                "industry": analysis["industry"],
                "priority": "high"
            }

        elif analysis["opportunity_score"] > 2:
            return {
                "action": "monitor_industry",
                "industry": analysis["industry"],
                "priority": "medium"
            }

        return {
            "action": "ignore",
            "industry": analysis["industry"],
            "priority": "low"
        }