from typing import Dict, List
from .learning_models import GoalOutcome


class GoalLearningMemory:

    def __init__(self):
        self.history: Dict[str, List[GoalOutcome]] = {}

    def record_outcome(self, outcome: GoalOutcome):
        if outcome.goal_id not in self.history:
            self.history[outcome.goal_id] = []

        self.history[outcome.goal_id].append(outcome)

    def get_outcomes(self, goal_id: str):
        return self.history.get(goal_id, [])


goal_learning_memory = GoalLearningMemory()
