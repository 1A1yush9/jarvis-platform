# brains/intent_classifier.py

import time


class IntentClassifier:
    """
    Passive intent labeling layer.
    Converts observed patterns into simple system intents.
    No execution authority.
    """

    def __init__(self):
        self.started = time.time()

    def classify(self, pattern_report: dict):

        freq = pattern_report.get("endpoint_frequency", {})
        total = pattern_report.get("total_observed_requests", 0)

        intent = "idle"

        if total == 0:
            intent = "idle"

        elif "/health" in freq and freq["/health"] > total * 0.6:
            intent = "monitoring_activity"

        elif len(freq.keys()) > 3:
            intent = "exploration_activity"

        else:
            intent = "normal_usage"

        return {
            "intent_state": intent,
            "observed_requests": total,
            "classifier_mode": "passive",
            "uptime": round(time.time() - self.started, 2)
        }


intent_classifier = IntentClassifier()