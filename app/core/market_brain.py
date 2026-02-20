from datetime import datetime


class MarketBrain:
    """
    Adds seasonal and timing awareness to campaigns.
    """

    FESTIVAL_MAP = {
        1: "new_year",
        2: "valentine",
        3: "financial_year_end",
        4: "summer_start",
        5: "summer_peak",
        6: "monsoon",
        7: "monsoon",
        8: "independence_sale",
        9: "festive_build_up",
        10: "diwali",
        11: "wedding_season",
        12: "year_end_sale"
    }

    @staticmethod
    def get_market_context():

        now = datetime.now()

        month = now.month
        weekday = now.weekday()

        season = MarketBrain.FESTIVAL_MAP.get(month, "regular")

        # urgency logic
        if weekday in [4, 5]:  # Friday / Saturday
            urgency = "high"
        elif weekday == 6:
            urgency = "medium"
        else:
            urgency = "normal"

        return {
            "month": month,
            "season": season,
            "urgency_level": urgency
        }
