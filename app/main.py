from fastapi import FastAPI
from app.growth.growth_scheduler import start_growth_engine

app = FastAPI(title="Jarvis Platform")


# ---------------------------------
# MOCK USAGE SOURCE (connect later
# to real metering database)
# ---------------------------------
def get_usage_metrics():
    return [
        {
            "client_id": "client_a",
            "requests": 1500,
            "revenue": 700
        },
        {
            "client_id": "client_b",
            "requests": 200,
            "revenue": 50
        }
    ]


@app.on_event("startup")
async def startup_event():
    print("Starting Autonomous Growth Engine...")
    start_growth_engine(get_usage_metrics)


@app.get("/")
def root():
    return {"status": "Jarvis LIVE — Growth Engine Active"}