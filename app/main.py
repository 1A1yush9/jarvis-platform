from fastapi import FastAPI

from app.operational_status import router as operational_router
from app.shadow_status import router as shadow_router
from app.adaptive_status import router as adaptive_router
from app.containment_status import router as containment_router
from app.activation_status import router as activation_router
from app.oversight_api import router as oversight_router
from app.constitution_api import router as constitution_router


# ---------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="40.0",
)


# ---------------------------------------------------------
# Router Registration
# ---------------------------------------------------------

app.include_router(operational_router)
app.include_router(shadow_router)
app.include_router(adaptive_router)
app.include_router(containment_router)
app.include_router(activation_router)
app.include_router(oversight_router)
app.include_router(constitution_router)


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "system": "Jarvis Platform",
        "stage": "40.0",
        "mode": "Advisory Cognition Only",
        "status": "LIVE",
        "governance": "Constitutional Layer Active"
    }