"""
Resilience Alignment Model

Deterministic alignment synthesis logic.
"""

from typing import Dict


class ResilienceAlignmentModel:

    def align(self, normalized_vector: Dict[str, float]) -> Dict[str, float]:
        if not normalized_vector:
            return {}

        avg = sum(normalized_vector.values()) / len(normalized_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in normalized_vector.items()
        }

    def classify_posture(
        self,
        readiness_score: float,
        fragility_index: float
    ) -> str:

        if readiness_score >= 0.85 and fragility_index <= 0.08:
            return "RESILIENT"

        if readiness_score >= 0.7:
            return "ADAPTIVE"

        return "FRAGILE"