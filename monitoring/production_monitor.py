from datetime import datetime

from app.core.orchestrator.cognitive_orchestrator import (
    cognitive_orchestrator,
)
from app.core.executive.executive_decision_policy import (
    executive_decision_policy,
)
from app.core.autonomy.goal_registry import goal_registry
from app.core.strategy.strategic_resource_allocator import (
    strategic_resource_allocator,
)
from app.core.reflection.self_reflection_engine import (
    self_reflection_engine,
)


class ProductionMonitor:

    def build_status(self):

        state = cognitive_orchestrator.current_state
        policy = executive_decision_policy.state
        allocation = strategic_resource_allocator.current_allocation

        goals = list(goal_registry.goals.values())

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "system_status": "healthy" if state else "starting",

            "execution_mode": policy.mode.value,

            "allocation": {
                "stabilization": allocation.stabilization_weight,
                "optimization": allocation.optimization_weight,
                "expansion": allocation.expansion_weight,
            },

            "goal_metrics": {
                "active": len(goal_registry.list_active()),
                "total": len(goals),
            },

            "reflection": (
                self_reflection_engine.last_report.dict()
                if self_reflection_engine.last_report
                else None
            ),
        }


production_monitor = ProductionMonitor()
