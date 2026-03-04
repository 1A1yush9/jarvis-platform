import os
from typing import List


class NodePeerRegistry:
    """
    Deterministic peer registry for governance replication.
    Peers are defined via environment variable to keep Render deployment simple.
    """

    ENV_KEY = "GOVERNANCE_PEERS"

    def __init__(self):
        self._peers = self._load_peers()

    def _load_peers(self) -> List[str]:
        peers = os.getenv(self.ENV_KEY, "")
        if not peers:
            return []
        return [p.strip() for p in peers.split(",") if p.strip()]

    def get_peers(self) -> List[str]:
        return list(sorted(self._peers))