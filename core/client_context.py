# app/core/client_context.py

from datetime import datetime


class ClientContextManager:
    """
    Stage-5.0 Cognitive Isolation Layer
    Maintains separated runtime context per client.
    """

    def __init__(self):
        self.clients = {}

    def get_client(self, client_id: str):

        if client_id not in self.clients:
            self.clients[client_id] = {
                "created_at": datetime.utcnow().isoformat(),
                "requests": 0,
            }

        self.clients[client_id]["requests"] += 1
        return self.clients[client_id]


client_context = ClientContextManager()