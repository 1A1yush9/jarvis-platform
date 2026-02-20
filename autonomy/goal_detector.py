from .goal_models import AutonomousGoal, GoalPriority
from .goal_registry import goal_registry


class GoalDetector:

    def analyze_signal(self, signal: dict):

        signal_type = signal.get("type")
        score = signal.get("score", 0)

        # SAFE RULE BASE (no AI hallucination)
        if signal_type == "performance_drop" and score > 0.7:
            goal = AutonomousGoal(
                title="Optimize Performance Bottleneck",
                description="Detected sustained performance degradation",
                source_signal=signal_type,
                confidence=score,
                priority=GoalPriority.HIGH,
                metadata=signal
            )
            return goal_registry.add_goal(goal)

        if signal_type == "conversion_opportunity":
            goal = AutonomousGoal(
                title="Improve Funnel Conversion",
                description="Observer detected optimization opportunity",
                source_signal=signal_type,
                confidence=score,
                priority=GoalPriority.MEDIUM,
                metadata=signal
            )
            return goal_registry.add_goal(goal)

        return None


goal_detector = GoalDetector()
