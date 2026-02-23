# app/mesh_engine.py

import uuid
import time
from typing import List, Dict


class IntelligenceMeshEngine:
    """
    Stage-8.0
    Enables Jarvis nodes to operate as cooperative agents.
    """

    def __init__(self):
        self.agent_id = f"jarvis-node-{uuid.uuid4().hex[:8]}"
        self.known_agents: List[str] = []
        self.received_signals: List[dict] = []
        self.last_sync = 0

    # -----------------------------------
    def publish_signal(
        self,
        opportunity_snapshot: dict,
        revenue_snapshot: dict,
        expansion_snapshot: dict
    ):

        signal = {
            "agent_id": self.agent_id,
            "timestamp": time.time(),
            "opportunity_density": opportunity_snapshot.get(
                "total_opportunities", 0
            ),
            "revenue_level": revenue_snapshot.get(
                "tracked_revenue", 0
            ),
            "expansion_activity": expansion_snapshot.get(
                "expansions_detected", 0
            )
        }

        return signal

    # -----------------------------------
    def receive_signal(self, signal: dict):

        agent = signal.get("agent_id")

        if agent and agent not in self.known_agents:
            self.known_agents.append(agent)

        self.received_signals.append(signal)
        self.last_sync = time.time()

        return {
            "received_from": agent,
            "known_agents": len(self.known_agents)
        }

    # -----------------------------------
    def snapshot(self):
        return {
            "engine": "Global Intelligence Mesh",
            "agent_id": self.agent_id,
            "known_agents": len(self.known_agents),
            "signals_received": len(self.received_signals),
            "last_sync": self.last_sync
        }