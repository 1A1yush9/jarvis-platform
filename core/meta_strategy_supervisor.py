# app/core/meta_strategy_supervisor.py

from typing import Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class MetaStrategySupervisor:
    """
    Global decision governor.

    Validates decisions coming from all brains and
    prevents conflicting or risky execution.
    """

    def __init__(self):
        self.version = "4.44"

    # -------------------------------------------------
    # PUBLIC ENTRY
    # -------------------------------------------------
    def supervise(
        self,
        funnel_strategy: Dict[str, Any],
        roi_prediction: Dict[str, Any],
        budget_decision: Dict[str, Any],
        optimization_result: Dict[str, Any],
        adaptive_strategy: Dict[str, Any],
    ) -> Dict[str, Any]:

        try:
            decision = {
                "timestamp": datetime.utcnow().isoformat(),
                "final_execution_mode":
                    adaptive_strategy.get("execution_mode", "stable"),
                "risk_level": "low",
                "overrides_applied": [],
                "approved": True,
            }

            predicted_roas = roi_prediction.get("predicted_roas", 0)
            stability = optimization_result.get("stability_score", 0.5)
            strategy_mode = decision["final_execution_mode"]

            # ---------------------------------------------
            # RULE 1 — Prevent scaling if ROI weak
            # ---------------------------------------------
            if predicted_roas < 1.2 and strategy_mode == "scale_mode":
                decision["final_execution_mode"] = "controlled_adaptation"
                decision["overrides_applied"].append(
                    "Scaling blocked due to weak ROI"
                )
                decision["risk_level"] = "medium"

            # ---------------------------------------------
            # RULE 2 — Stability protection
            # ---------------------------------------------
            if stability < 0.4:
                decision["final_execution_mode"] = "stable"
                decision["overrides_applied"].append(
                    "Low stability — forcing safe mode"
                )
                decision["risk_level"] = "high"

            # ---------------------------------------------
            # RULE 3 — Budget sanity check
            # ---------------------------------------------
            allocation = budget_decision.get(
                "channel_allocation", {}
            )

            total_budget = sum(allocation.values()) if allocation else 0

            if total_budget > 0 and predicted_roas < 1:
                decision["overrides_applied"].append(
                    "Budget risk detected"
                )
                decision["risk_level"] = "high"

            # ---------------------------------------------
            # RULE 4 — Funnel mismatch correction
            # ---------------------------------------------
            funnel = funnel_strategy.get("selected_funnel", "")

            if funnel == "conversion" and predicted_roas < 1:
                decision["final_execution_mode"] = "stable"
                decision["overrides_applied"].append(
                    "Conversion funnel downgraded due to poor ROI"
                )

            return decision

        except Exception as e:
            logger.exception("MetaStrategySupervisor failure")

            return {
                "approved": False,
                "final_execution_mode": "stable",
                "risk_level": "high",
                "overrides_applied": [f"fallback:{str(e)}"],
            }
