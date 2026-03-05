"""
Terminal Kernel Model

Deterministic terminal kernel synthesis logic.
"""

from typing import Dict


class TerminalKernelModel:

    def evaluate(self, closure_vector: Dict[str, float]) -> Dict[str, float]:
        if not closure_vector:
            return {}

        avg = sum(closure_vector.values()) / len(closure_vector)

        return {
            k: round((v + avg) / 2.0, 6)
            for k, v in closure_vector.items()
        }

    def classify_state(
        self,
        coherence_score: float,
        drift_index: float
    ) -> str:

        if coherence_score >= 0.97 and drift_index <= 0.03:
            return "TERMINAL_KERNEL_CLOSED"

        if coherence_score >= 0.9:
            return "TERMINAL_KERNEL_CLOSING"

        return "TERMINAL_KERNEL_DRIFT"