import requests
from typing import Dict

from .node_peer_registry import NodePeerRegistry
from .ledger_state_snapshot import LedgerStateSnapshot
from .replication_consensus import ReplicationConsensus
from governance.consensus.global_consensus_stabilizer import GlobalConsensusStabilizer
from governance.security.byzantine_anomaly_detector import ByzantineAnomalyDetector


class DeterministicReplicationEngine:
    """
    Stage-114 / 115 / 116

    Deterministic Multi-Node Governance Replication

    Responsibilities

    - Snapshot local governance state
    - Query peer nodes
    - Compare deterministic hashes
    - Detect divergence
    - Evaluate cluster stability
    - Detect Byzantine anomalies

    No mutation authority.
    """

    PEER_ENDPOINT = "/governance/snapshot"

    def __init__(self):
        self.registry = NodePeerRegistry()
        self.snapshot = LedgerStateSnapshot()
        self.consensus = ReplicationConsensus()
        self.stabilizer = GlobalConsensusStabilizer()
        self.anomaly_detector = ByzantineAnomalyDetector()

    def execute(self) -> dict:

        # 1️⃣ Local governance snapshot
        local_snapshot = self.snapshot.snapshot_payload()

        # 2️⃣ Collect peer snapshots
        peer_snapshots = self._collect_peer_snapshots()

        # 3️⃣ Replication consensus
        replication_result = self.consensus.evaluate(
            local_snapshot,
            peer_snapshots
        )

        # 4️⃣ Cluster stability analysis
        stability = self.stabilizer.evaluate(
            local_snapshot,
            peer_snapshots,
            replication_result
        )

        # 5️⃣ Byzantine anomaly detection
        security_report = self.anomaly_detector.analyze(
            replication_result
        )

        # 6️⃣ Deterministic final output
        return {
            "local_snapshot": local_snapshot,
            "peer_count": len(peer_snapshots),
            "replication_result": replication_result,
            "cluster_stability": stability,
            "security_analysis": security_report,
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

                    try:
                        payload = r.json()

                        if "snapshot_hash" in payload:
                            peer_data[peer] = payload
                        else:
                            peer_data[peer] = {
                                "snapshot_hash": "INVALID",
                                "segment_hash": "INVALID",
                            }

                    except Exception:
                        peer_data[peer] = {
                            "snapshot_hash": "INVALID_JSON",
                            "segment_hash": "INVALID_JSON",
                        }

            except Exception:

                peer_data[peer] = {
                    "snapshot_hash": "UNREACHABLE",
                    "segment_hash": "UNREACHABLE",
                }

        return peer_data