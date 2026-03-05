"""
Epoch Transition Model

Deterministic epoch-boundary synthesis logic.
"""

from typing import Dict


class EpochTransitionModel:

    def evaluate(self, observation_vector: Dict[str, float]) -> Dict[str, float]:
        if not observation_vector:
            return {}

        avg = sum(observation_vector.values()) / len(observation_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in observation_vector.items()
        }

    def classify_state(
        self,
        readiness_score: float,
        instability_index: float
    ) -> str:

        if readiness_score >= 0.93 and instability_index <= 0.05:
            return "TRANSITION_READY"

        if readiness_score >= 0.82:
            return "TRANSITION_MONITORED"

        return "TRANSITION_UNSTABLE"