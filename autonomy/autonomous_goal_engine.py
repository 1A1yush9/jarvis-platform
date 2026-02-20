from .goal_detector import goal_detector
from .goal_registry import goal_registry
from .goal_models import GoalStatus
from .goal_governance import goal_governance
from .governance_models import GovernanceDecision


class AutonomousGoalEngine:
    """
    Converts approved observer signals into
    governed autonomous goals.
    """

    # -------------------------------------------------
    # MAIN ENTRY (called by ObserverDecisionEngine)
    # -------------------------------------------------
    def process_observer_signal(self, signal: dict):

        # Detect goal from observer signal
        goal = goal_detector.analyze_signal(signal)

        if not goal:
            return None

        # -----------------------------
        # GOVERNANCE CHECK
        # -----------------------------
        result = goal_governance.evaluate(goal)

        if result.decision != GovernanceDecision.APPROVED:
            print(f"[Governance] Goal blocked: {result.reason}")
            return goal

        # Approved → lifecycle continues
        goal_registry.update_status(goal.id, GoalStatus.VALIDATED)

        # Send into planning pipeline
        self.send_to_planner(goal)

        return goal

    # -------------------------------------------------
    # PLANNER HANDOFF (NON-BREAKING)
    # -------------------------------------------------
    def send_to_planner(self, goal):
        """
        Emits planning event without modifying
        existing planning brain behavior.
        """

        print(f"[AGE] Sending goal {goal.id} to Planning Brain")

        goal_registry.update_status(goal.id, GoalStatus.PLANNED)


# Singleton instance
autonomous_goal_engine = AutonomousGoalEngine()
