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


app = FastAPI(
    title="Jarvis Cognitive Business OS",
    version="10.2",
    description="Jarvis LIVE — Meta Learning Active"
)

startup_time = datetime.utcnow().isoformat()

# ---------------------------------------------------
# SYSTEM INITIALIZATION (ORDER MATTERS)
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

print("Stage 10.2 Meta Learning ACTIVE")


# ---------------------------------------------------
# ROOT
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE — Meta Learning Active",
        "stage": "10.2",
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
    return executive_core.get_status()


@app.get("/strategy/status")
def strategy_status():
    return strategy_rewrite.get_status()


@app.get("/revenue-ops/status")
def revenue_ops_status():
    return revenue_operations.get_status()


@app.get("/meta/status")
def meta_status():
    return meta_learning.get_status()