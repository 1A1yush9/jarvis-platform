# app/core/usage_meter.py

from datetime import datetime


class UsageMeter:
    """
    Stage-5.2 Revenue Foundation
    Tracks per-client usage metrics.
    Database-ready design.
    """

    def __init__(self):
        self.usage = {}

    def record(self, client_id: str, action: str):

        if client_id not in self.usage:
            self.usage[client_id] = {
                "total_requests": 0,
                "actions": {},
                "last_used": None,
            }

        client = self.usage[client_id]

        client["total_requests"] += 1
        client["last_used"] = datetime.utcnow().isoformat()

        if action not in client["actions"]:
            client["actions"][action] = 0

        client["actions"][action] += 1

        return client

    def summary(self, client_id: str):
        return self.usage.get(client_id, {})


usage_meter = UsageMeter()