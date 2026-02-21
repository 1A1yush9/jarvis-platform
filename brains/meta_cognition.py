# brains/meta_cognition.py

import time


class MetaCognition:
    """
    Self-observation layer.
    Evaluates stability of internal cognitive states.
    No execution authority.
    """

    def __init__(self):
        self.started = time.time()

    def reflect(self, awareness_report, strategy_report):

        awareness = awareness_report.get("awareness_state", "unknown")
        trajectory = strategy_report.get("projected_trajectory", "unknown")

        stability = "stable"
        confidence = "medium"

        if awareness == "calm_idle":
            confidence = "high"

        elif awareness == "high_activity":
            stability = "dynamic"
            confidence = "moderate"

        if trajectory == "risk_watch_phase":
            stability = "cautious"
            confidence = "low"

        return {
            "meta_mode": "self_observation",
            "cognitive_stability": stability,
            "confidence_level": confidence,
            "awareness_reference": awareness,
            "trajectory_reference": trajectory,
            "uptime": round(time.time() - self.started, 2)
        }


meta_cognition = MetaCognition()