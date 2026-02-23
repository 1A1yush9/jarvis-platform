# app/revenue_engine.py

import time
from typing import Dict, List


class RevenueOptimizationEngine:
    """
    Stage-6.5
    Learns from execution outcomes and optimizes future strategy bias.
    """

    def __init__(self):
        self.client_revenue_log: Dict[str, List[dict]] = {}
        self.strategy_performance: Dict[str, dict] = {}

    # -----------------------------------
    # Record Revenue Outcome
    # -----------------------------------
    def record_outcome(self, client_id: str, action: dict, revenue: float):

        record = {
            "action_id": action["action_id"],
            "strategy": action["strategy"],
            "revenue": revenue,
            "timestamp": time.time()
        }

        self.client_revenue_log.setdefault(client_id, []).append(record)

        self._update_strategy_learning(action["strategy"], revenue)

        return record

    # -----------------------------------
    # Learning Model
    # -----------------------------------
    def _update_strategy_learning(self, strategy: str, revenue: float):

        stats = self.strategy_performance.setdefault(
            strategy,
            {"uses": 0, "total_revenue": 0}
        )

        stats["uses"] += 1
        stats["total_revenue"] += revenue

    # -----------------------------------
    # Strategy Score
    # -----------------------------------
    def strategy_score(self, strategy: str):

        stats = self.strategy_performance.get(strategy)

        if not stats or stats["uses"] == 0:
            return 0

        return round(stats["total_revenue"] / stats["uses"], 2)

    # -----------------------------------
    # Client Data
    # -----------------------------------
    def get_client_revenue(self, client_id: str):
        return self.client_revenue_log.get(client_id, [])

    # -----------------------------------
    # System Snapshot
    # -----------------------------------
    def system_snapshot(self):

        total_revenue = sum(
            r["revenue"]
            for records in self.client_revenue_log.values()
            for r in records
        )

        return {
            "engine": "Revenue Optimization Intelligence",
            "total_clients": len(self.client_revenue_log),
            "strategies_learned": len(self.strategy_performance),
            "tracked_revenue": round(total_revenue, 2)
        }