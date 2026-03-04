from typing import Dict, List


class ReintegrationPolicyEngine:
    """
    Determines when isolated nodes can rejoin governance evaluation.
    """

    REINTEGRATION_THRESHOLD = 0.75

    def evaluate(self, trust_scores: Dict[str, float], isolated_nodes: List[str]):

        reintegrated = []

        for node in isolated_nodes:

            score = trust_scores.get(node, 0)

            if score >= self.REINTEGRATION_THRESHOLD:

                reintegrated.append(node)

        return reintegrated