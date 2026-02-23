# app/main.py

from fastapi import FastAPI, Header, HTTPException
from typing import Optional
import time

from app.opportunity_engine import OpportunityEngine

app = FastAPI(title="Jarvis Platform")

# -----------------------------------
# SYSTEM STATE
# -----------------------------------

SYSTEM_STATUS = "Jarvis LIVE — Opportunity Discovery Engine Active"

API_KEYS = {
    "admin-key": "admin",
    "client-demo-key": "client_001"
}

usage_meter = {}
observer_log = []

opportunity_engine = OpportunityEngine()


# -----------------------------------
# AUTH LAYER
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
        "stage": "6.3",
        "timestamp": time.time()
    }


# -----------------------------------
# OBSERVER SYSTEM
# -----------------------------------

def observer_event(event: str):
    observer_log.append({
        "event": event,
        "time": time.time()
    })


# -----------------------------------
# USAGE METERING
# -----------------------------------

def meter_usage(client_id: str):
    usage_meter[client_id] = usage_meter.get(client_id, 0) + 1


# -----------------------------------
# PREDICTIVE SIGNAL INPUT
# -----------------------------------

@app.post("/predictive/signal")
def receive_predictive_signal(
    signal: dict,
    x_api_key: Optional[str] = Header(None)
):

    client_id = authenticate(x_api_key)
    meter_usage(client_id)

    observer_event("Predictive signal received")

    opportunity = opportunity_engine.generate_opportunity(
        client_id,
        signal
    )

    return {
        "message": "Opportunity generated",
        "opportunity": opportunity
    }


# -----------------------------------
# CLIENT OPPORTUNITY FEED
# -----------------------------------

@app.get("/opportunities")
def get_opportunities(
    x_api_key: Optional[str] = Header(None)
):

    client_id = authenticate(x_api_key)
    meter_usage(client_id)

    return {
        "client_id": client_id,
        "opportunities": opportunity_engine.get_client_opportunities(client_id)
    }


# -----------------------------------
# ADMIN CONTROL VIEW
# -----------------------------------

@app.get("/admin/opportunity-system")
def admin_snapshot(
    x_api_key: Optional[str] = Header(None)
):

    role = authenticate(x_api_key)

    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    return {
        "system": opportunity_engine.system_snapshot(),
        "observer_events": len(observer_log),
        "usage_clients": len(usage_meter)
    }