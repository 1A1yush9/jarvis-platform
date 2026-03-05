"""
Civilizational Envelope Model

Defines deterministic stability thresholds across civilizational epochs.
"""


class CivilizationalEnvelopeModel:

    def evaluate(self, coherence_score: float, drift_score: float) -> str:

        if coherence_score >= 0.97 and drift_score <= 0.02:
            return "OPTIMAL_ENVELOPE"

        if coherence_score >= 0.94 and drift_score <= 0.04:
            return "STABLE_ENVELOPE"

        if coherence_score >= 0.90:
            return "MARGINAL_ENVELOPE"

        return "OUTSIDE_ENVELOPE"