class MessagingBrain:
    """
    Decides communication tone dynamically.
    """

    @staticmethod
    def decide_tone(prediction, budget_plan, market_context):

        roi = prediction["predicted_roi"]
        mode = budget_plan.get("mode", "test")
        season = market_context.get("season", "regular")
        urgency = market_context.get("urgency_level", "normal")

        # --- Base tone ---
        if roi > 1.5:
            tone = "confident"
        elif roi > 0.8:
            tone = "persuasive"
        else:
            tone = "educational"

        # --- Budget influence ---
        if mode == "scale":
            tone = "aggressive_conversion"
        elif mode == "test":
            tone = "soft_explainer"

        # --- Seasonal override ---
        if season in ["diwali", "year_end_sale", "independence_sale"]:
            tone = "offer_driven"

        # --- Urgency modifier ---
        if urgency == "high":
            cta_style = "strong_cta"
        else:
            cta_style = "normal_cta"

        return {
            "tone": tone,
            "cta_style": cta_style,
            "season": season
        }
