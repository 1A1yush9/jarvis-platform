# app/consensus_engine.py

from typing import Dict, List


class DistributedConsensusEngine:
    """
    Stage-8.1
    Builds global strategic bias from mesh signals.
    """

    def __init__(self):
        self.mesh_history: List[dict] = []

    # -----------------------------------
    def ingest_mesh_signal(self, signal: dict):
        self.mesh_history.append(signal)

    # -----------------------------------
    def consensus_bias(self) -> Dict[str, float]:

        if not self.mesh_history:
            return {}

        total_opportunities = sum(
            s.get("opportunity_density", 0)
            for s in self.mesh_history
        )

        total_revenue = sum(
            s.get("revenue_level", 0)
            for s in self.mesh_history
        )

        expansion_activity = sum(
            s.get("expansion_activity", 0)
            for s in self.mesh_history
        )

        count = len(self.mesh_history)

        return {
            "growth_mode": total_opportunities / max(count, 1),
            "optimization_mode": total_revenue / max(count, 1),
            "exploration_mode": expansion_activity / max(count, 1),
        }

    # -----------------------------------
    def snapshot(self):
        return {
            "engine": "Distributed Learning Consensus",
            "signals_processed": len(self.mesh_history)
        }