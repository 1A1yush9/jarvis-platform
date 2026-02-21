# brains/stability_guardian.py

import time


class StabilityGuardian:
    """
    Passive system stability monitor.
    Detects risk indicators but takes NO action.
    """

    def __init__(self):
        self.started = time.time()

    def evaluate(self, memory_report: dict, pattern_report: dict):

        memory_size = memory_report.get("memory_size", 0)
        total_requests = pattern_report.get("total_observed_requests", 0)

        status = "stable"
        warnings = []

        # memory growth check
        if memory_size > 40:
            status = "watch"
            warnings.append("memory_buffer_near_capacity")

        # traffic spike check
        if total_requests > 200:
            status = "watch"
            warnings.append("high_request_volume")

        # inactivity check
        if total_requests == 0:
            warnings.append("idle_system")

        return {
            "guardian_status": status,
            "warnings": warnings,
            "mode": "passive_monitoring",
            "uptime": round(time.time() - self.started, 2)
        }


stability_guardian = StabilityGuardian()