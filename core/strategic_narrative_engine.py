"""
Jarvis Platform — Stage 21.5
Strategic Narrative Generator

Transforms prioritized executive signals
into a readable strategic briefing.

SAFE MODE:
Template-based synthesis only.
No execution authority.
"""

from datetime import datetime
from typing import Dict, Any, List


class StrategicNarrativeEngine:
    def __init__(self, prioritizer):
        self.engine_name = "Strategic Narrative Generator"
        self.version = "21.5"
        self.mode = "advisory_only"
        self.prioritizer = prioritizer

    # -----------------------------------------------------
    # Narrative Builder
    # -----------------------------------------------------
    def generate_narrative(self) -> Dict[str, Any]:

        prioritized_data = self.prioritizer.prioritize()
        priorities: List[Dict[str, Any]] = prioritized_data.get(
            "priorities", []
        )

        if not priorities:
            summary = "System operating normally with no critical signals."
            focus = ["Maintain current strategic trajectory."]
        else:
            top = priorities[0]

            if top["priority"] == 1:
                summary = (
                    "Critical strategic risk detected requiring executive attention."
                )
            elif top["priority"] == 2:
                summary = (
                    "Emerging strategic instability observed. Preventive action advised."
                )
            else:
                summary = (
                    "Operational optimization opportunities identified."
                )

            focus = [p["message"] for p in priorities[:3]]

        return {
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "executive_summary": summary,
            "priority_focus": focus,
            "mode": self.mode,
        }

    # -----------------------------------------------------
    # Status
    # -----------------------------------------------------
    def status(self):
        return {
            "engine": self.engine_name,
            "version": self.version,
            "status": "operational",
            "mode": self.mode,
        }