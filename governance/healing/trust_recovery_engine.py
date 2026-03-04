from typing import Dict


class TrustRecoveryEngine:
    """
    Gradually restores trust for nodes with improved behavior.
    """

    RECOVERY_RATE = 0.05
    MAX_TRUST = 1.0

    def recover(self, trust_scores: Dict[str, float]) -> Dict[str, float]:

        recovered = {}

        for node, score in trust_scores.items():

            if score < self.MAX_TRUST:

                new_score = min(self.MAX_TRUST, score + self.RECOVERY_RATE)

                recovered[node] = round(new_score, 4)

            else:

                recovered[node] = score

        return recovered