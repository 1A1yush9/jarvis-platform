import logging
from datetime import datetime

from app.core.strategy.strategic_resource_allocator import (
    strategic_resource_allocator,
)
from app.core.autonomy.goal_registry import goal_registry
from .policy_models import ExecutionMode, ExecutivePolicyState

logger = logging.getLogger(__name__)


class ExecutiveDecisionPolicy:
    """
    Determines global autonomy behavior level.
    """

    def __init__(self):
        self.state = ExecutivePolicyState(
            mode=ExecutionMode.BALANCED,
            confidence=0.5,
        )

    # -------------------------------------------------
    # POLICY EVALUATION
    # -------------------------------------------------
    def evaluate(self):

        allocation = strategic_resource_allocator.current_allocation
        active_goals = goal_registry.list_active()

        risk_pressure = 0

        for g in active_goals:
            if "performance" in g.title.lower():
                risk_pressure += 1

        # -----------------------------
        # Policy Logic
        # -----------------------------
        if risk_pressure > 2 or allocation.stabilization_weight > 0.5:
            mode = ExecutionMode.SAFE
            confidence = 0.8

        elif allocation.expansion_weight > 0.45:
            mode = ExecutionMode.AGGRESSIVE
            confidence = 0.75

        else:
            mode = ExecutionMode.BALANCED
            confidence = 0.6

        self.state = ExecutivePolicyState(
            mode=mode,
            confidence=confidence,
            updated_at=datetime.utcnow(),
        )

        logger.info(f"[EDP] Mode updated → {mode}")

        return self.state


executive_decision_policy = ExecutiveDecisionPolicy()
