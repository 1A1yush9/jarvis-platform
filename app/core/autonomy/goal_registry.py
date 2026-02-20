from typing import Dict, List
from datetime import datetime
from .goal_models import AutonomousGoal, GoalStatus


# =====================================================
# Goal Registry (Stable Version)
# =====================================================

class GoalRegistry:

    def __init__(self):
        self.goals: Dict[str, AutonomousGoal] = {}

    # ---------------------------------
    # Get goal
    # ---------------------------------
    def get_goal(self, goal_id: str):
        return self.goals.get(goal_id)

    # ---------------------------------
    # Add goal
    # ---------------------------------
    def add_goal(self, goal_id: str, data: AutonomousGoal):
        self.goals[goal_id] = data

    # ---------------------------------
    # Update status
    # ---------------------------------
    def update_status(self, goal_id: str, status: GoalStatus):
        goal = self.goals.get(goal_id)
        if not goal:
            return None

        goal.status = status
        goal.updated_at = datetime.utcnow()
        goal.last_activity_at = datetime.utcnow()

        return goal

    # ---------------------------------
    # List active goals
    # ---------------------------------
    def list_active(self) -> List[AutonomousGoal]:
        return [
            g for g in self.goals.values()
            if g.status not in ["completed", "failed", "cancelled"]
        ]


# Global singleton
goal_registry = GoalRegistry()