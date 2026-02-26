"""
Stage-25.0 — Executive Intent Modeling Engine (EIME)

Purpose:
Infer implicit executive intent using historical
alignment behavior stored in Strategic Memory.

Design:
- Advisory only
- Non-predictive execution
- Safe statistical inference
"""

from typing import Dict, Any, List
import json
import os


class ExecutiveIntentModel:
    def __init__(self, memory_file: str = "strategic_memory.json"):
        self.memory_file = memory_file
        self.version = "25.0"

    # --------------------------------------------------
    # Load Memory
    # --------------------------------------------------
    def _load_memory(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.memory_file):
            return []

        try:
            with open(self.memory_file, "r") as f:
                return json.load(f)
        except Exception:
            return []

    # --------------------------------------------------
    # Intent Inference
    # --------------------------------------------------
    def model_intent(self) -> Dict[str, Any]:

        history = self._load_memory()

        if len(history) < 8:
            return {
                "intent_status": "INSUFFICIENT_DATA",
                "intent_vector": {},
                "engine_version": self.version,
            }

        scores = [x.get("alignment_score", 0.5) for x in history[-20:]]

        avg_alignment = sum(scores) / len(scores)

        volatility = self._volatility(scores)

        intent_profile = self._classify_intent(avg_alignment, volatility)

        return {
            "intent_status": "MODELED",
            "intent_vector": intent_profile,
            "engine_version": self.version,
        }

    # --------------------------------------------------
    # Volatility Measurement
    # --------------------------------------------------
    def _volatility(self, scores: List[float]) -> float:
        mean = sum(scores) / len(scores)
        variance = sum((s - mean) ** 2 for s in scores) / len(scores)
        return variance ** 0.5

    # --------------------------------------------------
    # Intent Classification
    # --------------------------------------------------
    def _classify_intent(self, avg_alignment: float, volatility: float):

        if avg_alignment > 0.75:
            strategic_bias = "LONG_TERM_STABILITY"
        elif avg_alignment > 0.6:
            strategic_bias = "BALANCED_GROWTH"
        else:
            strategic_bias = "ADAPTIVE_EXPERIMENTATION"

        if volatility < 0.05:
            risk_profile = "LOW_VARIANCE_EXECUTION"
        elif volatility < 0.12:
            risk_profile = "MODERATE_ADAPTABILITY"
        else:
            risk_profile = "HIGH_EXPLORATION"

        return {
            "strategic_bias": strategic_bias,
            "risk_profile": risk_profile,
            "avg_alignment": round(avg_alignment, 3),
            "behavioral_volatility": round(volatility, 3),
        }