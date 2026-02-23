# app/main.py

from fastapi import FastAPI
from datetime import datetime

# Core systems
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

try:
    from app.core.revenue_operations import RevenueOperationsBrain
except Exception:
    RevenueOperationsBrain = None

try:
    from app.core.executive_core import ExecutiveDecisionCore
except Exception:
    ExecutiveDecisionCore = None


app = FastAPI(
    title="Jarvis Cognitive Business OS",
    version="10.0",
    description="Jarvis LIVE — Executive Decision Core Active"
)

startup_time = datetime.utcnow().isoformat()

enterprise_controller = None
revenue_command = None
client_acquisition = None
deal_intelligence = None
proposal_engine = None
revenue_operations = None
executive_core = None


# ---------------------------------------------------
# SYSTEM INITIALIZATION
# ---------------------------------------------------

if AutonomousEnterpriseController:
    enterprise_controller = AutonomousEnterpriseController()

if RevenueCommandSystem:
    revenue_command = RevenueCommandSystem(enterprise_controller)

if ClientAcquisitionEngine:
    client_acquisition = ClientAcquisitionEngine(
        enterprise_controller,
        revenue_command
    )

if DealIntelligenceEngine:
    deal_intelligence = DealIntelligenceEngine(
        client_acquisition,
        revenue_command
    )

if ProposalGenerationEngine:
    proposal_engine = ProposalGenerationEngine(deal_intelligence)

if RevenueOperationsBrain:
    revenue_operations = RevenueOperationsBrain(proposal_engine)

if ExecutiveDecisionCore:
    executive_core = ExecutiveDecisionCore(
        enterprise_controller,
        revenue_operations,
        revenue_command
    )


# ---------------------------------------------------
# ROOT
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE — Executive Decision Core Active",
        "stage": "10.0",
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

@app.get("/executive/status")
def executive_status():
    if executive_core:
        return executive_core.get_status()
    return {"executive_core": "inactive"}


@app.get("/revenue-ops/status")
def revenue_ops_status():
    if revenue_operations:
        return revenue_operations.get_status()
    return {"revenue_operations": "inactive"}