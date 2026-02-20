from datetime import datetime, timedelta


class GoalAgingPolicy:
    """
    Defines when goals become stale.
    """

    STALE_AFTER = timedelta(minutes=30)
    RETIRE_AFTER = timedelta(hours=2)

    def compute_age(self, goal):

        elapsed = datetime.utcnow() - goal.last_activity_at

        if elapsed > self.RETIRE_AFTER:
            return "retire"

        if elapsed > self.STALE_AFTER:
            return "age"

        return "active"


goal_aging_policy = GoalAgingPolicy()
