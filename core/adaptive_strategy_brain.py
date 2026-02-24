# app/core/adaptive_strategy_brain.py

from typing import Dict, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class AdaptiveStrategyBrain:
    """
    Adaptive Strategy Brain
    -----------------------
    Dynamically adjusts funnel, budget allocation,
    and execution strategy during workflow runtime.

    SAFE DESIGN:
    - No external imports from routers
    - No orchestrator imports (prevents circular deps)
    - Pure decision engine
    """

    def __init__(self):
        self.version = "4.43"
        self.min_confidence_threshold = 0.55

    # ---------------------------------------------------------
    # PUBLIC ENTRY
    # ---------------------------------------------------------
    def adapt_strategy(
        self,
        workflow_state: Dict[str, Any],
        performance_metrics: Dict[str, Any],
        roi_prediction: Dict[str, Any],
        optimization_feedback: Dict[str, Any],
        budget_plan: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Main adaptive decision engine.
        Never throws — always returns safe structure.
        """

        try:
            adjustment = {
                "timestamp": datetime.utcnow().isoformat(),
                "strategy_changed": False,
                "funnel_adjustment": None,
                "budget_adjustment": {},
                "execution_mode": "stable",
                "confidence": 0.0,
                "reasoning": [],
            }

            performance_score = self._evaluate_performance(
                performance_metrics,
                roi_prediction
            )

            learning_signal = self._evaluate_learning_signal(
                optimization_feedback
            )

            confidence = (performance_score + learning_signal) / 2
            adjustment["confidence"] = round(confidence, 3)

            # -------------------------------------------------
            # DECISION LOGIC
            # -------------------------------------------------

            # 1️⃣ Underperforming → aggressive optimization
            if confidence < 0.4:
                adjustment["strategy_changed"] = True
                adjustment["execution_mode"] = "aggressive_optimization"

                adjustment["funnel_adjustment"] = self._suggest_funnel_shift(
                    workflow_state
                )

                adjustment["budget_adjustment"] = \
                    self._reallocate_budget(budget_plan, boost_winners=True)

                adjustment["reasoning"].append(
                    "Low performance confidence detected."
                )

            # 2️⃣ Moderate → controlled adaptation
            elif confidence < self.min_confidence_threshold:
                adjustment["strategy_changed"] = True
                adjustment["execution_mode"] = "controlled_adaptation"

                adjustment["budget_adjustment"] = \
                    self._reallocate_budget(budget_plan, boost_winners=False)

                adjustment["reasoning"].append(
                    "Moderate performance — incremental tuning applied."
                )

            # 3️⃣ High performance → scale winners
            else:
                adjustment["execution_mode"] = "scale_mode"

                adjustment["budget_adjustment"] = \
                    self._scale_success_channels(budget_plan)

                adjustment["reasoning"].append(
                    "Strong performance — scaling successful channels."
                )

            return adjustment

        except Exception as e:
            logger.exception("AdaptiveStrategyBrain failure")

            # SAFE FALLBACK
            return {
                "strategy_changed": False,
                "execution_mode": "stable",
                "confidence": 0.0,
                "reasoning": [f"fallback_due_to_error: {str(e)}"]
            }

    # ---------------------------------------------------------
    # INTERNAL SCORING
    # ---------------------------------------------------------

    def _evaluate_performance(
        self,
        metrics: Dict[str, Any],
        roi_prediction: Dict[str, Any],
    ) -> float:

        conversion = metrics.get("conversion_rate", 0.0)
        ctr = metrics.get("ctr", 0.0)
        predicted_roi = roi_prediction.get("predicted_roi", 0.0)

        score = (
            conversion * 0.4 +
            ctr * 0.2 +
            predicted_roi * 0.4
        )

        return max(0.0, min(score, 1.0))

    def _evaluate_learning_signal(
        self,
        feedback: Dict[str, Any]
    ) -> float:

        improvement = feedback.get("performance_improvement", 0.0)
        stability = feedback.get("stability_score", 0.5)

        return max(0.0, min((improvement * 0.6 + stability * 0.4), 1.0))

    # ---------------------------------------------------------
    # STRATEGY ACTIONS
    # ---------------------------------------------------------

    def _suggest_funnel_shift(
        self,
        workflow_state: Dict[str, Any]
    ) -> Optional[str]:

        current = workflow_state.get("funnel_type", "unknown")

        fallback_map = {
            "awareness": "lead_generation",
            "lead_generation": "conversion",
            "conversion": "retargeting",
        }

        return fallback_map.get(current)

    def _reallocate_budget(
        self,
        budget_plan: Dict[str, Any],
        boost_winners: bool
    ) -> Dict[str, float]:

        adjusted = {}

        for channel, value in budget_plan.items():
            if boost_winners:
                adjusted[channel] = round(value * 1.15, 2)
            else:
                adjusted[channel] = round(value * 1.05, 2)

        return adjusted

    def _scale_success_channels(
        self,
        budget_plan: Dict[str, Any]
    ) -> Dict[str, float]:

        return {
            ch: round(v * 1.25, 2)
            for ch, v in budget_plan.items()
        }
