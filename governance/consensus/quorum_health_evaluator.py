from typing import Dict


class QuorumHealthEvaluator:
    """
    Evaluates cluster quorum health deterministically.

    Input:
        replication_result from Stage-114
    """

    def evaluate(self, replication_result: Dict) -> Dict:

        matches = replication_result["matches"]
        mismatches = replication_result["mismatches"]

        total_nodes = len(matches) + len(mismatches)

        if total_nodes == 0:
            return {
                "status": "SINGLE_NODE",
                "health_score": 1.0,
            }

        healthy_nodes = len(matches)

        health_score = healthy_nodes / total_nodes

        status = "HEALTHY"

        if health_score < 0.7:
            status = "DEGRADED"

        if health_score < 0.5:
            status = "CRITICAL"

        return {
            "status": status,
            "health_score": round(health_score, 4),
            "total_nodes": total_nodes,
            "healthy_nodes": healthy_nodes,
        }