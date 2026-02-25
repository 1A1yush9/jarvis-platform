# core/executive_interface.py

"""
Stage-15.1 — Executive Intelligence Interface

Purpose:
Provides a stable external-facing intelligence
response format for API delivery.

Advisory cognition only.
No execution authority.
"""

from typing import Dict, Any
from datetime import datetime


class ExecutiveIntelligenceInterface:

    def __init__(self):
        self.version = "15.1"
        self.mode = "advisory"

    # --------------------------------------------------
    # Build API Response
    # --------------------------------------------------
    def build_response(
        self,
        orchestrated_output: Dict[str, Any]
    ) -> Dict[str, Any]:

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "system_version": self.version,
            "mode": self.mode,

            # Strategic overview
            "strategic_state":
                orchestrated_output.get("strategic_state"),

            "executive_readiness":
                orchestrated_output.get("executive_readiness"),

            "confidence_score":
                orchestrated_output.get("confidence_score"),

            "advisory_bias":
                orchestrated_output.get("advisory_bias"),

            # Risk & awareness
            "risk_flags":
                orchestrated_output.get("risk_flags"),

            # Intelligence summary
            "executive_summary":
                orchestrated_output.get("executive_summary"),

            # Diagnostics (safe exposure)
            "calibration_profile":
                orchestrated_output.get("calibration_profile"),

            "memory_patterns":
                orchestrated_output.get("memory_patterns"),

            "notice":
                "Advisory intelligence only. No autonomous execution enabled."
        }