from fastapi import FastAPI

from app.growth.growth_scheduler import start_growth_engine
from app.strategy.strategy_router import router as strategy_router
from app.strategy.strategy_engine import (
    update_strategic_memory,
    generate_strategy_insights
)
from app.prediction.prediction_router import router as prediction_router
from app.prediction.prediction_engine import generate_predictions

app = FastAPI(title="Jarvis Platform")


def get_usage_metrics():
    return [
        {"client_id": "client_a", "requests": 1500, "revenue": 700},
        {"client_id": "client_b", "requests": 200, "revenue": 50},
    ]


@app.on_event("startup")
async def startup_event():
    print("Starting Autonomous Growth Engine...")
    start_growth_engine(get_usage_metrics)

    # Strategic layer
    update_strategic_memory([])
    generate_strategy_insights()

    # Predictive layer
    generate_predictions()


app.include_router(strategy_router)
app.include_router(prediction_router)


@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE — Predictive Market Awareness Active"
    }