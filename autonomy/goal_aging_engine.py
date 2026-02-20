from datetime import datetime
from .goal_registry import goal_registry
from .goal_models import GoalStatus
from .goal_aging_policy import goal_aging_policy


class GoalAgingEngine:

    def run_cycle(self):

        for goal in goal_registry.goals.values():

            action = goal_aging_policy.compute_age(goal)

            if action == "age" and goal.status not in [
                GoalStatus.COMPLETED,
                GoalStatus.RETIRED,
            ]:
                goal.status = GoalStatus.AGED

            if action == "retire":
                goal.status = GoalStatus.RETIRED

            goal.updated_at = datetime.utcnow()


goal_aging_engine = GoalAgingEngine()
