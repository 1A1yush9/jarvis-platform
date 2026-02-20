# app/core/executive_dashboard_brain.py

from typing import Dict, Any
from datetime import datetime
from app.core.autonomy.goal_registry import goal_registry


class ExecutiveDashboardBrain:
    """
    Converts multi-brain outputs into a single
    executive-level intelligence report.
    """

    def build_report(
        "goal_overview": {
    "active_goals": len(goal_registry.list_active())
    }
        self,
        job_id: str,
        funnel: Dict[str, Any],
        roi: Dict[str, Any],
        budget: Dict[str, Any],
        optimization: Dict[str, Any],
        adaptive: Dict[str, Any],
        supervision: Dict[str, Any],
        memory_hint: Dict[str, Any],
        growth: Dict[str, Any],
    ) -> Dict[str, Any]:

        execution_mode = supervision.get(
            "final_execution_mode", "stable"
        )

        confidence = adaptive.get("confidence", 0)

        summary = self._generate_summary(
            execution_mode,
            roi,
            optimization,
            memory_hint
        )

        return {
            "job_id": job_id,
            "generated_at": datetime.utcnow().isoformat(),

            "executive_summary": summary,

            "ai_decisions": {
                "execution_mode": execution_mode,
                "risk_level": supervision.get("risk_level"),
                "confidence_score": confidence,
            },

            "performance_snapshot": {
                "predicted_roas": roi.get("predicted_roas"),
                "predicted_cpa": roi.get("predicted_cpa"),
                "stability_score": optimization.get("stability_score"),
            },

            "strategy_snapshot": {
                "selected_funnel": funnel.get("selected_funnel"),
                "budget_channels":
                    budget.get("channel_allocation", {}),
            },

            "learning_insight": memory_hint,
            "growth_recommendations":
                growth.get("opportunities", []),
        }

    # -------------------------------------------------
    # HUMAN READABLE SUMMARY
    # -------------------------------------------------
    def _generate_summary(
        self,
        execution_mode: str,
        roi: Dict[str, Any],
        optimization: Dict[str, Any],
        memory_hint: Dict[str, Any],
    ) -> str:

        roas = roi.get("predicted_roas", 0)
        stability = optimization.get("stability_score", 0)

        if execution_mode == "scale_mode":
            action = "AI recommends scaling campaign investment."
        elif execution_mode == "controlled_adaptation":
            action = "AI recommends controlled optimization."
        else:
            action = "AI recommends maintaining stable execution."

        memory_note = ""
        if memory_hint.get("recommended_funnel"):
            memory_note = (
                f" Historical learning favors "
                f"{memory_hint['recommended_funnel']} funnel."
            )

        return (
            f"Predicted ROAS is {round(roas,2)} with "
            f"stability score {round(stability,2)}. "
            f"{action}{memory_note}"
        )
