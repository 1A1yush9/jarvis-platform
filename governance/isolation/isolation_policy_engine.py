from typing import Dict


class IsolationPolicyEngine:
    """
    Determines if a node should be isolated.
    """

    TRUST_THRESHOLD = 0.40

    def evaluate(self, security_report: Dict) -> Dict:

        trust_scores = security_report.get("trust_scores", {})

        isolation_candidates = []

        for node, score in trust_scores.items():

            if score <= self.TRUST_THRESHOLD:

                isolation_candidates.append({
                    "node": node,
                    "reason": "LOW_TRUST_SCORE",
                    "score": score
                })

        return {
            "isolation_candidates": isolation_candidates
        }