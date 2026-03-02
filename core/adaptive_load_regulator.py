"""
Jarvis Platform — Stage 55.0
Adaptive Load & Cognitive Pressure Regulator

Purpose:
Prevent cognitive overload and maintain stability
during traffic spikes or reasoning saturation.
Advisory-only regulation.
"""

from datetime import datetime
from typing import Dict, Any, List
import time


class AdaptiveLoadRegulator:
    """
    Observes request velocity and regulates reasoning pressure.
    """

    WINDOW_SECONDS = 10
    MAX_REQUESTS_PER_WINDOW = 25

    def __init__(self, decision_trace=None):
        self.decision_trace = decision_trace
        self.request_times: List[float] = []
        self.pressure_state = "NORMAL"

    # --------------------------------------------------

    def regulate(self, signal: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluate load pressure before reasoning.
        """

        now = time.time()
        self.request_times.append(now)

        # remove old timestamps
        self.request_times = [
            t for t in self.request_times
            if now - t <= self.WINDOW_SECONDS
        ]

        rate = len(self.request_times)

        if rate > self.MAX_REQUESTS_PER_WINDOW:
            self.pressure_state = "HIGH_PRESSURE"
            signal["cognitive_pressure"] = {
                "state": "HIGH",
                "regulated": True,
                "timestamp": datetime.utcnow().isoformat(),
            }
            self._record("HIGH_PRESSURE", rate)
        else:
            self.pressure_state = "NORMAL"
            signal["cognitive_pressure"] = {
                "state": "NORMAL",
                "regulated": False,
                "timestamp": datetime.utcnow().isoformat(),
            }

        return signal

    # --------------------------------------------------

    def _record(self, state: str, rate: int) -> None:
        if self.decision_trace:
            self.decision_trace.record({
                "timestamp": datetime.utcnow().isoformat(),
                "event": "COGNITIVE_PRESSURE_STATE",
                "detail": f"{state} rate={rate}",
                "layer": "AdaptiveLoadRegulator",
            })