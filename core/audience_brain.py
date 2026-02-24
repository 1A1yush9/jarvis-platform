class AudienceBrain:
    """
    Detects audience characteristics and buying psychology.
    """

    @staticmethod
    def detect_audience(intent, budget_plan, strategy_plan):

        industry = intent.industry.lower()
        total_budget = budget_plan.get("total_budget", 0)

        # -------------------
        # B2B vs B2C
        # -------------------
        if industry in ["real estate", "construction", "software", "saas"]:
            audience_type = "B2B"
        else:
            audience_type = "B2C"

        # -------------------
        # Price sensitivity
        # -------------------
        if total_budget > 80000:
            price_segment = "premium"
        elif total_budget > 30000:
            price_segment = "mid_market"
        else:
            price_segment = "price_sensitive"

        # -------------------
        # Decision speed
        # -------------------
        if audience_type == "B2B":
            decision_style = "logical"
        else:
            decision_style = "emotional"

        return {
            "audience_type": audience_type,
            "price_segment": price_segment,
            "decision_style": decision_style
        }
