"""
Jarvis Platform API
Production Safe — Stage 20.5 Integrated
"""

from fastapi import FastAPI
from typing import Dict, Any, List
import asyncio

from core.strategic_alignment_engine import StrategicAlignmentEngine
from core.adaptive_strategy_memory import AdaptiveStrategyMemory
from core.predictive_stability_engine import PredictiveStabilityEngine
from core.executive_dashboard_api import ExecutiveDashboardAPI
from core.client_intelligence_router import ClientIntelligenceRouter
from core.autonomous_insight_engine import AutonomousInsightEngine
from core.continuous_intelligence_cycle import ContinuousIntelligenceCycle

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="20.5",
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

continuous_cycle = ContinuousIntelligenceCycle(
    insight_engine,
    predictive_engine,
)

# -----------------------------------------------------
# Startup Event (SAFE BACKGROUND LOOP)
# -----------------------------------------------------
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(continuous_cycle.start_cycle())

# -----------------------------------------------------
# Root
# -----------------------------------------------------
@app.get("/")
def root():
    return {
        "platform": "Jarvis",
        "status": "LIVE",
        "mode": "advisory_only",
        "stage": "20.5",
    }

# -----------------------------------------------------
# Alignment
# -----------------------------------------------------
@app.post("/alignment/evaluate")
def evaluate_alignment(payload: Dict[str, Any]):

    decisions: List[Dict[str, Any]] = payload.get("decisions", [])
    objectives = payload.get(
        "objectives",
        {"revenue_focus": True, "safety_priority": True},
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

# -----------------------------------------------------
# Predictive
# -----------------------------------------------------
@app.get("/predictive/forecast")
def predictive_forecast():
    return predictive_engine.forecast()

# -----------------------------------------------------
# Executive Snapshot
# -----------------------------------------------------
@app.get("/executive/snapshot")
def executive_snapshot():
    return dashboard_api.generate_snapshot()

# -----------------------------------------------------
# Client Snapshot
# -----------------------------------------------------
@app.get("/client/{client_id}/snapshot")
def client_snapshot(client_id: str):
    return client_router.client_snapshot(client_id)

# -----------------------------------------------------
# Insights
# -----------------------------------------------------
@app.get("/insights/generate")
def generate_insights():
    return insight_engine.generate_insights()

# -----------------------------------------------------
# Continuous Intelligence (NEW)
# -----------------------------------------------------
@app.get("/cycle/status")
def cycle_status():
    return continuous_cycle.status()

@app.get("/cycle/state")
def cycle_state():
    return continuous_cycle.get_state()