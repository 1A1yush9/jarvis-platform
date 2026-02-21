# brains/adaptive_awareness.py

import time


class AdaptiveAwareness:
    """
    Passive awareness layer.
    Converts intent into overall system awareness state.
    No decisions or actions allowed.
    """

    def __init__(self):
        self.started = time.time()

    def evaluate(self, intent_report: dict):

        intent = intent_report.get("intent_state", "idle")
        observed = intent_report.get("observed_requests", 0)

        awareness = "calm_idle"

        if intent == "monitoring_activity":
            awareness = "monitored"

        elif intent == "normal_usage":
            awareness = "active_usage"

        elif intent == "exploration_activity":
            awareness = "high_activity"

        if observed == 0:
            awareness = "calm_idle"

        return {
            "awareness_state": awareness,
            "source_intent": intent,
            "awareness_mode": "passive",
            "uptime": round(time.time() - self.started, 2)
        }


adaptive_awareness = AdaptiveAwareness()