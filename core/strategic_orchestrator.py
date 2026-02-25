# core/strategic_orchestrator.py

"""
Stage-15.0 — Strategic Intelligence Orchestrator

Purpose:
Unifies all cognitive layer outputs into a single
strategic intelligence report.

Advisory cognition only.
No execution authority.
"""

from typing import Dict, Any


class StrategicIntelligenceOrchestrator:

    def __init__(self):
        self.version = "15.0"
        self.mode = "advisory"

    # --------------------------------------------------
    # Strategic State Evaluation
    # --------------------------------------------------
    def _determine_state(
        self,
        awareness: Dict[str, Any],
        calibration: Dict[str, Any]
    ) -> str:

        confidence = awareness.get("confidence_score", 0)
        stability = calibration.get("stability_state", "UNKNOWN")
        risks = awareness.get("risk_flags", [])

        if confidence >= 0.75 and stability == "HIGH" and not risks:
            return "STRATEGIC"

        if confidence >= 0.5:
            return "BALANCED"

        return "CAUTIOUS"

    # --------------------------------------------------
    # Executive Readiness
    # --------------------------------------------------
    def _readiness_score(
        self,
        awareness: Dict[str, Any],
        calibration: Dict[str, Any]
    ) -> float:

        confidence = awareness.get("confidence_score", 0)

        stability_weight = {
            "HIGH": 1.0,
            "MODERATE": 0.75,
            "LOW": 0.5,
            "UNKNOWN": 0.6
        }

        stability = calibration.get("stability_state", "UNKNOWN")

        return round(confidence * stability_weight[stability], 2)

    # --------------------------------------------------
    # Unified Intelligence Report
    # --------------------------------------------------
    def orchestrate(
        self,
        signals: Dict[str, Any],
        context: Dict[str, Any],
        prediction: Dict[str, Any],
        priority: Dict[str, Any],
        executive: Dict[str, Any],
        awareness: Dict[str, Any],
        memory_summary: Dict[str, Any],
        calibration: Dict[str, Any],
    ) -> Dict[str, Any]:

        strategic_state = self._determine_state(
            awareness, calibration
        )

        readiness = self._readiness_score(
            awareness, calibration
        )

        return {
            "stage": "15.0",
            "strategic_state": strategic_state,
            "executive_readiness": readiness,
            "advisory_bias": calibration.get("advisory_bias"),
            "confidence_score": awareness.get("confidence_score"),
            "risk_flags": awareness.get("risk_flags"),
            "memory_patterns": memory_summary,
            "calibration_profile": calibration,
            "executive_summary": executive,
            "system_mode": self.mode,
        }