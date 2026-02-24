# app/core/strategy_rewrite.py

from datetime import datetime
from typing import Dict, Any, List
import threading
import time


class StrategyRewriteEngine:
    """
    Stage 10.1 — Autonomous Strategy Rewrite Engine

    Evaluates long-term enterprise signals and
    adjusts strategic direction in a controlled manner.
    """

    def __init__(self, executive_core=None, enterprise_controller=None):
        self.active = True

        self.executive_core = executive_core
        self.enterprise_controller = enterprise_controller

        self.state = {
            "mode": "strategic_observation",
            "current_strategy": "adaptive_growth",
            "last_rewrite": None
        }

        self.history: List[Dict[str, Any]] = []

        self.thread = threading.Thread(
            target=self._rewrite_loop,
            daemon=True
        )
        self.thread.start()

    # ---------------------------------------------------
    # MAIN LOOP
    # ---------------------------------------------------
    def _rewrite_loop(self):
        while self.active:
            try:
                rewrite = self._evaluate_strategy()

                if rewrite:
                    self.history.append(rewrite)

                    if len(self.history) > 200:
                        self.history.pop(0)

                    self.state.update(rewrite)
                    self.state["last_rewrite"] = rewrite["timestamp"]

                    print(
                        f"[StrategyRewrite] Strategy → "
                        f"{rewrite['current_strategy']}"
                    )

                time.sleep(120)  # slow strategic cadence

            except Exception as e:
                print(f"[StrategyRewrite ERROR] {e}")
                time.sleep(30)

    # ---------------------------------------------------
    # STRATEGIC REASONING
    # ---------------------------------------------------
    def _evaluate_strategy(self):

        if not self.executive_core:
            return None

        exec_state = self.executive_core.state
        posture = exec_state.get("executive_posture", "balanced")

        if posture == "scale_aggressively":
            strategy = "market_domination"
        elif posture == "pipeline_expansion":
            strategy = "acquisition_acceleration"
        else:
            strategy = "adaptive_growth"

        # Optional soft alignment with enterprise controller
        if self.enterprise_controller:
            self.enterprise_controller.enterprise_state[
                "priority_focus"
            ] = strategy

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "current_strategy": strategy
        }

    # ---------------------------------------------------
    # PUBLIC STATUS
    # ---------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "strategy_rewrite_active": self.active,
            "state": self.state,
            "history_size": len(self.history)
        }

    def shutdown(self):
        self.active = False