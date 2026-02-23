# app/execution_engine.py

import uuid
import time
from typing import Dict, List


class ExecutionEngine:

    def __init__(self):
        self.client_actions: Dict[str, List[dict]] = {}

    # ---------------------------------
    # Strategy Selection (Adaptive)
    # ---------------------------------
    def _generate_strategy(self, opportunity: dict, strategy_bias=None):

        priority = opportunity.get("priority", "LOW")

        strategies = {
            "HIGH": "Immediate campaign deployment with paid + organic amplification",
            "MEDIUM": "Launch validation experiment and content positioning",
            "LOW": "Monitor trend and prepare lightweight content assets",
        }

        base_strategy = strategies.get(priority)

        # Apply optimization bias if available
        if strategy_bias and strategy_bias.get(base_strategy, 0) > 0:
            return f"{base_strategy} (AI-Optimized)"

        return base_strategy

    # ---------------------------------
    # Create Execution Plan
    # ---------------------------------
    def create_execution_plan(
        self,
        client_id: str,
        opportunity: dict,
        strategy_bias=None
    ):

        strategy = self._generate_strategy(opportunity, strategy_bias)

        action = {
            "action_id": str(uuid.uuid4()),
            "client_id": client_id,
            "source_opportunity": opportunity["opportunity_id"],
            "title": f"Execute: {opportunity['title']}",
            "strategy": strategy,
            "status": "proposed",
            "created_at": time.time()
        }

        self.client_actions.setdefault(client_id, []).append(action)
        return action

    # ---------------------------------
    # Update Status
    # ---------------------------------
    def update_status(self, client_id: str, action_id: str, new_status: str):

        for action in self.client_actions.get(client_id, []):
            if action["action_id"] == action_id:
                action["status"] = new_status
                action["updated_at"] = time.time()
                return action

        return None

    # ---------------------------------
    def get_client_actions(self, client_id: str):
        return self.client_actions.get(client_id, [])

    def find_action(self, client_id: str, action_id: str):
        for action in self.client_actions.get(client_id, []):
            if action["action_id"] == action_id:
                return action
        return None

    # ---------------------------------
    def system_snapshot(self):
        total = sum(len(v) for v in self.client_actions.values())
        return {
            "engine": "Autonomous Execution Layer",
            "total_actions": total,
            "clients_active": len(self.client_actions)
        }