# ==========================================================
# JARVIS AI — STRATEGIC EVOLUTION ENGINE
# Stage 13.2
# ==========================================================

from datetime import datetime


class StrategicEvolutionEngine:
    """
    Evolves long-term strategy preferences using
    accumulated intelligence signals.
    """

    def __init__(self):
        self.strategy_history = []
        self.current_strategy = {
            "growth_mode": "balanced",
            "market_focus": "diversified",
            "execution_style": "controlled"
        }

    # ------------------------------------------------------
    # Record Strategic Outcome
    # ------------------------------------------------------
    def record_strategy_result(self, result_score):

        entry = {
            "timestamp": datetime.utcnow(),
            "result_score": result_score
        }

        self.strategy_history.append(entry)
        self._evolve_strategy(result_score)

        return {"status": "strategy_updated"}

    # ------------------------------------------------------
    # Strategy Evolution Logic
    # ------------------------------------------------------
    def _evolve_strategy(self, score):

        if score > 0.8:
            self.current_strategy["growth_mode"] = "aggressive"

        elif score > 0.6:
            self.current_strategy["growth_mode"] = "balanced"

        else:
            self.current_strategy["growth_mode"] = "conservative"

    # ------------------------------------------------------
    # Get Current Strategy
    # ------------------------------------------------------
    def get_strategy(self):
        return self.current_strategy