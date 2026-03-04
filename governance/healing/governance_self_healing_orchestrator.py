from typing import Dict

from .trust_recovery_engine import TrustRecoveryEngine
from .reintegration_policy_engine import ReintegrationPolicyEngine


class GovernanceSelfHealingOrchestrator:
    """
    Stage-118.0

    Governance self-healing controller.

    Responsibilities:

    - Restore trust scores
    - Evaluate reintegration eligibility
    - Produce governance recovery report

    No mutation authority over runtime systems.
    """

    def __init__(self):

        self.recovery = TrustRecoveryEngine()
        self.policy = ReintegrationPolicyEngine()

    def evaluate(self, security_report: Dict, fault_domain_status: Dict) -> Dict:

        trust_scores = security_report.get("trust_scores", {})

        isolated_nodes = fault_domain_status.get("isolated_nodes", [])

        recovered_scores = self.recovery.recover(trust_scores)

        reintegrated = self.policy.evaluate(
            recovered_scores,
            isolated_nodes
        )

        return {
            "recovered_trust_scores": recovered_scores,
            "reintegrated_nodes": reintegrated
        }