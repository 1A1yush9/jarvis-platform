import logging
from datetime import datetime

from app.core.executive.executive_decision_policy import (
    executive_decision_policy,
)
from app.core.strategy.strategic_resource_allocator import (
    strategic_resource_allocator,
)
from app.core.autonomy.goal_registry import goal_registry
from .cognitive_state import CognitiveState

logger = logging.getLogger(__name__)


class CognitiveOrchestrator:
    """
    Central awareness loop coordinating all brains.
    """

    def __init__(self):
        self.current_state = None

    # -------------------------------------------------
    # BUILD GLOBAL STATE
    # -------------------------------------------------
    def build_state(self):

        policy = executive_decision_policy.state
        allocation = strategic_resource_allocator.current_allocation
        active_goals = len(goal_registry.list_active())

        state = CognitiveState(
            timestamp=datetime.utcnow(),
            execution_mode=policy.mode.value,
            allocation={
                "stabilization": allocation.stabilization_weight,
                "optimization": allocation.optimization_weight,
                "expansion": allocation.expansion_weight,
            },
            active_goals=active_goals,
            system_status="healthy",
        )

        self.current_state = state

        logger.info(
            f"[Orchestrator] Mode={state.execution_mode} "
            f"Goals={active_goals}"
        )

        return state


cognitive_orchestrator = CognitiveOrchestrator()
