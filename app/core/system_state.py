# app/core/system_state.py

from datetime import datetime

class SystemState:
    """
    Maintains runtime health and readiness state of Jarvis.
    Designed to later integrate with distributed health checks.
    """

    def __init__(self):
        self.started_at = datetime.utcnow()
        self.brain_loaded = True
        self.api_ready = True
        self.last_check = datetime.utcnow()

    def health(self):
        self.last_check = datetime.utcnow()

        return {
            "status": "ok" if self.api_ready else "degraded",
            "brain_loaded": self.brain_loaded,
            "api_ready": self.api_ready,
            "started_at": self.started_at.isoformat(),
            "last_check": self.last_check.isoformat(),
        }


# Singleton instance
system_state = SystemState()