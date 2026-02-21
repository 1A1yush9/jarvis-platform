# brains/pattern_observer.py

import time


class PatternObserver:
    """
    Passive analytics layer.
    Reads memory snapshots and extracts usage patterns.
    No execution authority.
    """

    def __init__(self):
        self.started = time.time()

    def analyze(self, memory_snapshots):

        endpoint_frequency = {}
        total_requests = 0

        for snap in memory_snapshots:
            signals = snap.get("signals", {})
            requests = signals.get("recent_requests", [])

            for req in requests:
                path = req.get("path", "unknown")
                endpoint_frequency[path] = (
                    endpoint_frequency.get(path, 0) + 1
                )
                total_requests += 1

        return {
            "analysis_mode": "passive",
            "total_observed_requests": total_requests,
            "endpoint_frequency": endpoint_frequency,
            "observer_uptime": round(time.time() - self.started, 2),
        }


pattern_observer = PatternObserver()