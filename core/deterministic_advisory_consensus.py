"""
Stage-82.0 — Deterministic Advisory Consensus Mesh (DACM)

Advisory-only multi-layer consensus engine.
No execution authority.
Deterministic weighted aggregation.
"""

import hashlib
import json
from typing import Dict, Any
from datetime import datetime


class DeterministicAdvisoryConsensus:
    """
    Deterministic Advisory Consensus Mesh

    - Aggregates governance advisory layers
    - Computes weighted consensus score
    - Detects disagreement anomalies
    - Generates consensus certification seal
    """

    def __init__(self):
        # Fixed deterministic weights (must sum to 1.0)
        self.weights = {
            "predictive_risk": 0.4,
            "coherence_status": 0.3,
            "severity_score": 0.2,
            "entropy_score": 0.1
        }

    # ------------------------------------------------------------------
    # Deterministic Hash Utility
    # ------------------------------------------------------------------

    def _hash_state(self, state: Dict[str, Any]) -> str:
        encoded = json.dumps(state, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    # ------------------------------------------------------------------
    # Normalization Helpers
    # ------------------------------------------------------------------

    def _normalize_coherence(self, coherence_status: bool) -> float:
        return 1.0 if coherence_status else 0.0

    # ------------------------------------------------------------------
    # Consensus Computation
    # ------------------------------------------------------------------

    def compute_consensus(
        self,
        predictive_layer: Dict[str, Any],
        coherence_layer: Dict[str, Any],
        severity_layer: Dict[str, Any],
        entropy_layer: Dict[str, Any]
    ) -> Dict[str, Any]:

        timestamp = datetime.utcnow().isoformat()

        predictive_risk = predictive_layer.get("risk_envelope", {}).get("risk_score", 0.0)
        coherence_score = self._normalize_coherence(
            coherence_layer.get("coherence_status", False)
        )
        severity_score = severity_layer.get("severity_score", 0.0)
        entropy_score = entropy_layer.get("entropy_score", 0.0)

        weighted_score = (
            predictive_risk * self.weights["predictive_risk"] +
            coherence_score * self.weights["coherence_status"] +
            severity_score * self.weights["severity_score"] +
            entropy_score * self.weights["entropy_score"]
        )

        disagreement_flag = (
            predictive_risk > 0.5 and coherence_score == 1.0
        )

        consensus_level = "STABLE"
        if weighted_score > 0.4:
            consensus_level = "WATCH"
        if weighted_score > 0.6:
            consensus_level = "CRITICAL"

        consensus_envelope = {
            "stage": "82.0",
            "timestamp": timestamp,
            "weighted_score": round(weighted_score, 6),
            "consensus_level": consensus_level,
            "disagreement_flag": disagreement_flag,
            "advisory_mode": True,
            "execution_authority": False
        }

        consensus_envelope["consensus_seal"] = self._hash_state(consensus_envelope)

        return consensus_envelope