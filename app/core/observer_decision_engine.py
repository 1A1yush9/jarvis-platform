# app/core/observer_decision_engine.py

import logging
from typing import Dict, Any
from app.core.autonomy.autonomous_goal_engine import autonomous_goal_engine
from app.core.adaptive_strategy_brain import AdaptiveStrategyBrain
from app.core.meta_strategy_supervisor import MetaStrategySupervisor
from app.core.reaction_task_manager import ReactionTaskManager
from app.core.observer_signal_guard import ObserverSignalGuard

logger = logging.getLogger(__name__)


class ObserverDecisionEngine:
    """
    Converts observer signals into Jarvis decisions
    and triggers autonomous reactions.
    """

    def __init__(self):
        self.adaptive_brain = AdaptiveStrategyBrain()
        self.supervisor = MetaStrategySupervisor()
        self.reaction_manager = ReactionTaskManager()
        self.signal_guard = ObserverSignalGuard()

    # -------------------------------------------------
    # MAIN ENTRY
    # -------------------------------------------------
    def process_signal(self, signal: Dict[str, Any]):

    status = signal.get("status")

    # Ignore stable signals
    if status == "stable":
        return

    # Anti-loop protection
    if not self.signal_guard.allow_trigger(signal):
        return

    # ✅ SAFE PLACE — observer approved signal
    autonomous_goal_engine.process_observer_signal(signal)

    logger.info(f"[DecisionEngine] Processing signal: {signal}")

    try:
        # -----------------------------------------
        # Minimal synthetic state (starter logic)
        # -----------------------------------------
        workflow_state = {"funnel_type": "lead_generation"}

        performance_metrics = {
            "conversion_rate":
                signal.get("data", {}).get("conversions", 0) / 100,
            "ctr": 0.02,
        }

        roi_prediction = {"predicted_roi": 1.5}

        optimization_feedback = {
            "performance_improvement": 0.5,
            "stability_score": 0.6,
        }

        budget_plan = {
            "meta_ads": 1000,
            "google_ads": 1000,
        }

        # -----------------------------------------
        # Adaptive Strategy
        # -----------------------------------------
        adaptive_result = self.adaptive_brain.adapt_strategy(
            workflow_state,
            performance_metrics,
            roi_prediction,
            optimization_feedback,
            budget_plan,
        )

        # -----------------------------------------
        # Meta Supervision
        # -----------------------------------------
        supervisor_result = self.supervisor.supervise(
            funnel_strategy={"selected_funnel": "lead_generation"},
            roi_prediction={"predicted_roas": 1.5},
            budget_decision={"channel_allocation": budget_plan},
            optimization_result={"stability_score": 0.6},
            adaptive_strategy=adaptive_result,
        )

        logger.info(
            f"[DecisionEngine] Final decision: {supervisor_result}"
        )

        # ✅ Autonomous Reaction Trigger
        self.reaction_manager.create_reaction(signal)

    except Exception as e:
        logger.error(
            f"[DecisionEngine] Processing failed: {str(e)}"
        )
