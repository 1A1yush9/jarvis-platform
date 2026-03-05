"""
Terminal Stability Model

Deterministic terminal synthesis logic.
"""

from typing import Dict


class TerminalStabilityModel:

    def evaluate(self, assurance_vector: Dict[str, float]) -> Dict[str, float]:
        if not assurance_vector:
            return {}

        avg = sum(assurance_vector.values()) / len(assurance_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in assurance_vector.items()
        }

    def classify_state(
        self,
        terminal_score: float,
        instability_index: float
    ) -> str:

        if terminal_score >= 0.92 and instability_index <= 0.05:
            return "TERMINALLY_STABLE"

        if terminal_score >= 0.8:
            return "LATE_TRANSITION"

        return "TERMINALLY_UNSTABLE"