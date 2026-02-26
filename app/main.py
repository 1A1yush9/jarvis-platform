"""
Jarvis Platform API
Production Safe — Stage 19.0 Integrated
"""

from fastapi import FastAPI
from typing import Dict, Any, List

from core.strategic_alignment_engine import StrategicAlignmentEngine
from core.adaptive_strategy_memory import AdaptiveStrategyMemory
from core.predictive_stability_engine import PredictiveStabilityEngine
from core.executive_dashboard_api import ExecutiveDashboardAPI

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="19.0",
)

# -----------------------------------------------------
# Engine Initialization
# -----------------------------------------------------

alignment_engine = StrategicAlignmentEngine()
adaptive_memory = AdaptiveStrategyMemory()
predictive_engine = PredictiveStabilityEngine()

dashboard_api = ExecutiveDashboardAPI(
    alignment_engine,
    adaptive_memory,
    predictive_engine,
)

# -----------------------------------------------------
# Root
# -----------------------------------------------------
@app.get("/")
def root():
    return {
        "platform": "Jarvis",
        "status": "LIVE",
        "mode": "advisory_only",
        "stage": "19.0",
    }


# -----------------------------------------------------
# Alignment
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

    return alignment_engine.evaluate_alignment(
        decisions,
        objectives,
    )


# -----------------------------------------------------
# Memory
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
# Predictive Stability
# -----------------------------------------------------
@app.get("/predictive/status")
def predictive_status():
    return predictive_engine.status()


@app.get("/predictive/forecast")
def predictive_forecast():
    return predictive_engine.forecast()


# -----------------------------------------------------
# Executive Dashboard (NEW)
# -----------------------------------------------------
@app.get("/executive/snapshot")
def executive_snapshot():
    return dashboard_api.generate_snapshot()


@app.get("/executive/status")
def executive_status():
    return dashboard_api.status()