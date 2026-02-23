# app/main.py

from fastapi import FastAPI
from datetime import datetime

# Controllers
try:
    from app.core.enterprise_controller import AutonomousEnterpriseController
except Exception:
    AutonomousEnterpriseController = None

try:
    from app.core.revenue_command import RevenueCommandSystem
except Exception:
    RevenueCommandSystem = None

try:
    from app.core.client_acquisition import ClientAcquisitionEngine
except Exception:
    ClientAcquisitionEngine = None


app = FastAPI(
    title="Jarvis Cognitive Business OS",
    version="9.2",
    description="Jarvis LIVE — Client Acquisition Active"
)

startup_time = datetime.utcnow().isoformat()

enterprise_controller = None
revenue_command = None
client_acquisition = None


# ---------------------------------------------------
# SYSTEM INITIALIZATION
# ---------------------------------------------------

if AutonomousEnterpriseController:
    enterprise_controller = AutonomousEnterpriseController()
    print("Stage 9.0 Controller ACTIVE")

if RevenueCommandSystem:
    revenue_command = RevenueCommandSystem(enterprise_controller)
    print("Stage 9.1 Revenue Command ACTIVE")

if ClientAcquisitionEngine:
    client_acquisition = ClientAcquisitionEngine(
        enterprise_controller,
        revenue_command
    )
    print("Stage 9.2 Client Acquisition ACTIVE")


# ---------------------------------------------------
# ROOT
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE — Client Acquisition Active",
        "stage": "9.2",
        "startup_time": startup_time
    }


# ---------------------------------------------------
# HEALTH
# ---------------------------------------------------

@app.get("/health")
def health():
    return {
        "system": "operational",
        "timestamp": datetime.utcnow().isoformat()
    }


# ---------------------------------------------------
# ENTERPRISE STATUS
# ---------------------------------------------------

@app.get("/enterprise/status")
def enterprise_status():
    if enterprise_controller:
        return enterprise_controller.get_status()
    return {"controller": "inactive"}


# ---------------------------------------------------
# REVENUE STATUS
# ---------------------------------------------------

@app.get("/revenue/status")
def revenue_status():
    if revenue_command:
        return revenue_command.get_status()
    return {"revenue_command": "inactive"}


# ---------------------------------------------------
# CLIENT ACQUISITION STATUS
# ---------------------------------------------------

@app.get("/acquisition/status")
def acquisition_status():
    if client_acquisition:
        return client_acquisition.get_status()
    return {"acquisition": "inactive"}


# ---------------------------------------------------
# RISK CONTROL
# ---------------------------------------------------

@app.post("/enterprise/risk/{level}")
def update_risk(level: str):
    if enterprise_controller:
        enterprise_controller.update_risk_level(level)
        return {"message": f"Risk level set to {level}"}

    return {"error": "Controller unavailable"}