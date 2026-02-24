# app/core/deal_intelligence.py

from datetime import datetime
from typing import Dict, Any, List
import threading
import time
import random


class DealIntelligenceEngine:
    """
    Stage 9.3 — Autonomous Deal Intelligence Layer

    Converts acquisition opportunities into structured
    deal strategies with win probability estimation.
    """

    def __init__(self, client_acquisition=None, revenue_command=None):
        self.active = True
        self.client_acquisition = client_acquisition
        self.revenue_command = revenue_command

        self.state = {
            "mode": "evaluation",
            "last_analysis": None,
            "active_deal_focus": None
        }

        self.deal_pipeline: List[Dict[str, Any]] = []
        self.analysis_history: List[Dict[str, Any]] = []

        self.thread = threading.Thread(
            target=self._deal_loop,
            daemon=True
        )
        self.thread.start()

    # ---------------------------------------------------
    # MAIN LOOP
    # ---------------------------------------------------
    def _deal_loop(self):
        while self.active:
            try:
                deal = self._analyze_opportunity()

                if deal:
                    self.deal_pipeline.append(deal)
                    self.analysis_history.append(deal)

                    if len(self.analysis_history) > 150:
                        self.analysis_history.pop(0)

                    self.state["last_analysis"] = deal["timestamp"]

                    print(
                        f"[DealIntelligence] Strategy created → {deal['strategy_type']}"
                    )

                time.sleep(45)  # Render-safe pacing

            except Exception as e:
                print(f"[DealIntelligence ERROR] {e}")
                time.sleep(15)

    # ---------------------------------------------------
    # DEAL ANALYSIS
    # ---------------------------------------------------
    def _analyze_opportunity(self):

        if not self.client_acquisition:
            return None

        if not self.client_acquisition.lead_queue:
            return None

        lead = random.choice(self.client_acquisition.lead_queue)

        strategy_types = [
            "performance_marketing_package",
            "seo_growth_retainer",
            "full_stack_digital_transformation",
            "conversion_optimization_program",
            "brand_scaling_campaign"
        ]

        pricing_band = random.choice([
            "low_ticket",
            "mid_market",
            "premium"
        ])

        win_probability = random.randint(55, 92)

        deal = {
            "timestamp": datetime.utcnow().isoformat(),
            "industry": lead["industry"],
            "geo_target": lead["geo_target"],
            "strategy_type": random.choice(strategy_types),
            "pricing_band": pricing_band,
            "estimated_value": lead["estimated_value"],
            "win_probability": win_probability,
            "source": "Deal Intelligence Engine"
        }

        self.state["active_deal_focus"] = deal["strategy_type"]

        return deal

    # ---------------------------------------------------
    # PUBLIC STATUS
    # ---------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "deal_intelligence_active": self.active,
            "state": self.state,
            "pipeline_size": len(self.deal_pipeline),
            "history_size": len(self.analysis_history)
        }

    def shutdown(self):
        self.active = False