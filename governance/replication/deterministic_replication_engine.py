import requests
from typing import Dict

from .node_peer_registry import NodePeerRegistry
from .ledger_state_snapshot import LedgerStateSnapshot
from .replication_consensus import ReplicationConsensus

from governance.consensus.global_consensus_stabilizer import GlobalConsensusStabilizer
from governance.security.byzantine_anomaly_detector import ByzantineAnomalyDetector
from governance.isolation.governance_fault_isolator import GovernanceFaultIsolator
from governance.healing.governance_self_healing_orchestrator import GovernanceSelfHealingOrchestrator


class DeterministicReplicationEngine:
    """
    Deterministic Governance Replication Engine

    Integrated Stages
        Stage-114  Deterministic Replication
        Stage-115  Global Consensus Stabilizer
        Stage-116  Byzantine Anomaly Detector
        Stage-117  Governance Fault Domain Isolation
        Stage-118  Governance Self-Healing Orchestrator

    Governance Layer Rules

    - Read-only
    - Deterministic
    - No mutation authority
    - No runtime execution authority
    """

    PEER_ENDPOINT = "/governance/snapshot"

    def __init__(self):

        self.registry = NodePeerRegistry()
        self.snapshot = LedgerStateSnapshot()
        self.consensus = ReplicationConsensus()

        self.stabilizer = GlobalConsensusStabilizer()
        self.anomaly_detector = ByzantineAnomalyDetector()
        self.fault_isolator = GovernanceFaultIsolator()
        self.self_healer = GovernanceSelfHealingOrchestrator()

    def execute(self) -> Dict:

        # --------------------------------------------------
        # 1. Local governance snapshot
        # --------------------------------------------------

        local_snapshot = self.snapshot.snapshot_payload()

        # --------------------------------------------------
        # 2. Collect peer snapshots
        # --------------------------------------------------

        peer_snapshots = self._collect_peer_snapshots()

        # --------------------------------------------------
        # 3. Replication consensus verification
        # --------------------------------------------------

        replication_result = self.consensus.evaluate(
            local_snapshot,
            peer_snapshots
        )

        # --------------------------------------------------
        # 4. Cluster stability evaluation
        # --------------------------------------------------

        stability = self.stabilizer.evaluate(
            local_snapshot,
            peer_snapshots,
            replication_result
        )

        # --------------------------------------------------
        # 5. Byzantine anomaly detection
        # --------------------------------------------------

        security_report = self.anomaly_detector.analyze(
            replication_result
        )

        # --------------------------------------------------
        # 6. Fault domain isolation
        # --------------------------------------------------

        fault_domain_report = self.fault_isolator.evaluate(
            security_report
        )

        # --------------------------------------------------
        # 7. Governance self-healing
        # --------------------------------------------------

        healing_report = self.self_healer.evaluate(
            security_report,
            fault_domain_report
        )

        # --------------------------------------------------
        # 8. Deterministic governance output
        # --------------------------------------------------

        return {
            "local_snapshot": local_snapshot,
            "peer_count": len(peer_snapshots),
            "replication_result": replication_result,
            "cluster_stability": stability,
            "security_analysis": security_report,
            "fault_domain_status": fault_domain_report,
            "self_healing_status": healing_report
        }

    def _collect_peer_snapshots(self) -> Dict[str, dict]:

        peers = self.registry.get_peers()

        peer_data: Dict[str, dict] = {}

        for peer in peers:

            try:

                response = requests.get(
                    f"{peer}{self.PEER_ENDPOINT}",
                    timeout=3
                )

                if response.status_code == 200:

                    try:

                        payload = response.json()

                        if isinstance(payload, dict) and "snapshot_hash" in payload:

                            peer_data[peer] = {
                                "snapshot_hash": payload.get("snapshot_hash"),
                                "segment_hash": payload.get("segment_hash")
                            }

                        else:

                            peer_data[peer] = {
                                "snapshot_hash": "INVALID_PAYLOAD",
                                "segment_hash": "INVALID_PAYLOAD"
                            }

                    except Exception:

                        peer_data[peer] = {
                            "snapshot_hash": "INVALID_JSON",
                            "segment_hash": "INVALID_JSON"
                        }

                else:

                    peer_data[peer] = {
                        "snapshot_hash": "HTTP_ERROR",
                        "segment_hash": "HTTP_ERROR"
                    }

            except Exception:

                peer_data[peer] = {
                    "snapshot_hash": "UNREACHABLE",
                    "segment_hash": "UNREACHABLE"
                }

        return peer_data