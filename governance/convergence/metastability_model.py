"""
Meta-Stability Model

Deterministic convergence synthesis logic.
"""

from typing import Dict


class MetaStabilityModel:

    def converge(self, alignment_vector: Dict[str, float]) -> Dict[str, float]:
        if not alignment_vector:
            return {}

        avg = sum(alignment_vector.values()) / len(alignment_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in alignment_vector.items()
        }

    def classify_state(
        self,
        metastability_score: float,
        divergence_index: float
    ) -> str:

        if metastability_score >= 0.88 and divergence_index <= 0.07:
            return "CONVERGED"

        if metastability_score >= 0.75:
            return "TRANSITIONING"

        return "DIVERGING"