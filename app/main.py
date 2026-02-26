"""
Jarvis Platform API
Production Safe — Stage 20.0 Integrated
"""

from fastapi import FastAPI
from typing import Dict, Any, List

from core.strategic_alignment_engine import StrategicAlignmentEngine
from core.adaptive_strategy_memory import AdaptiveStrategyMemory
from core.predictive_stability_engine import PredictiveStabilityEngine
from core.executive_dashboard_api import ExecutiveDashboardAPI
from core.client_intelligence_router import ClientIntelligenceRouter
from core.autonomous_insight_engine import AutonomousInsightEngine

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="20.0",
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

client_router = ClientIntelligenceRouter(dashboard_api)

insight_engine = AutonomousInsightEngine(
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
        "stage": "20.0",
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

    return alignment_engine.evaluate_alignment(decisions, objectives)

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
# Executive Dashboard
# -----------------------------------------------------
@app.get("/executive/snapshot")
def executive_snapshot():
    return dashboard_api.generate_snapshot()


# -----------------------------------------------------
# Client Intelligence
# -----------------------------------------------------
@app.get("/client/{client_id}/snapshot")
def client_snapshot(client_id: str):
    return client_router.client_snapshot(client_id)

# -----------------------------------------------------
# Autonomous Insights (NEW)
# -----------------------------------------------------
@app.get("/insights/generate")
def generate_insights():
    return insight_engine.generate_insights()


@app.get("/insights/status")
def insight_status():
    return insight_engine.status()