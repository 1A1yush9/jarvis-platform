"""
Closure Integrity Model

Deterministic closure synthesis logic.
"""

from typing import Dict


class ClosureIntegrityModel:

    def evaluate(self, terminal_vector: Dict[str, float]) -> Dict[str, float]:
        if not terminal_vector:
            return {}

        avg = sum(terminal_vector.values()) / len(terminal_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in terminal_vector.items()
        }

    def classify_state(
        self,
        legacy_score: float,
        degradation_index: float
    ) -> str:

        if legacy_score >= 0.93 and degradation_index <= 0.04:
            return "CLOSED_PRESERVED"

        if legacy_score >= 0.82:
            return "CLOSING"

        return "DEGRADING"