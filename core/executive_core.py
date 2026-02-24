# app/core/executive_core.py

from datetime import datetime
from typing import Dict, Any, List
import threading
import time


class ExecutiveDecisionCore:
    """
    Stage 10.0 — Executive Decision Core

    Cross-layer reasoning engine that evaluates
    enterprise-wide intelligence signals and
    determines global operational posture.
    """

    def __init__(
        self,
        enterprise_controller=None,
        revenue_operations=None,
        revenue_command=None
    ):
        self.active = True

        self.enterprise_controller = enterprise_controller
        self.revenue_operations = revenue_operations
        self.revenue_command = revenue_command

        self.state = {
            "mode": "executive_monitoring",
            "last_decision": None,
            "executive_posture": "balanced",
            "global_priority": "growth_alignment"
        }

        self.history: List[Dict[str, Any]] = []

        self.thread = threading.Thread(
            target=self._executive_loop,
            daemon=True
        )
        self.thread.start()

    # ---------------------------------------------------
    # MAIN LOOP
    # ---------------------------------------------------
    def _executive_loop(self):
        while self.active:
            try:
                decision = self._evaluate_enterprise()

                if decision:
                    self.history.append(decision)

                    if len(self.history) > 200:
                        self.history.pop(0)

                    self.state.update(decision)
                    self.state["last_decision"] = decision["timestamp"]

                    print(
                        f"[ExecutiveCore] Posture → {decision['executive_posture']}"
                    )

                time.sleep(75)  # slow, safe executive cadence

            except Exception as e:
                print(f"[ExecutiveCore ERROR] {e}")
                time.sleep(20)

    # ---------------------------------------------------
    # EXECUTIVE REASONING
    # ---------------------------------------------------
    def _evaluate_enterprise(self):

        if not self.revenue_operations:
            return None

        ops_state = self.revenue_operations.state

        forecast = ops_state.get("forecast_monthly_revenue", 0)
        pressure = ops_state.get("execution_pressure", "normal")

        if forecast > 60000 and pressure == "scale_execution":
            posture = "scale_aggressively"
            priority = "execution_expansion"

        elif forecast < 10000:
            posture = "pipeline_expansion"
            priority = "market_capture"

        else:
            posture = "balanced_growth"
            priority = "optimization"

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "executive_posture": posture,
            "global_priority": priority
        }

    # ---------------------------------------------------
    # PUBLIC STATUS
    # ---------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "executive_core_active": self.active,
            "state": self.state,
            "history_size": len(self.history)
        }

    def shutdown(self):
        self.active = False