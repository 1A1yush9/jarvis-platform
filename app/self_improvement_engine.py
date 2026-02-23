# app/self_improvement_engine.py

import time
from typing import Dict


class SelfImprovementEngine:
    """
    Stage-7.2
    Learns which cognitive focus modes produce results
    and biases future decisions.
    """

    def __init__(self):
        self.focus_performance: Dict[str, dict] = {}
        self.last_revenue_snapshot = 0

    # -----------------------------------
    def record_cycle_result(self, focus: str, revenue_snapshot: dict):

        total_revenue = revenue_snapshot.get("tracked_revenue", 0)
        revenue_delta = total_revenue - self.last_revenue_snapshot
        self.last_revenue_snapshot = total_revenue

        stats = self.focus_performance.setdefault(
            focus,
            {"cycles": 0, "revenue_generated": 0}
        )

        stats["cycles"] += 1
        stats["revenue_generated"] += max(revenue_delta, 0)

        return {
            "focus": focus,
            "revenue_delta": revenue_delta
        }

    # -----------------------------------
    def focus_score(self, focus: str):

        stats = self.focus_performance.get(focus)
        if not stats or stats["cycles"] == 0:
            return 0

        return round(stats["revenue_generated"] / stats["cycles"], 2)

    # -----------------------------------
    def bias_map(self):
        return {
            focus: self.focus_score(focus)
            for focus in self.focus_performance
        }

    # -----------------------------------
    def snapshot(self):
        return {
            "engine": "Continuous Self-Improvement",
            "focus_modes_tracked": len(self.focus_performance),
            "learning_state": self.focus_performance
        }