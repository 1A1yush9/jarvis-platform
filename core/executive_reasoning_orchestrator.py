"""
Executive Reasoning Orchestrator
(Stage 51.0 Integrated)
"""

from typing import Dict, Any

from core.executive_autonomy_boundary import (
    ExecutiveAutonomyBoundary,
)

from core.governance_self_audit import GovernanceSelfAudit


class ExecutiveReasoningOrchestrator:

    def __init__(
        self,
        intelligence_kernel,
        consensus_engine,
        decision_trace,
        stability_regulator=None,
    ):
        self.kernel = intelligence_kernel
        self.consensus = consensus_engine
        self.decision_trace = decision_trace

        # Stage-50 containment
        self.autonomy_boundary = ExecutiveAutonomyBoundary(
            decision_trace=self.decision_trace
        )

        # Stage-51 governance audit
        self.self_audit = GovernanceSelfAudit(
            autonomy_boundary=self.autonomy_boundary,
            decision_trace=self.decision_trace,
            stability_regulator=stability_regulator,
        )

    # --------------------------------------------------

    def process(self, signal: Dict[str, Any]) -> Dict[str, Any]:

        reasoning_output = self.kernel.process(signal)

        consensus_output = self.consensus.evaluate(reasoning_output)

        # Stage-50 containment
        safe_output = self.autonomy_boundary.validate_intent(
            consensus_output
        )

        # Stage-51 continuous verification
        audited_output = self.self_audit.run_audit(safe_output)

        return audited_output


# Backward compatibility export
executive_reasoning_orchestrator = ExecutiveReasoningOrchestrator

__all__ = [
    "ExecutiveReasoningOrchestrator",
    "executive_reasoning_orchestrator",
]