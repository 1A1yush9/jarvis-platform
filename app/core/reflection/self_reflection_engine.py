import logging
from datetime import datetime

from app.core.autonomy.goal_registry import goal_registry
from app.core.executive.executive_decision_policy import (
    executive_decision_policy,
)
from .reflection_models import ReflectionReport

logger = logging.getLogger(__name__)


class SelfReflectionEngine:
    """
    Evaluates long-term effectiveness of Jarvis decisions.
    """

    def __init__(self):
        self.last_report = None

    # -------------------------------------------------
    # MAIN REFLECTION
    # -------------------------------------------------
    def reflect(self):

        goals = list(goal_registry.goals.values())

        if not goals:
            return None

        completed = [
            g for g in goals if g.status.value == "completed"
        ]

        success_rate = len(completed) / max(len(goals), 1)

        # simple stability proxy
        stability_score = 1.0 - min(len(goals) / 20, 1.0)

        # policy recommendation
        if success_rate < 0.4:
            bias = "more_conservative"
        elif success_rate > 0.7:
            bias = "more_aggressive"
        else:
            bias = "balanced"

        report = ReflectionReport(
            timestamp=datetime.utcnow(),
            success_rate=round(success_rate, 2),
            stability_score=round(stability_score, 2),
            recommended_mode_bias=bias,
            notes="System-level reflection completed",
        )

        self.last_report = report

        logger.info(
            f"[Reflection] Success={report.success_rate} "
            f"Bias={bias}"
        )

        return report


self_reflection_engine = SelfReflectionEngine()
