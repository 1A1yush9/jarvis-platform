import requests
from typing import Dict

from .node_peer_registry import NodePeerRegistry
from .ledger_state_snapshot import LedgerStateSnapshot
from .replication_consensus import ReplicationConsensus
from governance.consensus.global_consensus_stabilizer import GlobalConsensusStabilizer


class DeterministicReplicationEngine:
    """
    Stage-114 / 115
    Deterministic Multi-Node Governance Replication
    with Global Consensus Stabilization

    Responsibilities:

    - Snapshot local governance state
    - Query peer nodes
    - Compare deterministic hashes
    - Detect divergence
    - Evaluate cluster stability

    No authority to mutate system state.
    """

    PEER_ENDPOINT = "/governance/snapshot"

    def __init__(self):
        self.registry = NodePeerRegistry()
        self.snapshot = LedgerStateSnapshot()
        self.consensus = ReplicationConsensus()
        self.stabilizer = GlobalConsensusStabilizer()

    def execute(self) -> dict:

        # 1️⃣ compute local snapshot
        local_snapshot = self.snapshot.snapshot_payload()

        # 2️⃣ collect peer snapshots
        peer_snapshots = self._collect_peer_snapshots()

        # 3️⃣ run replication verification
        replication_result = self.consensus.evaluate(
            local_snapshot,
            peer_snapshots
        )

        # 4️⃣ evaluate cluster stability
        stability = self.stabilizer.evaluate(
            local_snapshot,
            peer_snapshots,
            replication_result
        )

        # 5️⃣ deterministic output
        return {
            "local_snapshot": local_snapshot,
            "peer_count": len(peer_snapshots),
            "replication_result": replication_result,
            "cluster_stability": stability,
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