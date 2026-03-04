from typing import Dict, List


class AnomalyClassificationEngine:
    """
    Classifies peer behavior using deterministic rules.
    """

    def classify(self, mismatches: List[Dict]) -> Dict:

        anomalies = []

        for m in mismatches:

            peer = m["peer"]
            peer_hash = m["peer_hash"]

            if peer_hash == "UNREACHABLE":

                anomalies.append({
                    "peer": peer,
                    "type": "NETWORK_FAILURE",
                })

            else:

                anomalies.append({
                    "peer": peer,
                    "type": "LEDGER_DIVERGENCE",
                })

        return {
            "anomaly_count": len(anomalies),
            "anomalies": anomalies,
        }