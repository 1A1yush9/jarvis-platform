"""
Post-Closure Model

Deterministic post-closure synthesis logic.
"""

from typing import Dict


class PostClosureModel:

    def observe(self, closure_vector: Dict[str, float]) -> Dict[str, float]:
        if not closure_vector:
            return {}

        avg = sum(closure_vector.values()) / len(closure_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in closure_vector.items()
        }

    def classify_state(
        self,
        persistence_score: float,
        resurgence_index: float
    ) -> str:

        if persistence_score >= 0.94 and resurgence_index <= 0.04:
            return "PERSISTENT"

        if persistence_score >= 0.85:
            return "MONITORED"

        return "RESURGENT"