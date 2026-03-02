"""
Executive Reasoning Orchestrator
Meta-Coordination Layer
(Stage 50.0 integrated)
"""

from typing import Dict, Any

from core.executive_autonomy_boundary import (
    ExecutiveAutonomyBoundary,
    AutonomyViolation
)


class ExecutiveReasoningOrchestrator:

    def __init__(
        self,
        intelligence_kernel,
        consensus_engine,
        decision_trace
    ):
        self.kernel = intelligence_kernel
        self.consensus = consensus_engine
        self.decision_trace = decision_trace

        # NEW — Final containment authority
        self.autonomy_boundary = ExecutiveAutonomyBoundary(
            decision_trace=self.decision_trace
        )

    # --------------------------------------------------

    def process(self, signal: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full cognitive lifecycle.
        """

        reasoning_output = self.kernel.process(signal)

        consensus_output = self.consensus.evaluate(reasoning_output)

        # FINAL STEP — CONTAINMENT VALIDATION
        safe_output = self.autonomy_boundary.validate_intent(
            consensus_output
        )

        return safe_output