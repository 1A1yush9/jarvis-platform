from .goal_learning_memory import goal_learning_memory


class GoalLearningEngine:

    def compute_success_score(self, outcomes):

        if not outcomes:
            return 0.5  # neutral baseline

        success_rate = sum(1 for o in outcomes if o.success) / len(outcomes)

        avg_perf = sum(o.performance_delta for o in outcomes) / len(outcomes)

        score = (success_rate * 0.7) + (avg_perf * 0.3)

        return max(0.0, min(score, 1.0))

    def learn_from_outcome(self, goal, outcome):

        goal_learning_memory.record_outcome(outcome)

        outcomes = goal_learning_memory.get_outcomes(goal.id)

        learned_score = self.compute_success_score(outcomes)

        # Adaptive confidence update
        goal.confidence = (goal.confidence * 0.6) + (learned_score * 0.4)

        print(
            f"[Learning] Updated confidence for {goal.id}: {goal.confidence}"
        )


goal_learning_engine = GoalLearningEngine()
