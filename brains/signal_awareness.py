# jarvis/brains/signal_awareness.py

import time
from collections import deque


class SignalAwareness:
    """
    Passive signal monitoring.
    Observes requests and internal events only.
    NO execution authority.
    """

    def __init__(self):
        self.start_time = time.time()
        self.request_log = deque(maxlen=100)
        self.event_log = deque(maxlen=100)

    # -----------------------------
    # Observe HTTP Requests
    # -----------------------------
    def observe_request(self, path: str, method: str):
        self.request_log.append({
            "timestamp": time.time(),
            "path": path,
            "method": method
        })

    # -----------------------------
    # Observe Internal Events
    # -----------------------------
    def observe_event(self, name: str, metadata=None):
        self.event_log.append({
            "timestamp": time.time(),
            "event": name,
            "metadata": metadata or {}
        })

    # -----------------------------
    # Report Signals
    # -----------------------------
    def report(self):
        uptime = round(time.time() - self.start_time, 2)

        return {
            "status": "passive_monitoring",
            "uptime_seconds": uptime,
            "recent_requests": list(self.request_log),
            "recent_events": list(self.event_log)
        }


# Safe global instance
signal_awareness = SignalAwareness()