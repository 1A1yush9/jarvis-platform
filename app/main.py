from fastapi import FastAPI
from datetime import datetime

# Existing Jarvis systems (keep your imports here if present)

# Stage-14.0
from core.unified_kernel import unified_kernel

app = FastAPI(title="Jarvis Cognitive Core")

# ---------------------------------------------------
# ROOT HEALTH CHECK
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "system": "Jarvis Platform",
        "status": "LIVE",
        "stage": "14.0 - Unified Intelligence Kernel",
        "timestamp": datetime.utcnow().isoformat()
    }


# ---------------------------------------------------
# KERNEL STATUS
# ---------------------------------------------------

@app.get("/kernel/status")
def kernel_status():
    return unified_kernel.status()


# ---------------------------------------------------
# KERNEL EVALUATION (SAFE TEST ENDPOINT)
# ---------------------------------------------------

@app.post("/kernel/evaluate")
def kernel_evaluate():
    """
    Runs advisory evaluation.
    Does NOT affect execution systems.
    """

    # Example ingestion (temporary safe defaults)
    unified_kernel.update_state(
        clients_active=5,
        execution_load=0.45,
        revenue_velocity=0.6,
        market_opportunity_score=0.5
    )

    decision = unified_kernel.evaluate()
    return decision