"""
Executive Reasoning Orchestrator
(Stage 54.0 Integrated)
"""

from typing import Dict, Any

from core.executive_autonomy_boundary import ExecutiveAutonomyBoundary
from core.governance_self_audit import GovernanceSelfAudit
from core.cognitive_integrity_monitor import CognitiveIntegrityMonitor
from core.meta_governance_sentinel import MetaGovernanceSentinel
from core.constitutional_resilience import ConstitutionalResilience


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

        # Stage-54 resilience
        self.resilience = ConstitutionalResilience(
            decision_trace=self.decision_trace
        )

        # Stage-50
        self.autonomy_boundary = ExecutiveAutonomyBoundary(
            decision_trace=self.decision_trace
        )

        # Stage-51
        self.self_audit = GovernanceSelfAudit(
            autonomy_boundary=self.autonomy_boundary,
            decision_trace=self.decision_trace,
            stability_regulator=stability_regulator,
        )

        # Stage-52
        self.integrity_monitor = CognitiveIntegrityMonitor(
            decision_trace=self.decision_trace
        )

        # Stage-53
        self.meta_sentinel = MetaGovernanceSentinel(
            decision_trace=self.decision_trace
        )

    # --------------------------------------------------

    def process(self, signal: Dict[str, Any]) -> Dict[str, Any]:

        reasoning_output = self.kernel.process(signal)

        consensus_output = self.consensus.evaluate(reasoning_output)

        safe_output = self.autonomy_boundary.validate_intent(
            consensus_output
        )

        audited_output = self.resilience.protect(
            "governance_self_audit",
            lambda: self.self_audit.run_audit(safe_output),
            safe_output,
        )

        integrity_output = self.resilience.protect(
            "cognitive_integrity_monitor",
            lambda: self.integrity_monitor.evaluate(audited_output),
            audited_output,
        )

        supervised_output = self.resilience.protect(
            "meta_governance_sentinel",
            lambda: self.meta_sentinel.supervise(integrity_output),
            integrity_output,
        )

        return supervised_output


# Backward compatibility export
executive_reasoning_orchestrator = ExecutiveReasoningOrchestrator

__all__ = [
    "ExecutiveReasoningOrchestrator",
    "executive_reasoning_orchestrator",
]