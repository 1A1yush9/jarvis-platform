# app/main.py

from fastapi import FastAPI, Header, HTTPException
from typing import Optional
import time

from app.opportunity_engine import OpportunityEngine
from app.execution_engine import ExecutionEngine
from app.revenue_engine import RevenueOptimizationEngine
from app.cognitive_os import CognitiveBusinessOS
from app.growth_orchestrator import AutonomousGrowthOrchestrator

app = FastAPI(title="Jarvis Platform")

SYSTEM_STATUS = "Jarvis LIVE — Autonomous Growth Orchestrator Active"

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
        "stage": "7.1",
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
@app.post("/actions/report-revenue")
def report_revenue(payload: dict, x_api_key: Optional[str] = Header(None)):

    client_id = authenticate(x_api_key)

    action = execution_engine.find_action(
        client_id,
        payload["action_id"]
    )

    if not action:
        raise HTTPException(status_code=404, detail="Action not found")

    record = revenue_engine.record_outcome(
        client_id,
        action,
        payload["revenue"]
    )

    observer_event("Revenue recorded")
    return {"revenue_record": record}


# -----------------------------------
@app.post("/admin/run-cognitive-cycle")
def run_cycle(x_api_key: Optional[str] = Header(None)):

    role = authenticate(x_api_key)
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    result = cognitive_os.run_cycle(
        opportunity_engine.system_snapshot(),
        execution_engine.system_snapshot(),
        revenue_engine.system_snapshot()
    )

    observer_event("Cognitive cycle executed")
    return result


# -----------------------------------
# AUTONOMOUS GROWTH TRIGGER
# -----------------------------------
@app.post("/admin/run-growth-cycle")
def run_growth(x_api_key: Optional[str] = Header(None)):

    role = authenticate(x_api_key)
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    result = growth_orchestrator.run_growth_cycle(
        cognitive_os.system_focus,
        opportunity_engine,
        execution_engine
    )

    observer_event("Autonomous growth cycle executed")

    return result


# -----------------------------------
@app.get("/admin/system")
def admin_snapshot(x_api_key: Optional[str] = Header(None)):

    role = authenticate(x_api_key)
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    return {
        "opportunities": opportunity_engine.system_snapshot(),
        "execution": execution_engine.system_snapshot(),
        "revenue": revenue_engine.system_snapshot(),
        "cognitive_os": cognitive_os.snapshot(),
        "growth_orchestrator": growth_orchestrator.snapshot(),
        "observer_events": len(observer_log),
        "clients_metered": len(usage_meter)
    }