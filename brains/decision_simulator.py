# brains/decision_simulator.py

import time


class DecisionSimulator:
    """
    Simulates possible decisions based on awareness.
    Produces suggestions only.
    No execution authority.
    """

    def __init__(self):
        self.started = time.time()

    def simulate(self, awareness_report: dict, guardian_report: dict):

        awareness = awareness_report.get("awareness_state", "calm_idle")
        guardian = guardian_report.get("guardian_status", "stable")

        suggestion = "no_action"

        if guardian != "stable":
            suggestion = "monitor_system"

        elif awareness == "high_activity":
            suggestion = "prepare_scaling"

        elif awareness == "active_usage":
            suggestion = "optimize_observation"

        elif awareness == "calm_idle":
            suggestion = "maintain_idle_state"

        return {
            "simulation_mode": "sandbox",
            "suggested_action": suggestion,
            "awareness_state": awareness,
            "guardian_state": guardian,
            "uptime": round(time.time() - self.started, 2)
        }


decision_simulator = DecisionSimulator()