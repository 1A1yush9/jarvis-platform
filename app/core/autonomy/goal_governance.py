from .governance_models import GovernanceResult, GovernanceDecision
from .goal_deduplicator import goal_deduplicator
from .goal_conflict_resolver import goal_conflict_resolver
from .risk_engine import risk_engine


class GoalGovernance:

    MAX_ACTIVE_GOALS = 5
    RISK_THRESHOLD = 0.7

    def evaluate(self, goal):

        # Duplicate protection
        if goal_deduplicator.is_duplicate(goal):
            return GovernanceResult(
                decision=GovernanceDecision.REJECTED,
                reason="Duplicate goal detected",
                risk_score=0.2,
            )

        # Conflict protection
        if goal_conflict_resolver.has_conflict(goal):
            return GovernanceResult(
                decision=GovernanceDecision.REJECTED,
                reason="Conflicting goal exists",
                risk_score=0.5,
            )

        # Risk scoring
        risk = risk_engine.calculate_risk(goal)

        if risk > self.RISK_THRESHOLD:
            return GovernanceResult(
                decision=GovernanceDecision.DELAYED,
                reason="Risk too high",
                risk_score=risk,
            )

        return GovernanceResult(
            decision=GovernanceDecision.APPROVED,
            reason="Safe to execute",
            risk_score=risk,
        )


goal_governance = GoalGovernance()
