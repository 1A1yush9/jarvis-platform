from typing import Dict


class FaultDomainRegistry:
    """
    Tracks isolated governance nodes.

    Isolation is deterministic and reversible.
    """

    def __init__(self):
        self._isolated_nodes: Dict[str, str] = {}

    def isolate(self, node: str, reason: str):

        self._isolated_nodes[node] = reason

    def is_isolated(self, node: str) -> bool:

        return node in self._isolated_nodes

    def snapshot(self) -> Dict[str, str]:

        return dict(sorted(self._isolated_nodes.items()))