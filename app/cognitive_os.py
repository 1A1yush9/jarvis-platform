# app/cognitive_os.py

import time


class CognitiveBusinessOS:

    def __init__(self):
        self.system_focus = "initializing"
        self.last_cycle = 0
        self.history = []

    # -----------------------------------
    def run_cycle(
        self,
        opportunity_snapshot,
        execution_snapshot,
        revenue_snapshot,
        local_bias=None,
        consensus_bias=None
    ):

        focus = self._decide_focus(
            opportunity_snapshot,
            execution_snapshot,
            revenue_snapshot,
            local_bias or {},
            consensus_bias or {}
        )

        self.system_focus = focus
        self.last_cycle = time.time()

        record = {"focus": focus, "time": self.last_cycle}
        self.history.append(record)

        return record

    # -----------------------------------
    def _decide_focus(
        self,
        opp,
        execs,
        revenue,
        local_bias,
        consensus_bias
    ):

        opportunities = opp.get("total_opportunities", 0)
        actions = execs.get("total_actions", 0)
        total_revenue = revenue.get("tracked_revenue", 0)

        base_focus = "exploration_mode"

        if total_revenue > 0 and actions > opportunities:
            base_focus = "optimization_mode"
        elif opportunities > actions:
            base_focus = "growth_mode"
        elif actions > 10:
            base_focus = "execution_mode"

        combined_bias = {}

        for k, v in (local_bias or {}).items():
            combined_bias[k] = combined_bias.get(k, 0) + v

        for k, v in (consensus_bias or {}).items():
            combined_bias[k] = combined_bias.get(k, 0) + v * 0.5

        if combined_bias:
            best_focus = max(combined_bias, key=combined_bias.get)
            if combined_bias.get(best_focus, 0) > 0:
                return best_focus

        return base_focus

    # -----------------------------------
    def snapshot(self):
        return {
            "engine": "Cognitive Business OS",
            "current_focus": self.system_focus,
            "last_cycle": self.last_cycle,
            "cycles_run": len(self.history)
        }