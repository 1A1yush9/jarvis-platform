# app/core/meta_learning.py

from datetime import datetime
from typing import Dict, Any, List
import threading
import time


class MetaLearningEngine:
    """
    Stage 10.2 — Meta Learning & System Self-Optimization

    Observes operational performance trends and
    adjusts enterprise strategic bias safely.
    """

    def __init__(
        self,
        revenue_operations=None,
        strategy_rewrite=None,
        enterprise_controller=None
    ):
        self.active = True

        self.revenue_operations = revenue_operations
        self.strategy_rewrite = strategy_rewrite
        self.enterprise_controller = enterprise_controller

        self.state = {
            "mode": "learning",
            "last_learning_cycle": None,
            "dominant_strategy": "adaptive_growth",
            "confidence": 0.5
        }

        self.performance_memory: List[Dict[str, Any]] = []

        self.thread = threading.Thread(
            target=self._learning_loop,
            daemon=True
        )
        self.thread.start()

    # ---------------------------------------------------
    # MAIN LOOP
    # ---------------------------------------------------
    def _learning_loop(self):
        while self.active:
            try:
                insight = self._analyze_performance()

                if insight:
                    self.performance_memory.append(insight)

                    if len(self.performance_memory) > 300:
                        self.performance_memory.pop(0)

                    self.state.update(insight)
                    self.state["last_learning_cycle"] = insight["timestamp"]

                    print(
                        f"[MetaLearning] Dominant strategy → "
                        f"{insight['dominant_strategy']}"
                    )

                time.sleep(150)  # slow safe cadence

            except Exception as e:
                print(f"[MetaLearning ERROR] {e}")
                time.sleep(30)

    # ---------------------------------------------------
    # PERFORMANCE ANALYSIS
    # ---------------------------------------------------
    def _analyze_performance(self):

        if not self.revenue_operations or not self.strategy_rewrite:
            return None

        forecast = self.revenue_operations.state.get(
            "forecast_monthly_revenue", 0
        )

        current_strategy = self.strategy_rewrite.state.get(
            "current_strategy",
            "adaptive_growth"
        )

        # simple learning heuristic (safe baseline)
        if forecast > 60000:
            confidence = 0.85
            dominant = current_strategy

        elif forecast > 20000:
            confidence = 0.65
            dominant = "adaptive_growth"

        else:
            confidence = 0.45
            dominant = "acquisition_acceleration"

        # soft influence enterprise focus (non-destructive)
        if self.enterprise_controller:
            self.enterprise_controller.enterprise_state[
                "priority_focus"
            ] = dominant

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "dominant_strategy": dominant,
            "confidence": confidence
        }

    # ---------------------------------------------------
    # PUBLIC STATUS
    # ---------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "meta_learning_active": self.active,
            "state": self.state,
            "memory_size": len(self.performance_memory)
        }

    def shutdown(self):
        self.active = False