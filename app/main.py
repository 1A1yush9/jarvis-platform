# app/main.py

from fastapi import FastAPI, Header, HTTPException
from typing import Optional
import time

from app.opportunity_engine import OpportunityEngine
from app.execution_engine import ExecutionEngine

app = FastAPI(title="Jarvis Platform")

SYSTEM_STATUS = "Jarvis LIVE — Autonomous Execution Layer Active"

API_KEYS = {
    "admin-key": "admin",
    "client-demo-key": "client_001"
}

usage_meter = {}
observer_log = []

opportunity_engine = OpportunityEngine()
execution_engine = ExecutionEngine()


# -----------------------------------
# AUTH
# -----------------------------------

def authenticate(api_key: Optional[str]):
    if not api_key or api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return API_KEYS[api_key]


# -----------------------------------
# ROOT
# -----------------------------------

@app.get("/")
def root():
    return {
        "status": SYSTEM_STATUS,
        "stage": "6.4",
        "timestamp": time.time()
    }


# -----------------------------------
# INTERNAL SYSTEMS
# -----------------------------------

def observer_event(event: str):
    observer_log.append({"event": event, "time": time.time()})


def meter_usage(client_id: str):
    usage_meter[client_id] = usage_meter.get(client_id, 0) + 1


# -----------------------------------
# PREDICTIVE → OPPORTUNITY
# -----------------------------------

@app.post("/predictive/signal")
def receive_signal(signal: dict, x_api_key: Optional[str] = Header(None)):

    client_id = authenticate(x_api_key)
    meter_usage(client_id)

    opportunity = opportunity_engine.generate_opportunity(client_id, signal)
    observer_event("Opportunity created")

    return {"opportunity": opportunity}


# -----------------------------------
# CREATE EXECUTION PLAN
# -----------------------------------

@app.post("/execute/from-opportunity")
def create_execution(
    payload: dict,
    x_api_key: Optional[str] = Header(None)
):

    client_id = authenticate(x_api_key)
    meter_usage(client_id)

    opportunities = opportunity_engine.get_client_opportunities(client_id)

    for opp in opportunities:
        if opp["opportunity_id"] == payload["opportunity_id"]:
            action = execution_engine.create_execution_plan(client_id, opp)
            observer_event("Execution plan proposed")
            return {"action": action}

    raise HTTPException(status_code=404, detail="Opportunity not found")


# -----------------------------------
# CLIENT ACTION FEED
# -----------------------------------

@app.get("/actions")
def get_actions(x_api_key: Optional[str] = Header(None)):

    client_id = authenticate(x_api_key)
    meter_usage(client_id)

    return {
        "client_id": client_id,
        "actions": execution_engine.get_client_actions(client_id)
    }


# -----------------------------------
# UPDATE ACTION STATUS
# -----------------------------------

@app.post("/actions/update")
def update_action(payload: dict, x_api_key: Optional[str] = Header(None)):

    client_id = authenticate(x_api_key)

    action = execution_engine.update_status(
        client_id,
        payload["action_id"],
        payload["status"]
    )

    if not action:
        raise HTTPException(status_code=404, detail="Action not found")

    observer_event("Action status updated")
    return {"updated": action}


# -----------------------------------
# ADMIN SNAPSHOT
# -----------------------------------

@app.get("/admin/system")
def admin_snapshot(x_api_key: Optional[str] = Header(None)):

    role = authenticate(x_api_key)

    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    return {
        "opportunities": opportunity_engine.system_snapshot(),
        "execution": execution_engine.system_snapshot(),
        "observer_events": len(observer_log),
        "clients_metered": len(usage_meter)
    }