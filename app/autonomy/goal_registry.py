from typing import Dict, List
from datetime import datetime
from .goal_models import AutonomousGoal, GoalStatus


class GoalRegistry:

    def __init__(self):
        self.goals: Dict[str, AutonomousGoal] = {}

    def add_goal(self, goal: AutonomousGoal):
        self.goals[goal.id] = goal
        return goal

    def update_status(self, goal_id: str, status: GoalStatus):
    goal = self.goals.get(goal_id)
    if not goal:
        return None

    goal.status = status
    goal.updated_at = datetime.utcnow()
    goal.last_activity_at = datetime.utcnow()

    return goal

    def list_active(self) -> List[AutonomousGoal]:
        return [
            g for g in self.goals.values()
            if g.status not in ["completed", "failed", "cancelled"]
        ]


goal_registry = GoalRegistry()
