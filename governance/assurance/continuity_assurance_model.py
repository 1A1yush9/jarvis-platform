"""
Continuity Assurance Model

Deterministic recursive continuity synthesis logic.
"""

from typing import Dict


class ContinuityAssuranceModel:

    def assure(self, convergence_vector: Dict[str, float]) -> Dict[str, float]:
        if not convergence_vector:
            return {}

        avg = sum(convergence_vector.values()) / len(convergence_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in convergence_vector.items()
        }

    def classify_state(
        self,
        continuity_score: float,
        discontinuity_index: float
    ) -> str:

        if continuity_score >= 0.9 and discontinuity_index <= 0.06:
            return "ASSURED"

        if continuity_score >= 0.78:
            return "STABILIZING"

        return "DISRUPTED"