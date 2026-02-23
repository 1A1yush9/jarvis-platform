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

app = FastAPI(title="Jarvis Platform")

SYSTEM_STATUS = "Jarvis LIVE — Distributed Learning Consensus Active"

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
        "stage": "8.1",
        "timestamp": time.time()
    }


# -----------------------------------
@app.post("/predictive/signal")
def receive_signal(signal: dict, x_api_key: Optional[str] = Header(None)):

    client_id = authenticate(x_api_key)
    meter_usage(client_id)

    opportunity = opportunity_engine.generate_opportunity(client_id, signal)
    observer_event("Opportunity created")

    return {"opportunity": opportunity}


# -----------------------------------
# RECEIVE MESH SIGNAL + LEARN
# -----------------------------------
@app.post("/mesh/receive")
def receive_mesh(signal: dict):

    mesh_engine.receive_signal(signal)
    consensus_engine.ingest_mesh_signal(signal)

    observer_event("Mesh consensus updated")

    return {"status": "signal integrated"}


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
        "self_improvement": self_improvement.snapshot(),
        "market_expansion": market_expansion.snapshot(),
        "mesh": mesh_engine.snapshot(),
        "consensus": consensus_engine.snapshot(),
        "observer_events": len(observer_log),
        "clients_metered": len(usage_meter)
    }