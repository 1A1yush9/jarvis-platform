class BudgetBrain:

    @staticmethod
    def optimize_budget(strategy_plan: dict, prediction: dict):

        roi = prediction["predicted_roi"]
        risk = prediction["risk_level"]
        confidence = strategy_plan["confidence"]

        # --- Base budget logic ---
        if roi > 1.5 and risk == "low":
            total_budget = 100000
            mode = "scale"

        elif roi > 0.8:
            total_budget = 50000
            mode = "growth"

        else:
            total_budget = 15000
            mode = "test"

        # --- Adjust by confidence ---
        if confidence == "high":
            total_budget *= 1.2
        elif confidence == "low":
            total_budget *= 0.7

        total_budget = int(total_budget)

        # --- Channel allocation ---
        allocation = {}
        for channel, percent in strategy_plan["budget_split"].items():
            allocation[channel] = int(total_budget * (percent / 100))

        return {
            "mode": mode,
            "total_budget": total_budget,
            "channel_allocation": allocation
        }
