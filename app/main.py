# app/main.py

from fastapi import FastAPI
from datetime import datetime

# Core Systems
from app.core.enterprise_controller import AutonomousEnterpriseController
from app.core.revenue_command import RevenueCommandSystem
from app.core.client_acquisition import ClientAcquisitionEngine
from app.core.deal_intelligence import DealIntelligenceEngine
from app.core.proposal_engine import ProposalGenerationEngine
from app.core.revenue_operations import RevenueOperationsBrain
from app.core.executive_core import ExecutiveDecisionCore
from app.core.strategy_rewrite import StrategyRewriteEngine
from app.core.meta_learning import MetaLearningEngine
from app.core.execution_interface import ExecutionInterface


app = FastAPI(
    title="Jarvis Cognitive Business OS",
    version="11.0",
    description="Jarvis LIVE — Execution Interface Active"
)

startup_time = datetime.utcnow().isoformat()

# ---------------------------------------------------
# SYSTEM INITIALIZATION
# ---------------------------------------------------

enterprise_controller = AutonomousEnterpriseController()

revenue_command = RevenueCommandSystem(enterprise_controller)

client_acquisition = ClientAcquisitionEngine(
    enterprise_controller,
    revenue_command
)

deal_intelligence = DealIntelligenceEngine(
    client_acquisition,
    revenue_command
)

proposal_engine = ProposalGenerationEngine(deal_intelligence)

revenue_operations = RevenueOperationsBrain(proposal_engine)

executive_core = ExecutiveDecisionCore(
    enterprise_controller,
    revenue_operations,
    revenue_command
)

strategy_rewrite = StrategyRewriteEngine(
    executive_core,
    enterprise_controller
)

meta_learning = MetaLearningEngine(
    revenue_operations,
    strategy_rewrite,
    enterprise_controller
)

execution_interface = ExecutionInterface(proposal_engine)

print("Stage 11.0 Execution Interface ACTIVE")


# ---------------------------------------------------
# ROOT
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE — Execution Interface Active",
        "stage": "11.0",
        "startup_time": startup_time
    }


@app.get("/health")
def health():
    return {
        "system": "operational",
        "timestamp": datetime.utcnow().isoformat()
    }


# ---------------------------------------------------
# STATUS ENDPOINTS
# ---------------------------------------------------

@app.get("/execution/status")
def execution_status():
    return execution_interface.get_status()


@app.get("/meta/status")
def meta_status():
    return meta_learning.get_status()


@app.get("/executive/status")
def executive_status():
    return executive_core.get_status()