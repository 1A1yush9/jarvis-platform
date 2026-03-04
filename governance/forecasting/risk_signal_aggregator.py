from typing import Dict


class RiskSignalAggregator:
    """
    Aggregates governance risk signals into a deterministic feature set.
    """

    def aggregate(
        self,
        replication_result: Dict,
        security_report: Dict,
        fault_domain_status: Dict
    ) -> Dict:

        mismatch_count = len(replication_result.get("mismatches", []))

        anomaly_summary = security_report.get("anomaly_summary", {})
        anomaly_count = anomaly_summary.get("anomaly_count", 0)

        isolated_nodes = fault_domain_status.get("isolated_nodes", [])

        return {
            "mismatch_count": mismatch_count,
            "anomaly_count": anomaly_count,
            "isolated_nodes": len(isolated_nodes)
        }