"""
Jarvis Platform API
Production Safe — Stage 23.0 Integrated
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
from core.executive_signal_prioritizer import ExecutiveSignalPrioritizer
from core.strategic_narrative_engine import StrategicNarrativeEngine
from core.intelligence_confidence_engine import IntelligenceConfidenceEngine
from core.executive_risk_radar import ExecutiveRiskRadar
from core.strategic_drift_explainer import StrategicDriftExplainer

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="23.0",
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

signal_prioritizer = ExecutiveSignalPrioritizer(
    continuous_cycle
)

narrative_engine = StrategicNarrativeEngine(signal_prioritizer)

confidence_engine = IntelligenceConfidenceEngine(
    adaptive_memory,
    predictive_engine,
    continuous_cycle,
)

risk_radar = ExecutiveRiskRadar(
    predictive_engine,
    confidence_engine,
    signal_prioritizer,
)

drift_explainer = StrategicDriftExplainer(
    adaptive_memory,
    predictive_engine,
    confidence_engine,
    risk_radar,
)

# -----------------------------------------------------
# Startup
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
        "stage": "23.0",
    }

# -----------------------------------------------------
# Core APIs
# -----------------------------------------------------
@app.post("/alignment/evaluate")
def evaluate_alignment(payload: Dict[str, Any]):
    decisions: List[Dict[str, Any]] = payload.get("decisions", [])
    objectives = payload.get(
        "objectives",
        {"revenue_focus": True, "safety_priority": True},
    )
    return alignment_engine.evaluate_alignment(decisions, objectives)

@app.post("/memory/record")
def record_alignment(payload: Dict[str, Any]):
    return adaptive_memory.record_alignment_event(payload)

@app.get("/predictive/forecast")
def predictive_forecast():
    return predictive_engine.forecast()

@app.get("/executive/snapshot")
def executive_snapshot():
    return dashboard_api.generate_snapshot()

@app.get("/client/{client_id}/snapshot")
def client_snapshot(client_id: str):
    return client_router.client_snapshot(client_id)

@app.get("/insights/generate")
def generate_insights():
    return insight_engine.generate_insights()

@app.get("/cycle/state")
def cycle_state():
    return continuous_cycle.get_state()

@app.get("/signals/prioritized")
def prioritized_signals():
    return signal_prioritizer.prioritize()

@app.get("/narrative/briefing")
def narrative_briefing():
    return narrative_engine.generate_narrative()

@app.get("/confidence/evaluate")
def confidence_evaluate():
    return confidence_engine.evaluate_confidence()

@app.get("/risk/evaluate")
def risk_evaluate():
    return risk_radar.evaluate_risk()

# -----------------------------------------------------
# DRIFT EXPLANATION (NEW)
# -----------------------------------------------------
@app.get("/drift/explain")
def drift_explain():
    return drift_explainer.explain()

@app.get("/drift/status")
def drift_status():
    return drift_explainer.status()