# app/main.py

from fastapi import FastAPI
from typing import Dict, Any
import uuid

# --------------------------------------------------
# ROUTES
# --------------------------------------------------

from app.routes.proposal import router as proposal_router
from app.routes.executive import router as executive_router
from app.routes.supervisor import router as supervisor_router

# --------------------------------------------------
# CORE SYSTEM IMPORTS
# --------------------------------------------------

from core.session_manager import SessionManager
from core.persistent_memory import PersistentMemory
from core.telemetry import Telemetry
from core.control_plane import ControlPlane
from core.access_control import AccessControl
from core.client_isolation import ClientIsolation
from core.revenue_intelligence import RevenueIntelligence


# --------------------------------------------------
# APP INITIALIZATION
# --------------------------------------------------

app = FastAPI(
    title="Jarvis Strategic Intelligence API",
    version="17.4",
    description="Unified Intelligence Kernel — Advisory Mode"
)

# --------------------------------------------------
# REGISTER ROUTERS (AFTER APP CREATION)
# --------------------------------------------------

app.include_router(proposal_router, tags=["Proposal Intelligence"])
app.include_router(executive_router, tags=["Executive Decision"])
app.include_router(supervisor_router, tags=["Strategic Supervisor"])


# --------------------------------------------------
# SYSTEM MODULE INITIALIZATION
# --------------------------------------------------

session_manager = SessionManager()
persistent_memory = PersistentMemory()
telemetry = Telemetry()
control_plane = ControlPlane()
access_control = AccessControl()
client_isolation = ClientIsolation()
revenue_intelligence = RevenueIntelligence()


# --------------------------------------------------
# ROOT ENDPOINT
# --------------------------------------------------

@app.get("/")
async def root():
    return {
        "system": "Jarvis Strategic Intelligence",
        "status": "operational",
        "mode": "advisory_only",
        "stage": "17.4"
    }


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "kernel": "active",
        "proposal_engine": "enabled",
        "executive_engine": "enabled",
        "strategic_supervisor": "enabled",
        "execution_authority": "disabled"
    }