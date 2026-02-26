"""
Jarvis Platform API
Production Safe — Stage 18.5 Integrated
"""

from fastapi import FastAPI
from typing import Dict, Any, List

from core.strategic_alignment_engine import StrategicAlignmentEngine
from core.adaptive_strategy_memory import AdaptiveStrategyMemory
from core.predictive_stability_engine import PredictiveStabilityEngine

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="18.5",
)

# -----------------------------------------------------
# Engine Initialization
# -----------------------------------------------------

alignment_engine = StrategicAlignmentEngine()
adaptive_memory = AdaptiveStrategyMemory()
predictive_engine = PredictiveStabilityEngine()


# -----------------------------------------------------
# Root Health
# -----------------------------------------------------
@app.get("/")
def root():
    return {
        "platform": "Jarvis",
        "status": "LIVE",
        "mode": "advisory_only",
        "stage": "18.5",
    }


# -----------------------------------------------------
# Alignment Engine
# -----------------------------------------------------
@app.get("/alignment/status")
def alignment_status():
    return alignment_engine.status()


@app.post("/alignment/evaluate")
def evaluate_alignment(payload: Dict[str, Any]):

    decisions: List[Dict[str, Any]] = payload.get("decisions", [])

    objectives = payload.get(
        "objectives",
        {
            "revenue_focus": True,
            "safety_priority": True,
        },
    )

    result = alignment_engine.evaluate_alignment(
        decisions=decisions,
        platform_objectives=objectives,
    )

    return result


# -----------------------------------------------------
# Adaptive Memory
# -----------------------------------------------------
@app.post("/memory/record")
def record_alignment(payload: Dict[str, Any]):
    return adaptive_memory.record_alignment_event(payload)


@app.get("/memory/analyze")
def analyze_memory():
    return adaptive_memory.analyze_trends()


@app.get("/memory/status")
def memory_status():
    return adaptive_memory.status()


# -----------------------------------------------------
# Predictive Stability Engine
# -----------------------------------------------------
@app.get("/predictive/status")
def predictive_status():
    return predictive_engine.status()


@app.get("/predictive/forecast")
def predictive_forecast():
    return predictive_engine.forecast()