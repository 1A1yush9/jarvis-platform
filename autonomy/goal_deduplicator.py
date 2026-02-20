from typing import List
from .goal_registry import goal_registry


class GoalDeduplicator:

    def is_duplicate(self, new_goal) -> bool:
        active_goals = goal_registry.list_active()

        for goal in active_goals:
            if (
                goal.title == new_goal.title and
                goal.source_signal == new_goal.source_signal
            ):
                return True

        return False


goal_deduplicator = GoalDeduplicator()
