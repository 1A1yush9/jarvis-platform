from fastapi import FastAPI
from app.operational_status import router as operational_router
from app.shadow_status import router as shadow_router
from app.adaptive_status import router as adaptive_router

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="36.0",
)

# Routes
app.include_router(operational_router)
app.include_router(shadow_router)
app.include_router(adaptive_router)


@app.get("/")
def root():
    return {
        "system": "Jarvis Platform",
        "stage": "36.0",
        "mode": "Advisory Cognition Only",
        "status": "LIVE"
    }