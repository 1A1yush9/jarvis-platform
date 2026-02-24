# app/core/autopilot_brain.py

from datetime import datetime, timedelta
from typing import Dict, Any, List
import json
import os
import logging
import uuid

logger = logging.getLogger(__name__)


class AutoPilotBrain:
    """
    Controlled autonomous workflow launcher.
    """

    STATE_PATH = "app/memory/autopilot_state.json"

    MAX_DAILY_RUNS = 3
    CONFIDENCE_THRESHOLD = 0.7
    COOLDOWN_MINUTES = 30

    def __init__(self):
        self._ensure_state()

    # -------------------------------------------------
    # STATE MANAGEMENT
    # -------------------------------------------------
    def _ensure_state(self):
        os.makedirs("app/memory", exist_ok=True)

        if not os.path.exists(self.STATE_PATH):
            with open(self.STATE_PATH, "w") as f:
                json.dump(
                    {
                        "enabled": True,
                        "last_run": None,
                        "runs_today": 0,
                        "day": datetime.utcnow().date().isoformat(),
                    },
                    f,
                )

    def _load(self):
        with open(self.STATE_PATH, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.STATE_PATH, "w") as f:
            json.dump(data, f, indent=2)

    # -------------------------------------------------
    # MAIN DECISION
    # -------------------------------------------------
    def evaluate_autopilot(
        self,
        growth_report: Dict[str, Any]
    ) -> List[Dict[str, Any]]:

        state = self._load()

        if not state.get("enabled", False):
            return []

        today = datetime.utcnow().date().isoformat()

        # reset counter daily
        if state["day"] != today:
            state["runs_today"] = 0
            state["day"] = today

        # daily limit
        if state["runs_today"] >= self.MAX_DAILY_RUNS:
            return []

        # cooldown check
        if state["last_run"]:
            last = datetime.fromisoformat(state["last_run"])
            if datetime.utcnow() - last < timedelta(
                minutes=self.COOLDOWN_MINUTES
            ):
                return []

        opportunities = growth_report.get("opportunities", [])

        launches = []

        for opp in opportunities:
            if opp["confidence"] < self.CONFIDENCE_THRESHOLD:
                continue

            launches.append({
                "job_id": str(uuid.uuid4()),
                "industry": opp["industry"],
                "objective": opp["recommended_funnel"],
                "auto_generated": True,
            })

        if launches:
            state["runs_today"] += len(launches)
            state["last_run"] = datetime.utcnow().isoformat()
            self._save(state)

        return launches
