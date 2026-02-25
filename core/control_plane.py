# core/control_plane.py

"""
Stage-16.0 — Intelligence Control Plane

Central governance layer controlling
Jarvis operational behavior.
"""

from typing import Dict, Any
from datetime import datetime


class ControlPlane:

    def __init__(self):
        self.mode = "advisory"
        self.updated_at = datetime.utcnow().isoformat()

        self.allowed_modes = [
            "advisory",
            "analysis_intensive",
            "safe_guarded",
            "maintenance",
        ]

    # --------------------------------------------------
    # Get Current Mode
    # --------------------------------------------------
    def status(self) -> Dict[str, Any]:
        return {
            "mode": self.mode,
            "updated_at": self.updated_at
        }

    # --------------------------------------------------
    # Change Mode
    # --------------------------------------------------
    def set_mode(self, new_mode: str):

        if new_mode not in self.allowed_modes:
            return {
                "success": False,
                "message": "Invalid mode"
            }

        self.mode = new_mode
        self.updated_at = datetime.utcnow().isoformat()

        return {
            "success": True,
            "mode": self.mode
        }

    # --------------------------------------------------
    # Mode Rules
    # --------------------------------------------------
    def allow_processing(self) -> bool:
        return self.mode != "maintenance"