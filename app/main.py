# app/main.py

from fastapi import FastAPI
from datetime import datetime

# Existing systems (keep backward compatibility)
try:
    from app.core.enterprise_controller import AutonomousEnterpriseController
except Exception:
    AutonomousEnterpriseController = None


app = FastAPI(
    title="Jarvis Cognitive Business OS",
    version="9.0",
    description="Jarvis LIVE — Autonomous Enterprise Controller Active"
)

# ---------------------------------------------------
# SYSTEM BOOT
# ---------------------------------------------------

startup_time = datetime.utcnow().isoformat()

enterprise_controller = None

if AutonomousEnterpriseController:
    enterprise_controller = AutonomousEnterpriseController()
    print("Stage 9.0 — Autonomous Enterprise Controller INITIALIZED")


# ---------------------------------------------------
# ROOT STATUS
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE — Autonomous Enterprise Controller Active",
        "stage": "9.0",
        "startup_time": startup_time
    }


# ---------------------------------------------------
# HEALTH CHECK
# ---------------------------------------------------

@app.get("/health")
def health():
    return {
        "system": "operational",
        "timestamp": datetime.utcnow().isoformat()
    }


# ---------------------------------------------------
# ENTERPRISE CONTROLLER STATUS
# ---------------------------------------------------

@app.get("/enterprise/status")
def enterprise_status():
    if enterprise_controller:
        return enterprise_controller.get_status()

    return {
        "controller_active": False,
        "message": "Enterprise Controller not available"
    }


# ---------------------------------------------------
# SAFE RISK CONTROL ENDPOINT
# ---------------------------------------------------

@app.post("/enterprise/risk/{level}")
def update_risk(level: str):
    if enterprise_controller:
        enterprise_controller.update_risk_level(level)
        return {
            "message": f"Risk level updated to {level}"
        }

    return {"error": "Controller unavailable"}