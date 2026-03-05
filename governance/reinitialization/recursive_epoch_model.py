"""
Recursive Epoch Model

Deterministic recursive reset synthesis logic.
"""

from typing import Dict


class RecursiveEpochModel:

    def evaluate(self, transition_vector: Dict[str, float]) -> Dict[str, float]:
        if not transition_vector:
            return {}

        avg = sum(transition_vector.values()) / len(transition_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in transition_vector.items()
        }

    def classify_state(
        self,
        readiness_score: float,
        instability_index: float
    ) -> str:

        if readiness_score >= 0.94 and instability_index <= 0.05:
            return "REINITIALIZATION_READY"

        if readiness_score >= 0.85:
            return "REINITIALIZATION_MONITORED"

        return "REINITIALIZATION_UNSTABLE"