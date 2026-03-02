"""
Executive Reasoning Orchestrator
Meta-Coordination Layer
(Stage 50.0 — Backward Compatible)

This orchestrator coordinates reasoning while enforcing
Executive Autonomy Boundary containment.
"""

from typing import Dict, Any

from core.executive_autonomy_boundary import (
    ExecutiveAutonomyBoundary,
    AutonomyViolation,
)


class ExecutiveReasoningOrchestrator:
    """
    Central meta-coordination engine.
    """

    def __init__(
        self,
        intelligence_kernel,
        consensus_engine,
        decision_trace,
    ):
        self.kernel = intelligence_kernel
        self.consensus = consensus_engine
        self.decision_trace = decision_trace

        # Final containment authority (Stage-50)
        self.autonomy_boundary = ExecutiveAutonomyBoundary(
            decision_trace=self.decision_trace
        )

    # --------------------------------------------------

    def process(self, signal: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full cognitive lifecycle pipeline.
        """

        # Step 1 — reasoning
        reasoning_output = self.kernel.process(signal)

        # Step 2 — consensus validation
        consensus_output = self.consensus.evaluate(reasoning_output)

        # Step 3 — FINAL containment gate
        safe_output = self.autonomy_boundary.validate_intent(
            consensus_output
        )

        return safe_output


# ======================================================
# BACKWARD COMPATIBILITY EXPORT (CRITICAL)
# Older stages import:
# from core.executive_reasoning_orchestrator import executive_reasoning_orchestrator
# ======================================================

# Alias keeps legacy imports working safely
executive_reasoning_orchestrator = ExecutiveReasoningOrchestrator

__all__ = [
    "ExecutiveReasoningOrchestrator",
    "executive_reasoning_orchestrator",
]