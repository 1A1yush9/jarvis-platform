"""
Jarvis Platform — Stage-72.0
Governance Dependency Graph & Circular Stability Validator

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Validates governance module dependency structure and detects
circular feedback patterns.

This module:
- Accepts declared dependency graph
- Detects circular references
- Detects excessive feedback depth
- Emits advisory structural validation signals
- Never executes corrective action

Design Guarantees:
------------------
- Deterministic graph validation
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
from typing import Dict, List, Set


class GovernanceDependencyValidator:
    """
    Stage-72.0 Structural Dependency Integrity Layer

    Protects against:
    - Circular module dependencies
    - Feedback loop amplification
    - Excessive advisory depth chains
    """

    VERSION = "72.0"

    MAX_FEEDBACK_DEPTH = 12

    def __init__(self):
        self._lock = threading.Lock()
        self._last_report = None
        self._structural_violation = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def validate(self, dependency_graph: Dict[str, List[str]]) -> Dict[str, any]:
        """
        Validate governance dependency graph.

        Parameters:
        -----------
        dependency_graph : dict
            { module_name: [list_of_dependencies] }

        Returns:
        --------
        Structural validation report.
        """

        with self._lock:
            circular_detected = self._detect_cycle(dependency_graph)
            excessive_depth = self._detect_excessive_depth(dependency_graph)

            containment_reason = self._evaluate_structure(
                circular_detected,
                excessive_depth
            )

            report = {
                "dependency_validator_version": self.VERSION,
                "circular_dependency_detected": circular_detected,
                "excessive_feedback_depth": excessive_depth,
                "structural_violation": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._last_report = report
            self._structural_violation = containment_reason is not None

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _detect_cycle(self, graph: Dict[str, List[str]]) -> bool:
        """
        Detect cycles using DFS.
        """
        visited: Set[str] = set()
        recursion_stack: Set[str] = set()

        def dfs(node: str) -> bool:
            if node not in visited:
                visited.add(node)
                recursion_stack.add(node)

                for neighbor in graph.get(node, []):
                    if neighbor not in visited and dfs(neighbor):
                        return True
                    elif neighbor in recursion_stack:
                        return True

            recursion_stack.remove(node)
            return False

        for node in graph:
            if dfs(node):
                return True

        return False

    def _detect_excessive_depth(self, graph: Dict[str, List[str]]) -> bool:
        """
        Detect overly deep dependency chains.
        """

        def depth(node: str, visited: Set[str]) -> int:
            if node in visited:
                return 0

            visited.add(node)
            depths = [depth(neighbor, visited.copy()) for neighbor in graph.get(node, [])]
            return 1 + max(depths, default=0)

        max_depth = 0
        for node in graph:
            max_depth = max(max_depth, depth(node, set()))

        return max_depth > self.MAX_FEEDBACK_DEPTH

    def _evaluate_structure(
        self,
        circular: bool,
        excessive_depth: bool
    ) -> str | None:

        if circular:
            return "CIRCULAR_DEPENDENCY_DETECTED"

        if excessive_depth:
            return "EXCESSIVE_FEEDBACK_CHAIN_DEPTH"

        return None

    def _recommended_action(self, reason: str | None) -> str:

        if reason == "CIRCULAR_DEPENDENCY_DETECTED":
            return "RESTRUCTURE_GOVERNANCE_FLOW_TO_REMOVE_CYCLE"

        if reason == "EXCESSIVE_FEEDBACK_CHAIN_DEPTH":
            return "SIMPLIFY_GOVERNANCE_DEPENDENCY_GRAPH"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, any]:
        return {
            "dependency_validator_version": self.VERSION,
            "structural_violation": self._structural_violation,
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_governance_dependency_validator() -> GovernanceDependencyValidator:
    """
    Backward compatible instantiation.
    """
    return GovernanceDependencyValidator()