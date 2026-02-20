from app.executive.executive import executive_brain
from app.planning.planner import planning_brain
from app.intuition.intuition import intuition_brain
from app.conscious.conscious import conscious_brain

try:
    from app.agents.intelligence.intelligence import agent_intelligence
except Exception:
    agent_intelligence = None


class BrainService:

    def status(self):

        return {
            "executive_active": executive_brain is not None,
            "planning_active": planning_brain is not None,
            "intuition_active": intuition_brain is not None,
            "conscious_mode": conscious_brain.state.mode,
            "confidence": conscious_brain.state.confidence,
            "stress": conscious_brain.state.stress,
        }

    def plans(self):
        return {
            "active_plans": list(planning_brain.store.plans.keys())
        }

    def agents(self):
        if not agent_intelligence:
            return {"agents": []}

        return {
            "agents": [
                {
                    "name": k,
                    "score": v.performance_score,
                    "health": getattr(v, "health_state", "unknown"),
                }
                for k, v in agent_intelligence.store.stats.items()
            ]
        }

    def intuition(self):
        return {
            "patterns": len(intuition_brain.store.patterns)
        }


brain_service = BrainService()
