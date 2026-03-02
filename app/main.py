from fastapi import FastAPI

from app.operational_status import router as operational_router
from app.shadow_status import router as shadow_router
from app.adaptive_status import router as adaptive_router
from app.containment_status import router as containment_router
from app.activation_status import router as activation_router
from app.oversight_api import router as oversight_router
from app.constitution_api import router as constitution_router
from app.decision_trace_api import router as decision_trace_router
from app.simulation_api import router as simulation_router
from app.forecast_api import router as forecast_router


app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="43.0",
)


app.include_router(operational_router)
app.include_router(shadow_router)
app.include_router(adaptive_router)
app.include_router(containment_router)
app.include_router(activation_router)
app.include_router(oversight_router)
app.include_router(constitution_router)
app.include_router(decision_trace_router)
app.include_router(simulation_router)
app.include_router(forecast_router)


@app.get("/")
def root():
    return {
        "system": "Jarvis Platform",
        "stage": "43.0",
        "mode": "Advisory Cognition Only",
        "status": "LIVE",
        "forecasting": "Multi-Timeline Engine Active"
    }