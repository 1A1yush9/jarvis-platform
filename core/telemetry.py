# core/telemetry.py

"""
Stage-15.4 — Intelligence Telemetry
Tracks runtime health metrics.
Render-safe (in-memory).
"""

from datetime import datetime
from typing import Dict, Any
import time


class Telemetry:

    def __init__(self):
        self.start_time = time.time()
        self.total_requests = 0
        self.total_errors = 0
        self.last_latency = 0.0

    # ----------------------------------------------
    # Request Start
    # ----------------------------------------------
    def start_timer(self):
        return time.time()

    # ----------------------------------------------
    # Request End
    # ----------------------------------------------
    def end_timer(self, start_time: float):
        self.last_latency = round(time.time() - start_time, 4)
        self.total_requests += 1

    # ----------------------------------------------
    # Error Tracking
    # ----------------------------------------------
    def record_error(self):
        self.total_errors += 1

    # ----------------------------------------------
    # System Status
    # ----------------------------------------------
    def status(self) -> Dict[str, Any]:

        uptime = round(time.time() - self.start_time, 2)

        return {
            "uptime_seconds": uptime,
            "total_requests": self.total_requests,
            "total_errors": self.total_errors,
            "last_latency_seconds": self.last_latency,
            "timestamp": datetime.utcnow().isoformat()
        }