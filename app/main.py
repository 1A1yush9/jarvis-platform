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

try:
    from app.core.deal_intelligence import DealIntelligenceEngine
except Exception:
    DealIntelligenceEngine = None

try:
    from app.core.proposal_engine import ProposalGenerationEngine
except Exception:
    ProposalGenerationEngine = None


app = FastAPI(
    title="Jarvis Cognitive Business OS",
    version="9.4",
    description="Jarvis LIVE — Proposal Engine Active"
)

startup_time = datetime.utcnow().isoformat()

enterprise_controller = None
revenue_command = None
client_acquisition = None
deal_intelligence = None
proposal_engine = None


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

if DealIntelligenceEngine:
    deal_intelligence = DealIntelligenceEngine(
        client_acquisition,
        revenue_command
    )
    print("Stage 9.3 Deal Intelligence ACTIVE")

if ProposalGenerationEngine:
    proposal_engine = ProposalGenerationEngine(deal_intelligence)
    print("Stage 9.4 Proposal Engine ACTIVE")


# ---------------------------------------------------
# ROOT
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE — Proposal Engine Active",
        "stage": "9.4",
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
# STATUS ENDPOINTS
# ---------------------------------------------------

@app.get("/enterprise/status")
def enterprise_status():
    if enterprise_controller:
        return enterprise_controller.get_status()
    return {"controller": "inactive"}


@app.get("/revenue/status")
def revenue_status():
    if revenue_command:
        return revenue_command.get_status()
    return {"revenue_command": "inactive"}


@app.get("/acquisition/status")
def acquisition_status():
    if client_acquisition:
        return client_acquisition.get_status()
    return {"acquisition": "inactive"}


@app.get("/deal/status")
def deal_status():
    if deal_intelligence:
        return deal_intelligence.get_status()
    return {"deal_intelligence": "inactive"}


@app.get("/proposal/status")
def proposal_status():
    if proposal_engine:
        return proposal_engine.get_status()
    return {"proposal_engine": "inactive"}


# ---------------------------------------------------
# RISK CONTROL
# ---------------------------------------------------

@app.post("/enterprise/risk/{level}")
def update_risk(level: str):
    if enterprise_controller:
        enterprise_controller.update_risk_level(level)
        return {"message": f"Risk level set to {level}"}

    return {"error": "Controller unavailable"}