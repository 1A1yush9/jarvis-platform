# app/market_expansion_engine.py

import time
import uuid
from typing import Dict, List


class MarketExpansionEngine:
    """
    Stage-7.3
    Detects new business expansion opportunities
    based on accumulated opportunity intelligence.
    """

    def __init__(self):
        self.expansion_targets: List[dict] = []

    # -----------------------------------
    def analyze_opportunities(self, opportunity_snapshot: dict):

        total_opportunities = opportunity_snapshot.get(
            "total_opportunities", 0
        )

        if total_opportunities < 3:
            return {"message": "Insufficient data for expansion analysis"}

        expansion = {
            "expansion_id": str(uuid.uuid4()),
            "market_hint": self._generate_market_hint(total_opportunities),
            "confidence_score": min(95, 50 + total_opportunities * 5),
            "discovered_at": time.time()
        }

        self.expansion_targets.append(expansion)
        return expansion

    # -----------------------------------
    def _generate_market_hint(self, volume):

        if volume > 15:
            return "High-growth digital marketing vertical"
        elif volume > 8:
            return "Emerging SME automation services"
        else:
            return "Niche content-driven market segment"

    # -----------------------------------
    def get_expansions(self):
        return self.expansion_targets

    # -----------------------------------
    def snapshot(self):
        return {
            "engine": "Autonomous Market Expansion Intelligence",
            "expansions_detected": len(self.expansion_targets)
        }