import requests
from typing import Dict

from .node_peer_registry import NodePeerRegistry
from .ledger_state_snapshot import LedgerStateSnapshot
from .replication_consensus import ReplicationConsensus


class DeterministicReplicationEngine:
    """
    Stage-114.0
    Deterministic Multi-Node Governance Replication

    Responsibilities:

    - Snapshot local governance state
    - Query peer nodes
    - Compare deterministic hashes
    - Detect divergence
    - Emit telemetry signals

    No authority to mutate system state.
    """

    PEER_ENDPOINT = "/governance/snapshot"

    def __init__(self):
        self.registry = NodePeerRegistry()
        self.snapshot = LedgerStateSnapshot()
        self.consensus = ReplicationConsensus()

    def execute(self) -> dict:

        local_snapshot = self.snapshot.snapshot_payload()

        peer_snapshots = self._collect_peer_snapshots()

        result = self.consensus.evaluate(local_snapshot, peer_snapshots)

        return {
            "local_snapshot": local_snapshot,
            "peer_count": len(peer_snapshots),
            "replication_result": result,
        }

    def _collect_peer_snapshots(self) -> Dict[str, dict]:

        peers = self.registry.get_peers()

        peer_data = {}

        for peer in peers:

            try:

                r = requests.get(
                    f"{peer}{self.PEER_ENDPOINT}",
                    timeout=3,
                )

                if r.status_code == 200:
                    peer_data[peer] = r.json()

            except Exception:
                peer_data[peer] = {
                    "snapshot_hash": "UNREACHABLE",
                    "segment_hash": "UNREACHABLE",
                }

        return peer_data