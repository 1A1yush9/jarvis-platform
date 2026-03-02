from fastapi import FastAPI
from app.operational_status import router as operational_router
from app.shadow_status import router as shadow_router

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="35.0",
)

# Register Routes
app.include_router(operational_router)
app.include_router(shadow_router)

@app.get("/")
def root():
    return {
        "system": "Jarvis Platform",
        "stage": "35.0",
        "mode": "Advisory Cognition Only",
        "status": "LIVE"
    }