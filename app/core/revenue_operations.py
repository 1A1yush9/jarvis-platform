# app/core/revenue_operations.py

from datetime import datetime
from typing import Dict, Any, List
import threading
import time


class RevenueOperationsBrain:
    """
    Stage 9.5 — Autonomous Revenue Operations Brain

    Evaluates proposal pipeline and generates
    revenue forecasts and operational signals.
    """

    def __init__(self, proposal_engine=None):
        self.active = True
        self.proposal_engine = proposal_engine

        self.state = {
            "mode": "analysis",
            "last_evaluation": None,
            "pipeline_value": 0,
            "forecast_monthly_revenue": 0,
            "growth_velocity": "stable",
            "execution_pressure": "normal"
        }

        self.history: List[Dict[str, Any]] = []

        self.thread = threading.Thread(
            target=self._operations_loop,
            daemon=True
        )
        self.thread.start()

    # ---------------------------------------------------
    # MAIN LOOP
    # ---------------------------------------------------
    def _operations_loop(self):
        while self.active:
            try:
                report = self._evaluate_pipeline()

                if report:
                    self.history.append(report)

                    if len(self.history) > 150:
                        self.history.pop(0)

                    self.state.update(report)
                    self.state["last_evaluation"] = report["timestamp"]

                    print(
                        f"[RevenueOps] Forecast updated → "
                        f"{report['forecast_monthly_revenue']}"
                    )

                time.sleep(60)  # Render-safe interval

            except Exception as e:
                print(f"[RevenueOps ERROR] {e}")
                time.sleep(20)

    # ---------------------------------------------------
    # PIPELINE ANALYSIS
    # ---------------------------------------------------
    def _evaluate_pipeline(self):

        if not self.proposal_engine:
            return None

        proposals = self.proposal_engine.proposal_pipeline

        if not proposals:
            return None

        total_value = sum(p["estimated_value"] for p in proposals)

        avg_win_prob = (
            sum(p["win_probability"] for p in proposals) / len(proposals)
        )

        forecast = int(total_value * (avg_win_prob / 100) / 6)

        if forecast > 50000:
            velocity = "high_growth"
            pressure = "scale_execution"
        elif forecast > 15000:
            velocity = "moderate_growth"
            pressure = "balanced"
        else:
            velocity = "early_stage"
            pressure = "pipeline_building"

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "pipeline_value": total_value,
            "forecast_monthly_revenue": forecast,
            "growth_velocity": velocity,
            "execution_pressure": pressure
        }

    # ---------------------------------------------------
    # PUBLIC STATUS
    # ---------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "revenue_operations_active": self.active,
            "state": self.state,
            "history_size": len(self.history)
        }

    def shutdown(self):
        self.active = False