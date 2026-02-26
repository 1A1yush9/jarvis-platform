"""
Jarvis Platform — Stage 20.5
Continuous Intelligence Cycle

Runs a safe advisory monitoring loop inside API runtime.

SAFE MODE:
- No execution authority
- Low-frequency monitoring
- Read-only intelligence evaluation
"""

import asyncio
from datetime import datetime
from typing import Dict, Any


class ContinuousIntelligenceCycle:
    def __init__(self, insight_engine, predictive_engine):
        self.engine_name = "Continuous Intelligence Cycle"
        self.version = "20.5"
        self.mode = "advisory_only"

        self.insight_engine = insight_engine
        self.predictive_engine = predictive_engine

        self.latest_state: Dict[str, Any] = {
            "last_run": None,
            "insights": None,
            "forecast": None,
        }

        self.running = False

    # -----------------------------------------------------
    # Background Loop
    # -----------------------------------------------------
    async def start_cycle(self, interval_seconds: int = 120):
        if self.running:
            return

        self.running = True

        while True:
            try:
                insights = self.insight_engine.generate_insights()
                forecast = self.predictive_engine.forecast()

                self.latest_state = {
                    "last_run": datetime.utcnow().isoformat(),
                    "insights": insights,
                    "forecast": forecast,
                }

            except Exception as e:
                self.latest_state["error"] = str(e)

            await asyncio.sleep(interval_seconds)

    # -----------------------------------------------------
    # State Access
    # -----------------------------------------------------
    def get_state(self):
        return {
            "engine": self.engine_name,
            "version": self.version,
            "mode": self.mode,
            "state": self.latest_state,
        }

    def status(self):
        return {
            "engine": self.engine_name,
            "version": self.version,
            "running": self.running,
            "mode": self.mode,
        }