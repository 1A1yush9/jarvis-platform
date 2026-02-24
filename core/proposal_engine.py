# app/core/proposal_engine.py

from datetime import datetime
from typing import Dict, Any, List
import threading
import time
import random


class ProposalGenerationEngine:
    """
    Stage 9.4 — Autonomous Proposal Generation Engine

    Converts deal intelligence outputs into structured
    proposal blueprints ready for review.
    """

    def __init__(self, deal_intelligence=None):
        self.active = True
        self.deal_intelligence = deal_intelligence

        self.state = {
            "mode": "proposal_generation",
            "last_proposal": None,
            "active_template": None
        }

        self.proposal_pipeline: List[Dict[str, Any]] = []
        self.history: List[Dict[str, Any]] = []

        self.thread = threading.Thread(
            target=self._proposal_loop,
            daemon=True
        )
        self.thread.start()

    # ---------------------------------------------------
    # MAIN LOOP
    # ---------------------------------------------------
    def _proposal_loop(self):
        while self.active:
            try:
                proposal = self._generate_proposal()

                if proposal:
                    self.proposal_pipeline.append(proposal)
                    self.history.append(proposal)

                    if len(self.history) > 150:
                        self.history.pop(0)

                    self.state["last_proposal"] = proposal["timestamp"]

                    print(
                        f"[ProposalEngine] Proposal created → {proposal['offer_type']}"
                    )

                time.sleep(50)  # Render-safe pacing

            except Exception as e:
                print(f"[ProposalEngine ERROR] {e}")
                time.sleep(15)

    # ---------------------------------------------------
    # PROPOSAL CREATION
    # ---------------------------------------------------
    def _generate_proposal(self):

        if not self.deal_intelligence:
            return None

        if not self.deal_intelligence.deal_pipeline:
            return None

        deal = random.choice(self.deal_intelligence.deal_pipeline)

        offer_types = [
            "growth_retainer_package",
            "performance_marketing_bundle",
            "seo_authority_program",
            "brand_scale_framework",
            "conversion_acceleration_plan"
        ]

        delivery_models = [
            "monthly_retainer",
            "milestone_based",
            "hybrid_execution",
            "performance_linked"
        ]

        proposal = {
            "timestamp": datetime.utcnow().isoformat(),
            "industry": deal["industry"],
            "geo_target": deal["geo_target"],
            "offer_type": random.choice(offer_types),
            "delivery_model": random.choice(delivery_models),
            "pricing_band": deal["pricing_band"],
            "estimated_value": deal["estimated_value"],
            "win_probability": deal["win_probability"],
            "source": "Proposal Generation Engine"
        }

        self.state["active_template"] = proposal["offer_type"]

        return proposal

    # ---------------------------------------------------
    # PUBLIC STATUS
    # ---------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "proposal_engine_active": self.active,
            "state": self.state,
            "proposal_pipeline_size": len(self.proposal_pipeline),
            "history_size": len(self.history)
        }

    def shutdown(self):
        self.active = False