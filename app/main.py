from fastapi import FastAPI
from app.operational_status import router as operational_router

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="34.0",
)

# Register Routes
app.include_router(operational_router)

@app.get("/")
def root():
    return {
        "system": "Jarvis Platform",
        "stage": "34.0",
        "mode": "Advisory Cognition Only",
        "status": "LIVE"
    }