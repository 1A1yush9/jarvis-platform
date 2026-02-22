from fastapi import FastAPI

# Growth Engine
from app.growth.growth_scheduler import start_growth_engine

# Strategy Layer
from app.strategy.strategy_router import router as strategy_router
from app.strategy.strategy_engine import (
    update_strategic_memory,
    generate_strategy_insights,
)

# Prediction Layer
from app.prediction.prediction_router import router as prediction_router
from app.prediction.prediction_engine import generate_predictions


app = FastAPI(title="Jarvis Platform")


# --------------------------------------------------
# MOCK USAGE SOURCE
# (Later connect to real metering database)
# --------------------------------------------------
def get_usage_metrics():
    return [
        {
            "client_id": "client_a",
            "requests": 1500,
            "revenue": 700,
        },
        {
            "client_id": "client_b",
            "requests": 200,
            "revenue": 50,
        },
    ]


# --------------------------------------------------
# STARTUP EVENT
# --------------------------------------------------
@app.on_event("startup")
async def startup_event():
    print("Starting Autonomous Growth Engine...")

    # Stage 6.0 — Growth Engine
    start_growth_engine(get_usage_metrics)

    # Stage 6.1 — Strategic Intelligence
    update_strategic_memory([])
    generate_strategy_insights()

    # Stage 6.2 — Predictive Intelligence
    generate_predictions()


# --------------------------------------------------
# ADMIN ROUTERS
# --------------------------------------------------
app.include_router(strategy_router)
app.include_router(prediction_router)


# --------------------------------------------------
# ROOT HEALTH ENDPOINT
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE — Predictive Market Awareness Active"
    }