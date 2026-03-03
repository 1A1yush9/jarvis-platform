"""
Jarvis Platform — Stage-78.0
Deterministic Governance Latency & Timing Integrity Monitor

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Monitors governance evaluation timing to detect latency anomalies
and timing-based instability risks.

This module:
- Tracks evaluation duration
- Detects abnormal latency variance
- Identifies sustained timing drift
- Emits advisory-only timing integrity signals
- Never alters execution flow

Design Guarantees:
------------------
- Deterministic thresholds
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
import time
from collections import deque
from typing import Dict, Any


class GovernanceLatencyMonitor:
    """
    Stage-78.0 Timing Integrity Layer

    Protects against:
    - Latency spikes
    - Sustained timing drift
    - Performance degradation patterns
    """

    VERSION = "78.0"

    WINDOW_SIZE = 50
    SPIKE_THRESHOLD_MULTIPLIER = 3.0
    DRIFT_VARIANCE_THRESHOLD = 0.002  # seconds variance threshold

    def __init__(self):
        self._lock = threading.Lock()
        self._latencies = deque(maxlen=self.WINDOW_SIZE)
        self._last_start_time = None
        self._timing_violation = False
        self._last_report = None

    # ------------------------------------------------------------------
    # Public Timing Hooks
    # ------------------------------------------------------------------

    def start_timing(self):
        with self._lock:
            self._last_start_time = time.perf_counter()

    def end_timing(self) -> Dict[str, Any]:
        with self._lock:
            if self._last_start_time is None:
                return self._neutral_report()

            duration = time.perf_counter() - self._last_start_time
            self._latencies.append(duration)

            spike_detected = self._detect_spike(duration)
            drift_detected = self._detect_variance_drift()

            containment_reason = self._evaluate_timing(
                spike_detected,
                drift_detected
            )

            report = {
                "latency_monitor_version": self.VERSION,
                "latest_duration": round(duration, 6),
                "average_latency": round(self._average_latency(), 6),
                "spike_detected": spike_detected,
                "drift_detected": drift_detected,
                "timing_violation": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._timing_violation = containment_reason is not None
            self._last_report = report
            self._last_start_time = None

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _average_latency(self) -> float:
        if not self._latencies:
            return 0.0
        return sum(self._latencies) / len(self._latencies)

    def _detect_spike(self, duration: float) -> bool:
        avg = self._average_latency()
        if avg == 0:
            return False
        return duration > avg * self.SPIKE_THRESHOLD_MULTIPLIER

    def _detect_variance_drift(self) -> bool:
        if len(self._latencies) < 5:
            return False

        avg = self._average_latency()
        variance = sum((x - avg) ** 2 for x in self._latencies) / len(self._latencies)

        return variance > self.DRIFT_VARIANCE_THRESHOLD

    def _evaluate_timing(self, spike: bool, drift: bool) -> str | None:
        if spike:
            return "LATENCY_SPIKE_DETECTED"
        if drift:
            return "TIMING_VARIANCE_DRIFT_DETECTED"
        return None

    def _recommended_action(self, reason: str | None) -> str:
        if reason == "LATENCY_SPIKE_DETECTED":
            return "INVESTIGATE_RUNTIME_LOAD_CONDITIONS"
        if reason == "TIMING_VARIANCE_DRIFT_DETECTED":
            return "MONITOR_PERFORMANCE_STABILITY"
        return "PROCEED"

    def _neutral_report(self) -> Dict[str, Any]:
        return {
            "latency_monitor_version": self.VERSION,
            "latest_duration": None,
            "average_latency": None,
            "spike_detected": False,
            "drift_detected": False,
            "timing_violation": False,
            "containment_reason": None,
            "advisory_action": "PROCEED"
        }

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "latency_monitor_version": self.VERSION,
            "average_latency": round(self._average_latency(), 6),
            "timing_violation": self._timing_violation,
            "window_size": len(self._latencies),
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_governance_latency_monitor() -> GovernanceLatencyMonitor:
    """
    Backward compatible instantiation.
    """
    return GovernanceLatencyMonitor()