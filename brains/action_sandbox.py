# brains/action_sandbox.py

import time
from brains.capability_gate import capability_gate


class ActionSandbox:
    """
    Safe execution simulator.
    All actions must pass Capability Gate.
    Executes internal mock actions only.
    """

    def __init__(self):
        self.started = time.time()
        self.history = []

    def execute(self, action_name: str):

        # Ask gate for permission
        auth = capability_gate.authorize(action_name)

        result = {
            "action": action_name,
            "authorized": auth["authorized"],
            "reason": auth["reason"],
            "timestamp": time.time(),
        }

        # Only simulate — no real execution
        if auth["authorized"]:
            result["result"] = "sandbox_execution_success"
        else:
            result["result"] = "blocked_by_gate"

        self.history.append(result)

        return result

    def report(self):
        return {
            "mode": "sandbox_only",
            "executions": self.history[-20:],
            "uptime": round(time.time() - self.started, 2)
        }


action_sandbox = ActionSandbox()