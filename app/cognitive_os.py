# app/cognitive_os.py

import time
from typing import Dict


class CognitiveBusinessOS:
    """
    Stage-7.0 Cognitive Business Operating System
    Central decision coordinator for Jarvis.
    """

    def __init__(self):
        self.system_focus = "initializing"
        self.last_cycle = 0
        self.history = []

    # -----------------------------------
    # Cognitive Evaluation Cycle
    # -----------------------------------
    def run_cycle(self, opportunity_snapshot: dict,
                  execution_snapshot: dict,
                  revenue_snapshot: dict):

        focus = self._decide_focus(
            opportunity_snapshot,
            execution_snapshot,
            revenue_snapshot
        )

        self.system_focus = focus
        self.last_cycle = time.time()

        record = {
            "focus": focus,
            "time": self.last_cycle
        }

        self.history.append(record)
        return record

    # -----------------------------------
    # Decision Logic
    # -----------------------------------
    def _decide_focus(self, opp, execs, revenue):

        opportunities = opp.get("total_opportunities", 0)
        actions = execs.get("total_actions", 0)
        total_revenue = revenue.get("tracked_revenue", 0)

        if total_revenue > 0 and actions > opportunities:
            return "optimization_mode"

        if opportunities > actions:
            return "growth_mode"

        if actions > 10:
            return "execution_mode"

        return "exploration_mode"

    # -----------------------------------
    def snapshot(self):
        return {
            "engine": "Cognitive Business OS",
            "current_focus": self.system_focus,
            "last_cycle": self.last_cycle,
            "cycles_run": len(self.history)
        }