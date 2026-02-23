# app/main.py

from fastapi import FastAPI, Header, HTTPException
from typing import Optional
import time

from app.opportunity_engine import OpportunityEngine
from app.execution_engine import ExecutionEngine
from app.revenue_engine import RevenueOptimizationEngine
from app.cognitive_os import CognitiveBusinessOS
from app.growth_orchestrator import AutonomousGrowthOrchestrator
from app.self_improvement_engine import SelfImprovementEngine
from app.market_expansion_engine import MarketExpansionEngine
from app.mesh_engine import IntelligenceMeshEngine
from app.consensus_engine import DistributedConsensusEngine
from app.strategy_planner import AutonomousStrategyPlanner

app = FastAPI(title="Jarvis Platform")

SYSTEM_STATUS = "Jarvis LIVE — Autonomous Strategic Planning Active"

API_KEYS = {
    "admin-key": "admin",
    "client-demo-key": "client_001"
}

usage_meter = {}
observer_log = []

opportunity_engine = OpportunityEngine()
execution_engine = ExecutionEngine()
revenue_engine = RevenueOptimizationEngine()
cognitive_os = CognitiveBusinessOS()
growth_orchestrator = AutonomousGrowthOrchestrator()
self_improvement = SelfImprovementEngine()
market_expansion = MarketExpansionEngine()
mesh_engine = IntelligenceMeshEngine()
consensus_engine = DistributedConsensusEngine()
strategy_planner = AutonomousStrategyPlanner()


# -----------------------------------
def authenticate(api_key: Optional[str]):
    if not api_key or api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return API_KEYS[api_key]


def observer_event(event: str):
    observer_log.append({"event": event, "time": time.time()})


def meter_usage(client_id: str):
    usage_meter[client_id] = usage_meter.get(client_id, 0) + 1


# -----------------------------------
@app.get("/")
def root():
    return {
        "status": SYSTEM_STATUS,
        "stage": "8.2",
        "timestamp": time.time()
    }


# -----------------------------------
@app.post("/mesh/receive")
def receive_mesh(signal: dict):

    mesh_engine.receive_signal(signal)
    consensus_engine.ingest_mesh_signal(signal)

    observer_event("Mesh consensus updated")
    return {"status": "signal integrated"}


# -----------------------------------
# STRATEGIC PLAN GENERATION
# -----------------------------------
@app.post("/admin/generate-strategy-plan")
def generate_plan(x_api_key: Optional[str] = Header(None)):

    role = authenticate(x_api_key)
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    plan = strategy_planner.generate_plan(
        cognitive_os.system_focus
    )

    observer_event("Strategic plan generated")

    return plan


# -----------------------------------
@app.post("/admin/run-cognitive-cycle")
def run_cycle(x_api_key: Optional[str] = Header(None)):

    role = authenticate(x_api_key)
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    local_bias = self_improvement.bias_map()
    global_bias = consensus_engine.consensus_bias()

    result = cognitive_os.run_cycle(
        opportunity_engine.system_snapshot(),
        execution_engine.system_snapshot(),
        revenue_engine.system_snapshot(),
        local_bias,
        global_bias
    )

    self_improvement.record_cycle_result(
        result["focus"],
        revenue_engine.system_snapshot()
    )

    observer_event("Consensus cognitive cycle executed")
    return result


# -----------------------------------
@app.get("/admin/system")
def admin_snapshot(x_api_key: Optional[str] = Header(None)):

    role = authenticate(x_api_key)
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    return {
        "cognitive_os": cognitive_os.snapshot(),
        "strategy_planner": strategy_planner.snapshot(),
        "consensus": consensus_engine.snapshot(),
        "mesh": mesh_engine.snapshot(),
        "observer_events": len(observer_log),
        "clients_metered": len(usage_meter)
    }