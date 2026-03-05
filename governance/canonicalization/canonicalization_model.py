"""
Canonicalization Model

Deterministic canonical synthesis logic.
"""

from typing import Dict


class CanonicalizationModel:

    def evaluate(self, attestation_vector: Dict[str, float]) -> Dict[str, float]:
        if not attestation_vector:
            return {}

        avg = sum(attestation_vector.values()) / len(attestation_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in attestation_vector.items()
        }

    def classify_state(
        self,
        coherence_score: float,
        variance_index: float
    ) -> str:

        if coherence_score >= 0.998 and variance_index <= 0.006:
            return "CANONICALIZED"

        if coherence_score >= 0.99:
            return "CANONICALIZING"

        return "NONCANONICAL_VARIANCE"