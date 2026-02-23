# app/execution_engine.py

import uuid
import time
from typing import Dict, List


class ExecutionEngine:
    """
    Stage-6.4 Autonomous Execution Layer
    Converts opportunities into controlled execution plans.
    """

    def __init__(self):
        self.client_actions: Dict[str, List[dict]] = {}

    # ---------------------------------
    # Build Execution Plan
    # ---------------------------------
    def create_execution_plan(self, client_id: str, opportunity: dict):

        action = {
            "action_id": str(uuid.uuid4()),
            "client_id": client_id,
            "source_opportunity": opportunity["opportunity_id"],
            "title": f"Execute: {opportunity['title']}",
            "strategy": self._generate_strategy(opportunity),
            "status": "proposed",
            "created_at": time.time()
        }

        self.client_actions.setdefault(client_id, []).append(action)
        return action

    # ---------------------------------
    # Strategy Generator
    # ---------------------------------
    def _generate_strategy(self, opportunity: dict):

        priority = opportunity.get("priority", "LOW")

        if priority == "HIGH":
            return "Immediate campaign deployment with paid + organic amplification"
        elif priority == "MEDIUM":
            return "Launch validation experiment and content positioning"
        else:
            return "Monitor trend and prepare lightweight content assets"

    # ---------------------------------
    # Status Update
    # ---------------------------------
    def update_status(self, client_id: str, action_id: str, new_status: str):

        actions = self.client_actions.get(client_id, [])

        for action in actions:
            if action["action_id"] == action_id:
                action["status"] = new_status
                action["updated_at"] = time.time()
                return action

        return None

    # ---------------------------------
    # Accessors
    # ---------------------------------
    def get_client_actions(self, client_id: str):
        return self.client_actions.get(client_id, [])

    def system_snapshot(self):
        total = sum(len(v) for v in self.client_actions.values())
        return {
            "engine": "Autonomous Execution Layer",
            "total_actions": total,
            "clients_active": len(self.client_actions)
        }