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
        bias_map=None
    ):

        focus = self._decide_focus(
            opportunity_snapshot,
            execution_snapshot,
            revenue_snapshot,
            bias_map or {}
        )

        self.system_focus = focus
        self.last_cycle = time.time()

        record = {"focus": focus, "time": self.last_cycle}
        self.history.append(record)

        return record

    # -----------------------------------
    def _decide_focus(self, opp, execs, revenue, bias):

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

        # Apply learning bias
        if bias:
            best_focus = max(bias, key=bias.get, default=base_focus)
            if bias.get(best_focus, 0) > 0:
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