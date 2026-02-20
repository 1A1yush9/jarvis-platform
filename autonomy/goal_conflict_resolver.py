from .goal_registry import goal_registry


class GoalConflictResolver:

    CONFLICT_MAP = {
        "Scale Ad Spend": ["Reduce Budget"],
        "Reduce Budget": ["Scale Ad Spend"],
    }

    def has_conflict(self, new_goal):

        active = goal_registry.list_active()

        for goal in active:
            conflicts = self.CONFLICT_MAP.get(new_goal.title, [])
            if goal.title in conflicts:
                return True

        return False


goal_conflict_resolver = GoalConflictResolver()
