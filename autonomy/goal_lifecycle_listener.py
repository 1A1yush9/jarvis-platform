from .goal_registry import goal_registry
from .goal_models import GoalStatus
from .learning_models import GoalOutcome
from .goal_learning_engine import goal_learning_engine
from .predictive_engine import predictive_engine
from .goal_learning_memory import goal_learning_memory


class GoalLifecycleListener:

    def goal_completed(
    self,
    goal_id: str,
    success: bool,
    performance_delta: float,
    stability_delta: float,
):

    goal = goal_registry.goals.get(goal_id)
    if not goal:
        return

    # Update lifecycle
    goal_registry.update_status(goal_id, GoalStatus.COMPLETED)

    outcome = GoalOutcome(
        goal_id=goal_id,
        success=success,
        performance_delta=performance_delta,
        stability_delta=stability_delta,
    )

    # -----------------------------
    # LEARNING
    # -----------------------------
    goal_learning_engine.learn_from_outcome(goal, outcome)

    # -----------------------------
    # PREDICTIVE ANALYSIS (SAFE)
    # -----------------------------
    outcomes = goal_learning_memory.get_outcomes(goal_id)

    predictive_engine.analyze_metrics(
        [o.performance_delta for o in outcomes]
    )
