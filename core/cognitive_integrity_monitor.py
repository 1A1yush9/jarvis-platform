"""
Jarvis Platform — Stage 52.0
Cognitive Integrity & Drift Detection System

Purpose:
Detect long-term reasoning drift without modifying cognition.
Audit-only supervisory layer.
"""

from datetime import datetime
from typing import Dict, Any, List
import hashlib
import json


class CognitiveIntegrityMonitor:
    """
    Observes reasoning consistency across cycles.
    """

    HISTORY_LIMIT = 25

    def __init__(self, decision_trace=None):
        self.decision_trace = decision_trace
        self.reasoning_history: List[str] = []
        self.last_integrity_state = "STABLE"

    # --------------------------------------------------

    def evaluate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Passive drift evaluation.
        """

        fingerprint = self._generate_fingerprint(payload)
        self._update_history(fingerprint)

        drift_detected = self._detect_drift()

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "history_size": len(self.reasoning_history),
            "drift_detected": drift_detected,
            "integrity_state": "DRIFT_ALERT" if drift_detected else "STABLE",
        }

        self.last_integrity_state = report["integrity_state"]

        self._record(report)

        payload["cognitive_integrity"] = report
        return payload

    # --------------------------------------------------

    def _generate_fingerprint(self, payload: Dict[str, Any]) -> str:
        """
        Create stable structural hash of reasoning output.
        """

        normalized = json.dumps(payload, sort_keys=True, default=str)
        return hashlib.sha256(normalized.encode()).hexdigest()

    # --------------------------------------------------

    def _update_history(self, fingerprint: str) -> None:
        self.reasoning_history.append(fingerprint)

        if len(self.reasoning_history) > self.HISTORY_LIMIT:
            self.reasoning_history.pop(0)

    # --------------------------------------------------

    def _detect_drift(self) -> bool:
        """
        Drift heuristic:
        excessive uniqueness across recent reasoning cycles.
        """

        if len(self.reasoning_history) < 5:
            return False

        unique_ratio = len(set(self.reasoning_history)) / len(self.reasoning_history)

        # If almost every cycle differs structurally → drift suspicion
        return unique_ratio > 0.9

    # --------------------------------------------------

    def _record(self, report: Dict[str, Any]) -> None:
        if self.decision_trace:
            self.decision_trace.record({
                "timestamp": report["timestamp"],
                "event": "COGNITIVE_INTEGRITY_CHECK",
                "detail": report["integrity_state"],
                "layer": "CognitiveIntegrityMonitor",
            })