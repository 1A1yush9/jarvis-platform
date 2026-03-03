"""
Jarvis Platform — Stage 103.0
Deterministic Dependency Integrity Verifier (DDIV)

Advisory-Only
Deterministic
No execution authority.
No mutation authority.

Ensures governance layer dependencies remain acyclic,
hierarchically valid, and constitutionally aligned.
"""

from typing import Dict, List, Set, Any


class DeterministicDependencyIntegrityVerifier:
    """
    Validates dependency graph integrity across governance layers.
    """

    STAGE_VERSION = "103.0"
    DEPENDENCY_SEAL = "JARVIS_STAGE_103_DEPENDENCY_INTEGRITY_VERIFIER"

    def __init__(self, dependency_map: Dict[str, List[str]]):
        """
        dependency_map format:
        {
            "Stage-96": ["Stage-95", "Stage-94"],
            ...
        }
        """
        self.dependency_map = dependency_map

    # ------------------------------------------------------------------
    # Cycle Detection (DFS)
    # ------------------------------------------------------------------

    def _has_cycle(self) -> bool:
        visited: Set[str] = set()
        recursion_stack: Set[str] = set()

        def dfs(node: str) -> bool:
            if node not in visited:
                visited.add(node)
                recursion_stack.add(node)

                for neighbor in self.dependency_map.get(node, []):
                    if neighbor not in visited and dfs(neighbor):
                        return True
                    elif neighbor in recursion_stack:
                        return True

            recursion_stack.remove(node)
            return False

        for node in self.dependency_map:
            if dfs(node):
                return True

        return False

    # ------------------------------------------------------------------
    # Constitutional Root Alignment
    # ------------------------------------------------------------------

    def verify_constitutional_root(self, root_stage: str) -> bool:
        """
        Ensures all dependency chains ultimately trace to constitutional root.
        """
        for node, dependencies in self.dependency_map.items():
            if node == root_stage:
                continue
            if root_stage not in self._collect_all_dependencies(node):
                return False
        return True

    def _collect_all_dependencies(self, node: str) -> Set[str]:
        collected = set()

        def traverse(n: str):
            for dep in self.dependency_map.get(n, []):
                if dep not in collected:
                    collected.add(dep)
                    traverse(dep)

        traverse(node)
        return collected

    # ------------------------------------------------------------------
    # Full Dependency Audit
    # ------------------------------------------------------------------

    def audit_dependencies(self, constitutional_root: str) -> Dict[str, Any]:

        cycle_detected = self._has_cycle()
        root_alignment = self.verify_constitutional_root(constitutional_root)

        compliant = not cycle_detected and root_alignment

        return {
            "stage": self.STAGE_VERSION,
            "seal": self.DEPENDENCY_SEAL,
            "cycle_detected": cycle_detected,
            "constitutional_root_aligned": root_alignment,
            "dependency_integrity_certified": compliant
        }


# ----------------------------------------------------------------------
# Factory Constructor
# ----------------------------------------------------------------------

def initialize_stage_103(
    dependency_map: Dict[str, List[str]]
) -> DeterministicDependencyIntegrityVerifier:

    return DeterministicDependencyIntegrityVerifier(dependency_map)