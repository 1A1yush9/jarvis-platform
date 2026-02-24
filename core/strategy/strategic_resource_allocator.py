import logging
from datetime import datetime

from app.core.autonomy.goal_registry import goal_registry
from app.core.strategy.growth_scheduler import growth_scheduler
from .allocation_models import ResourceAllocation

logger = logging.getLogger(__name__)


class StrategicResourceAllocator:
    """
    Executive-level balancing system.

    Determines how Jarvis distributes attention
    between fixing, optimizing, and expanding.
    """

    def __init__(self):
        self.current_allocation = ResourceAllocation(
            stabilization_weight=0.33,
            optimization_weight=0.33,
            expansion_weight=0.34,
        )

    # -------------------------------------------------
    # MAIN EVALUATION
    # -------------------------------------------------
    def evaluate(self):

        active_goals = goal_registry.list_active()
        growth_data = growth_scheduler.last_result

        stabilization_pressure = 0
        optimization_pressure = len(active_goals)
        expansion_pressure = 0

        # Detect risk-heavy environment
        for g in active_goals:
            if "performance" in g.title.lower():
                stabilization_pressure += 1

        # Growth opportunities exist
        if growth_data and growth_data["data"].get("opportunities"):
            expansion_pressure = len(
                growth_data["data"]["opportunities"]
            )

        total = (
            stabilization_pressure
            + optimization_pressure
            + expansion_pressure
            + 1
        )

        self.current_allocation = ResourceAllocation(
            stabilization_weight=stabilization_pressure / total,
            optimization_weight=optimization_pressure / total,
            expansion_weight=expansion_pressure / total,
        )

        logger.info(
            f"[SRA] Allocation updated: {self.current_allocation}"
        )

        return self.current_allocation


strategic_resource_allocator = StrategicResourceAllocator()
