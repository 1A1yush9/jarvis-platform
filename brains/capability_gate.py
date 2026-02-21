# brains/capability_gate.py

import time


class CapabilityGate:
    """
    Central execution authorization system.
    ALL future actions must pass here.
    """

    def __init__(self):
        self.started = time.time()
        self.execution_mode = "LOCKED"
        self.allowed_actions = []

    # ---------------------------------
    # Mode control
    # ---------------------------------
    def get_status(self):
        return {
            "execution_mode": self.execution_mode,
            "allowed_actions": self.allowed_actions,
            "gate_uptime": round(time.time() - self.started, 2),
            "safety": "active"
        }

    # ---------------------------------
    # Check permission
    # ---------------------------------
    def authorize(self, action_name: str):

        if self.execution_mode == "LOCKED":
            return {
                "authorized": False,
                "reason": "system_locked"
            }

        if action_name not in self.allowed_actions:
            return {
                "authorized": False,
                "reason": "action_not_allowed"
            }

        return {
            "authorized": True,
            "reason": "approved"
        }


capability_gate = CapabilityGate()