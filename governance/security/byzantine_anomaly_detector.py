from typing import Dict

from .node_trust_registry import NodeTrustRegistry
from .anomaly_classification_engine import AnomalyClassificationEngine


class ByzantineAnomalyDetector:
    """
    Stage-116.0

    Detects adversarial or faulty governance nodes.

    Responsibilities:

    - Analyze replication mismatches
    - Classify anomalies
    - Update deterministic trust scores
    - Produce governance security report

    No mutation authority outside governance telemetry.
    """

    def __init__(self):

        self.trust_registry = NodeTrustRegistry()
        self.classifier = AnomalyClassificationEngine()

    def analyze(self, replication_result: Dict) -> Dict:

        mismatches = replication_result.get("mismatches", [])

        classification = self.classifier.classify(mismatches)

        trust_updates = {}

        for anomaly in classification["anomalies"]:

            peer = anomaly["peer"]

            if anomaly["type"] == "NETWORK_FAILURE":
                trust = self.trust_registry.update_trust(peer, -0.05)

            elif anomaly["type"] == "LEDGER_DIVERGENCE":
                trust = self.trust_registry.update_trust(peer, -0.20)

            trust_updates[peer] = trust

        return {
            "anomaly_summary": classification,
            "trust_scores": self.trust_registry.snapshot(),
            "trust_updates": trust_updates,
        }