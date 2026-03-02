"""
Executive Reasoning Orchestrator
(Stage 57.0 Integrated)
"""

from typing import Dict, Any

from core.adaptive_load_regulator import AdaptiveLoadRegulator
from core.executive_autonomy_boundary import ExecutiveAutonomyBoundary
from core.governance_self_audit import GovernanceSelfAudit
from core.cognitive_integrity_monitor import CognitiveIntegrityMonitor
from core.meta_governance_sentinel import MetaGovernanceSentinel
from core.constitutional_resilience import ConstitutionalResilience
from core.predictive_stability_engine import PredictiveStabilityEngine
from core.system_coherence_engine import SystemCoherenceEngine


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

        self.load_regulator = AdaptiveLoadRegulator(decision_trace)
        self.resilience = ConstitutionalResilience(decision_trace)

        self.autonomy_boundary = ExecutiveAutonomyBoundary(decision_trace)

        self.self_audit = GovernanceSelfAudit(
            autonomy_boundary=self.autonomy_boundary,
            decision_trace=decision_trace,
            stability_regulator=stability_regulator,
        )

        self.integrity_monitor = CognitiveIntegrityMonitor(decision_trace)
        self.meta_sentinel = MetaGovernanceSentinel(decision_trace)
        self.predictive_engine = PredictiveStabilityEngine(decision_trace)

        # Stage-57
        self.coherence_engine = SystemCoherenceEngine(decision_trace)

    # --------------------------------------------------

    def process(self, signal: Dict[str, Any]) -> Dict[str, Any]:

        signal = self.load_regulator.regulate(signal)

        reasoning_output = self.kernel.process(signal)
        consensus_output = self.consensus.evaluate(reasoning_output)

        safe_output = self.autonomy_boundary.validate_intent(
            consensus_output
        )

        safe_output = self.resilience.protect(
            "governance_self_audit",
            lambda: self.self_audit.run_audit(safe_output),
            safe_output,
        )

        safe_output = self.resilience.protect(
            "cognitive_integrity_monitor",
            lambda: self.integrity_monitor.evaluate(safe_output),
            safe_output,
        )

        safe_output = self.resilience.protect(
            "meta_governance_sentinel",
            lambda: self.meta_sentinel.supervise(safe_output),
            safe_output,
        )

        safe_output = self.predictive_engine.evaluate(safe_output)

        # FINAL HARMONIZATION
        final_output = self.coherence_engine.harmonize(safe_output)

        return final_output


executive_reasoning_orchestrator = ExecutiveReasoningOrchestrator

__all__ = [
    "ExecutiveReasoningOrchestrator",
    "executive_reasoning_orchestrator",
]