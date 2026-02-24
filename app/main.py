from fastapi import FastAPI
from datetime import datetime

from core.unified_kernel import unified_kernel
from core.signal_fusion import signal_fusion

app = FastAPI(title="Jarvis Cognitive Core")

# ---------------------------------------------------
# ROOT
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "system": "Jarvis Platform",
        "status": "LIVE",
        "stage": "14.1 - Cognitive Signal Fusion",
        "timestamp": datetime.utcnow().isoformat()
    }


# ---------------------------------------------------
# SIGNAL SNAPSHOT
# ---------------------------------------------------

@app.get("/fusion/status")
def fusion_status():
    return signal_fusion.status()


# ---------------------------------------------------
# KERNEL STATUS
# ---------------------------------------------------

@app.get("/kernel/status")
def kernel_status():
    return unified_kernel.status()


# ---------------------------------------------------
# FUSED EVALUATION
# ---------------------------------------------------

@app.post("/kernel/evaluate")
def kernel_evaluate():

    # Collect real-time signals
    signals = signal_fusion.collect_signals()

    # Feed kernel
    unified_kernel.update_state(
        clients_active=signals["clients_active"],
        execution_load=signals["execution_load"],
        revenue_velocity=signals["revenue_velocity"],
        market_opportunity_score=signals["market_opportunity_score"],
    )

    decision = unified_kernel.evaluate()

    return {
        "signals": signals,
        "decision": decision
    }