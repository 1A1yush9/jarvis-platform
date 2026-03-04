from typing import Dict

from .fault_domain_registry import FaultDomainRegistry
from .isolation_policy_engine import IsolationPolicyEngine


class GovernanceFaultIsolator:
    """
    Stage-117.0

    Deterministically isolates unreliable governance nodes.

    Responsibilities

    - Evaluate security trust scores
    - Identify isolation candidates
    - Register nodes in fault domain registry

    No network mutation authority.
    """

    def __init__(self):

        self.registry = FaultDomainRegistry()
        self.policy = IsolationPolicyEngine()

    def evaluate(self, security_report: Dict) -> Dict:

        policy = self.policy.evaluate(security_report)

        isolated = []

        for candidate in policy["isolation_candidates"]:

            node = candidate["node"]

            self.registry.isolate(node, candidate["reason"])

            isolated.append(node)

        return {
            "isolated_nodes": isolated,
            "fault_domain_registry": self.registry.snapshot()
        }