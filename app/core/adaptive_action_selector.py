# app/core/adaptive_action_selector.py

import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class AdaptiveActionSelector:
    """
    Chooses best action based on observer signal.
    """

    def select_action(self, signal: Dict[str, Any]) -> Dict[str, Any]:

        reason = signal.get("reason")

        action = {
            "action_type": "optimize_performance",
            "priority": "medium",
        }

        if reason == "conversion_drop":
            action = {"action_type": "optimize_ads", "priority": "high"}

        elif reason == "conversion_spike":
            action = {"action_type": "scale_budget", "priority": "high"}

        elif reason == "traffic_drop":
            action = {
                "action_type": "seo_recovery_campaign",
                "priority": "medium",
            }

        elif reason == "revenue_spike":
            action = {
                "action_type": "audience_expansion",
                "priority": "high",
            }

        elif reason == "unstable_metrics":
            action = {
                "action_type": "stabilize_campaign",
                "priority": "urgent",
            }

        logger.info(f"[ActionSelector] Selected action: {action}")

        return action
