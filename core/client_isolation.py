# core/client_isolation.py

"""
Stage-16.2 — Client Isolation Layer
Provides multi-tenant separation for Jarvis.
"""

from typing import Dict, Any


class ClientIsolation:

    def __init__(self):
        # Each client gets its own container
        self.clients: Dict[str, Dict[str, Any]] = {}

    # --------------------------------------------------
    # Get Client Space
    # --------------------------------------------------
    def get_client(self, client_id: str):

        if client_id not in self.clients:
            self.clients[client_id] = {
                "sessions": {},
                "memory": []
            }

        return self.clients[client_id]

    # --------------------------------------------------
    # Store Memory Per Client
    # --------------------------------------------------
    def store_memory(self, client_id: str, record: Dict[str, Any]):

        client = self.get_client(client_id)
        client["memory"].append(record)

        if len(client["memory"]) > 100:
            client["memory"].pop(0)

    # --------------------------------------------------
    # Client Summary
    # --------------------------------------------------
    def summary(self, client_id: str):

        client = self.get_client(client_id)

        return {
            "client_id": client_id,
            "memory_records": len(client["memory"])
        }