# app/core/execution_interface.py

from datetime import datetime
from typing import Dict, Any, List
import threading
import time
import random


class ExecutionInterface:
    """
    Stage 11.0 — Autonomous Business Execution Interface

    Converts proposal blueprints into structured
    execution-ready operational plans.
    """

    def __init__(self, proposal_engine=None):
        self.active = True
        self.proposal_engine = proposal_engine

        self.state = {
            "mode": "execution_planning",
            "last_plan_generated": None,
            "active_department": None
        }

        self.execution_queue: List[Dict[str, Any]] = []
        self.history: List[Dict[str, Any]] = []

        self.thread = threading.Thread(
            target=self._execution_loop,
            daemon=True
        )
        self.thread.start()

    # ---------------------------------------------------
    # MAIN LOOP
    # ---------------------------------------------------
    def _execution_loop(self):
        while self.active:
            try:
                plan = self._generate_execution_plan()

                if plan:
                    self.execution_queue.append(plan)
                    self.history.append(plan)

                    if len(self.history) > 200:
                        self.history.pop(0)

                    self.state["last_plan_generated"] = plan["timestamp"]

                    print(
                        f"[ExecutionInterface] Plan → {plan['execution_focus']}"
                    )

                time.sleep(70)  # safe pacing

            except Exception as e:
                print(f"[ExecutionInterface ERROR] {e}")
                time.sleep(20)

    # ---------------------------------------------------
    # PLAN CREATION
    # ---------------------------------------------------
    def _generate_execution_plan(self):

        if not self.proposal_engine:
            return None

        if not self.proposal_engine.proposal_pipeline:
            return None

        proposal = random.choice(
            self.proposal_engine.proposal_pipeline
        )

        departments = [
            "marketing",
            "seo",
            "paid_ads",
            "content",
            "conversion_optimization"
        ]

        plan = {
            "timestamp": datetime.utcnow().isoformat(),
            "industry": proposal["industry"],
            "geo_target": proposal["geo_target"],
            "execution_focus": proposal["offer_type"],
            "department": random.choice(departments),
            "priority": random.randint(70, 95),
            "estimated_value": proposal["estimated_value"],
            "source": "Execution Interface"
        }

        self.state["active_department"] = plan["department"]

        return plan

    # ---------------------------------------------------
    # PUBLIC STATUS
    # ---------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "execution_interface_active": self.active,
            "state": self.state,
            "execution_queue_size": len(self.execution_queue),
            "history_size": len(self.history)
        }

    def shutdown(self):
        self.active = False