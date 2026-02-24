# ==========================================================
# JARVIS AI — SELF IMPROVING INTELLIGENCE CORE
# Stage 13.0
# ==========================================================

from datetime import datetime


class SelfImprovingCore:
    """
    Learns from operational outcomes and adjusts
    strategic preference weights.
    """

    def __init__(self):
        self.learning_memory = []
        self.strategy_weights = {
            "acquisition": 1.0,
            "delivery": 1.0,
            "optimization": 1.0
        }

    # ------------------------------------------------------
    # Record Outcome
    # ------------------------------------------------------
    def record_outcome(self, category, success_score):

        event = {
            "timestamp": datetime.utcnow(),
            "category": category,
            "success_score": success_score
        }

        self.learning_memory.append(event)
        self._adjust_weights(category, success_score)

        return {"status": "learning_updated"}

    # ------------------------------------------------------
    # Adjust Strategy Weights
    # ------------------------------------------------------
    def _adjust_weights(self, category, score):

        if category not in self.strategy_weights:
            return

        adjustment = (score - 0.5) * 0.2
        self.strategy_weights[category] += adjustment

        # keep weights stable
        self.strategy_weights[category] = max(
            0.5,
            min(2.0, self.strategy_weights[category])
        )

    # ------------------------------------------------------
    # Get Current Strategy Bias
    # ------------------------------------------------------
    def get_strategy_profile(self):
        return self.strategy_weights