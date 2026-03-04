from typing import Dict


class NodeTrustRegistry:
    """
    Deterministic trust registry for governance nodes.

    Trust score ranges:
        1.0 = fully trusted
        0.0 = completely unreliable
    """

    def __init__(self):
        self._registry: Dict[str, float] = {}

    def get_trust(self, node: str) -> float:
        return self._registry.get(node, 1.0)

    def update_trust(self, node: str, delta: float) -> float:

        current = self.get_trust(node)

        new_score = max(0.0, min(1.0, current + delta))

        self._registry[node] = new_score

        return new_score

    def snapshot(self) -> Dict[str, float]:
        return dict(sorted(self._registry.items()))