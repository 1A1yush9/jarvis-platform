# =====================================================
# Autonomous Growth Brain
# =====================================================

from typing import Dict, Any, List
from collections import defaultdict
import logging
import json
import os

logger = logging.getLogger(__name__)


class AutonomousGrowthBrain:
    """
    Strategic intelligence module.

    Analyzes historical strategic memory and discovers
    long-term growth opportunities.

    IMPORTANT:
    - Does NOT create goals
    - Does NOT trigger execution
    - Only produces advisory intelligence
    """

    MEMORY_PATH = "app/memory/strategic_memory.json"

    # -------------------------------------------------
    # LOAD MEMORY SAFELY
    # -------------------------------------------------
    def _load_memory(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.MEMORY_PATH):
            logger.info("[GrowthBrain] No strategic memory yet.")
            return []

        try:
            with open(self.MEMORY_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)

            campaigns = data.get("campaigns", [])

            if not isinstance(campaigns, list):
                logger.warning("[GrowthBrain] Invalid memory format")
                return []

            return campaigns

        except Exception as e:
            logger.warning(f"[GrowthBrain] Memory load failed: {e}")
            return []

    # -------------------------------------------------
    # HELPER: SAFE AVERAGE
    # -------------------------------------------------
    def _avg(self, values: List[float]) -> float:
        return sum(values) / len(values) if values else 0.0

    # -------------------------------------------------
    # MAIN ANALYSIS
    # -------------------------------------------------
    def discover_growth_opportunities(self) -> Dict[str, Any]:

        campaigns = self._load_memory()

        if not campaigns:
            return {
                "type": "growth_opportunity",
                "opportunities": [],
                "message": "Not enough historical data yet.",
                "total_campaigns_analyzed": 0,
            }

        industry_scores = defaultdict(list)
        funnel_scores = defaultdict(list)

        # ---------------------------------------------
        # Aggregate historical performance
        # ---------------------------------------------
        for c in campaigns:
            try:
                industry = c.get("industry")
                funnel = c.get("funnel")
                roas = float(c.get("roas", 0))

                if industry:
                    industry_scores[industry].append(roas)

                if funnel:
                    funnel_scores[funnel].append(roas)

            except Exception:
                continue

        # ---------------------------------------------
        # Compute averages
        # ---------------------------------------------
        industry_avg = {
            k: self._avg(v) for k, v in industry_scores.items()
        }

        funnel_avg = {
            k: self._avg(v) for k, v in funnel_scores.items()
        }

        if not industry_avg or not funnel_avg:
            return {
                "type": "growth_opportunity",
                "opportunities": [],
                "message": "Insufficient structured data.",
                "total_campaigns_analyzed": len(campaigns),
            }

        # ---------------------------------------------
        # Select best performers
        # ---------------------------------------------
        top_industries = sorted(
            industry_avg.items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        best_funnel = max(funnel_avg, key=funnel_avg.get)

        opportunities = []

        for industry, score in top_industries:
            opportunities.append({
                "industry": industry,
                "recommended_funnel": best_funnel,
                "expected_roas": round(score, 2),
                "confidence": round(min(score / 3.0, 1.0), 2),
                "reason": "Historical ROAS dominance detected"
            })

        logger.info(
            f"[GrowthBrain] {len(opportunities)} opportunities discovered"
        )

        # ---------------------------------------------
        # RETURN STRATEGIC SIGNAL (ADVISORY ONLY)
        # ---------------------------------------------
        return {
            "type": "growth_opportunity",
            "opportunities": opportunities,
            "total_campaigns_analyzed": len(campaigns),
        }


# Singleton instance (recommended pattern)
autonomous_growth_brain = AutonomousGrowthBrain()
