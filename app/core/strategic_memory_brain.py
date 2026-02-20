# app/core/strategic_memory_brain.py

import json
import os
from typing import Dict, Any, List
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class StrategicMemoryBrain:
    """
    Persistent campaign intelligence memory.

    Stores historical outcomes and provides
    guidance signals for future workflows.
    """

    MEMORY_PATH = "app/memory/strategic_memory.json"

    def __init__(self):
        self._ensure_memory()

    # -------------------------------------------------
    # MEMORY FILE SAFETY
    # -------------------------------------------------
    def _ensure_memory(self):
        os.makedirs("app/memory", exist_ok=True)

        if not os.path.exists(self.MEMORY_PATH):
            with open(self.MEMORY_PATH, "w") as f:
                json.dump({"campaigns": []}, f)

    def _load(self) -> Dict[str, Any]:
        try:
            with open(self.MEMORY_PATH, "r") as f:
                return json.load(f)
        except Exception:
            logger.warning("Memory corrupted — resetting")
            return {"campaigns": []}

    def _save(self, data: Dict[str, Any]):
        with open(self.MEMORY_PATH, "w") as f:
            json.dump(data, f, indent=2)

    # -------------------------------------------------
    # STORE OUTCOME
    # -------------------------------------------------
    def remember_campaign(
        self,
        industry: str,
        funnel: str,
        roas: float,
        stability: float,
        execution_mode: str,
    ):

        data = self._load()

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "industry": industry,
            "funnel": funnel,
            "roas": roas,
            "stability": stability,
            "execution_mode": execution_mode,
        }

        data["campaigns"].append(entry)

        # keep last 500 campaigns only
        data["campaigns"] = data["campaigns"][-500:]

        self._save(data)

    # -------------------------------------------------
    # MEMORY INSIGHTS
    # -------------------------------------------------
    def get_strategy_hint(self, industry: str) -> Dict[str, Any]:

        data = self._load()
        campaigns: List[Dict[str, Any]] = data.get("campaigns", [])

        industry_data = [
            c for c in campaigns if c["industry"] == industry
        ]

        if not industry_data:
            return {"confidence": 0, "recommended_funnel": None}

        funnel_scores = {}

        for c in industry_data:
            funnel_scores.setdefault(c["funnel"], []).append(c["roas"])

        avg_scores = {
            f: sum(v) / len(v)
            for f, v in funnel_scores.items()
        }

        best_funnel = max(avg_scores, key=avg_scores.get)

        return {
            "confidence": round(len(industry_data) / 20, 2),
            "recommended_funnel": best_funnel,
            "avg_roas": round(avg_scores[best_funnel], 2),
        }
