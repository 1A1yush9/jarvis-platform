class OptimizerBrain:

    @staticmethod
    def evaluate_campaign(prediction: dict, roi_score: float):

        predicted_roi = prediction["predicted_roi"]

        # --- Kill switch ---
        if roi_score < 0:
            return {
                "action": "pause_campaign",
                "reason": "Negative ROI detected",
                "budget_multiplier": 0
            }

        # --- Underperforming ---
        if roi_score < predicted_roi * 0.6:
            return {
                "action": "reduce_budget",
                "reason": "Performance below expectation",
                "budget_multiplier": 0.7
            }

        # --- Performing well ---
        if roi_score > predicted_roi * 1.2:
            return {
                "action": "scale_campaign",
                "reason": "Performance exceeding prediction",
                "budget_multiplier": 1.3
            }

        # --- Stable ---
        return {
            "action": "maintain",
            "reason": "Performance within expected range",
            "budget_multiplier": 1.0
        }
