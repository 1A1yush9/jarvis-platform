from typing import Dict

from .quorum_health_evaluator import QuorumHealthEvaluator
from .network_partition_detector import NetworkPartitionDetector


class GlobalConsensusStabilizer:
    """
    Stage-115.0

    Provides cluster-wide governance stability evaluation.

    Responsibilities:

    - Evaluate quorum health
    - Detect network partitions
    - Produce deterministic cluster stability report

    No mutation authority.
    """

    def __init__(self):

        self.quorum = QuorumHealthEvaluator()
        self.partition = NetworkPartitionDetector()

    def evaluate(
        self,
        local_snapshot: Dict,
        peer_snapshots: Dict,
        replication_result: Dict,
    ) -> Dict:

        quorum_status = self.quorum.evaluate(replication_result)

        partition_status = self.partition.detect(
            local_snapshot,
            peer_snapshots,
        )

        stability = "STABLE"

        if quorum_status["status"] != "HEALTHY":
            stability = "UNSTABLE"

        if partition_status["partition_detected"]:
            stability = "PARTITIONED"

        return {
            "cluster_stability": stability,
            "quorum_health": quorum_status,
            "partition_analysis": partition_status,
        }