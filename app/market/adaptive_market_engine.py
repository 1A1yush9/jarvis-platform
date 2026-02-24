# ==========================================================
# JARVIS AI — ADAPTIVE MARKET BEHAVIOR ENGINE
# Stage 13.1
# ==========================================================

from datetime import datetime


class AdaptiveMarketEngine:
    """
    Adjusts market targeting behavior based on
    performance feedback and opportunity signals.
    """

    def __init__(self):
        self.market_memory = {}

    # ------------------------------------------------------
    # Record Market Outcome
    # ------------------------------------------------------
    def record_market_feedback(self, industry, success_score):

        entry = self.market_memory.get(industry, {
            "score": 0,
            "samples": 0
        })

        entry["score"] += success_score
        entry["samples"] += 1

        self.market_memory[industry] = entry

        return {"status": "market_feedback_recorded"}

    # ------------------------------------------------------
    # Evaluate Industry Priority
    # ------------------------------------------------------
    def evaluate_industry(self, industry):

        data = self.market_memory.get(industry)

        if not data or data["samples"] == 0:
            return {"priority": "unknown"}

        avg_score = data["score"] / data["samples"]

        if avg_score > 0.75:
            priority = "expand"
        elif avg_score > 0.5:
            priority = "maintain"
        else:
            priority = "reduce"

        return {
            "industry": industry,
            "average_score": round(avg_score, 2),
            "priority": priority,
            "evaluated_at": datetime.utcnow()
        }

    # ------------------------------------------------------
    # Get Best Markets
    # ------------------------------------------------------
    def best_markets(self):

        results = []

        for industry in self.market_memory:
            results.append(self.evaluate_industry(industry))

        return sorted(
            results,
            key=lambda x: x.get("average_score", 0),
            reverse=True
        )