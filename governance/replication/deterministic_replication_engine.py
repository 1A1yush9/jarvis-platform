import requests
from typing import Dict

from .node_peer_registry import NodePeerRegistry
from .ledger_state_snapshot import LedgerStateSnapshot
from .replication_consensus import ReplicationConsensus

from governance.consensus.global_consensus_stabilizer import GlobalConsensusStabilizer
from governance.security.byzantine_anomaly_detector import ByzantineAnomalyDetector
from governance.isolation.governance_fault_isolator import GovernanceFaultIsolator
from governance.healing.governance_self_healing_orchestrator import GovernanceSelfHealingOrchestrator
from governance.forecasting.governance_predictive_forecaster import GovernancePredictiveForecaster
from governance.stabilization.governance_autonomic_stabilizer import GovernanceAutonomicStabilizer
from governance.oversight.governance_strategic_oversight_engine import GovernanceStrategicOversightEngine
from governance.meta_resilience.governance_meta_resilience_engine import GovernanceMetaResilienceEngine
from governance.evolution.governance_adaptive_evolution_engine import GovernanceAdaptiveEvolutionEngine


class DeterministicReplicationEngine:
    """
    Deterministic Governance Replication Engine

    Integrated Governance Stages

        Stage-114  Deterministic Replication
        Stage-115  Global Consensus Stabilizer
        Stage-116  Byzantine Anomaly Detector
        Stage-117  Governance Fault Domain Isolation
        Stage-118  Governance Self-Healing Orchestrator
        Stage-119  Governance Predictive Risk Forecaster
        Stage-120  Governance Autonomic Stabilization Layer
        Stage-121  Governance Strategic Oversight Engine
        Stage-122  Governance Meta-Resilience Layer
        Stage-123  Governance Adaptive Evolution Engine

    Governance Constraints

    - Deterministic execution
    - Read-only governance layer
    - No mutation authority
    - No runtime execution authority
    """

    PEER_ENDPOINT = "/governance/snapshot"

    def __init__(self):

        # Core replication components
        self.registry = NodePeerRegistry()
        self.snapshot = LedgerStateSnapshot()
        self.consensus = ReplicationConsensus()

        # Governance analysis layers
        self.cluster_stabilizer = GlobalConsensusStabilizer()
        self.anomaly_detector = ByzantineAnomalyDetector()
        self.fault_isolator = GovernanceFaultIsolator()
        self.self_healer = GovernanceSelfHealingOrchestrator()
        self.forecaster = GovernancePredictiveForecaster()
        self.autonomic_stabilizer = GovernanceAutonomicStabilizer()
        self.oversight_engine = GovernanceStrategicOversightEngine()
        self.meta_resilience_engine = GovernanceMetaResilienceEngine()
        self.evolution_engine = GovernanceAdaptiveEvolutionEngine()

    def execute(self) -> Dict:

        # --------------------------------------------------
        # 1. Compute local governance snapshot
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

        stability = self.cluster_stabilizer.evaluate(
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
        # 7. Governance self-healing evaluation
        # --------------------------------------------------

        healing_report = self.self_healer.evaluate(
            security_report,
            fault_domain_report
        )

        # --------------------------------------------------
        # 8. Predictive governance risk forecast
        # --------------------------------------------------

        forecast_report = self.forecaster.evaluate(
            replication_result,
            security_report,
            fault_domain_report
        )

        # --------------------------------------------------
        # 9. Autonomic stabilization recommendation
        # --------------------------------------------------

        stabilization_report = self.autonomic_stabilizer.evaluate(
            forecast_report,
            stability,
            fault_domain_report
        )

        # --------------------------------------------------
        # 10. Strategic governance oversight
        # --------------------------------------------------

        oversight_report = self.oversight_engine.evaluate(
            stability,
            forecast_report
        )

        # --------------------------------------------------
        # 11. Meta-resilience diagnostics
        # --------------------------------------------------

        meta_resilience_report = self.meta_resilience_engine.evaluate(
            stability,
            security_report,
            forecast_report,
            oversight_report
        )

        # --------------------------------------------------
        # 12. Adaptive governance evolution
        # --------------------------------------------------

        evolution_report = self.evolution_engine.evaluate(
            meta_resilience_report,
            forecast_report,
            oversight_report
        )

        # --------------------------------------------------
        # 13. Deterministic governance output
        # --------------------------------------------------

        return {
            "local_snapshot": local_snapshot,
            "peer_count": len(peer_snapshots),
            "replication_result": replication_result,
            "cluster_stability": stability,
            "security_analysis": security_report,
            "fault_domain_status": fault_domain_report,
            "self_healing_status": healing_report,
            "predictive_risk_forecast": forecast_report,
            "autonomic_stabilization": stabilization_report,
            "strategic_governance_oversight": oversight_report,
            "meta_resilience_diagnostics": meta_resilience_report,
            "adaptive_governance_evolution": evolution_report
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