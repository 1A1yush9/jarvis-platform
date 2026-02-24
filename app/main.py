from fastapi import FastAPI
from datetime import datetime

from core.unified_kernel import unified_kernel
from core.signal_fusion import signal_fusion
from core.context_reasoner import context_reasoner
from core.predictive_engine import predictive_engine

app = FastAPI(title="Jarvis Cognitive Core")

# ---------------------------------------------------
# ROOT
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "system": "Jarvis Platform",
        "status": "LIVE",
        "stage": "14.3 - Predictive Reasoning Engine",
        "timestamp": datetime.utcnow().isoformat()
    }


# ---------------------------------------------------
# STATUS ENDPOINTS
# ---------------------------------------------------

@app.get("/fusion/status")
def fusion_status():
    return signal_fusion.status()


@app.get("/context/status")
def context_status():
    return context_reasoner.status()


@app.get("/prediction/status")
def prediction_status():
    return predictive_engine.status()


@app.get("/kernel/status")
def kernel_status():
    return unified_kernel.status()


# ---------------------------------------------------
# FULL COGNITIVE PIPELINE
# ---------------------------------------------------

@app.post("/kernel/evaluate")
def kernel_evaluate():

    # 1️⃣ Signals
    signals = signal_fusion.collect_signals()

    # 2️⃣ Context reasoning
    context = context_reasoner.analyze(signals)

    # 3️⃣ Prediction
    prediction = predictive_engine.forecast(signals, context)

    # 4️⃣ Kernel evaluation
    unified_kernel.update_state(
        clients_active=signals["clients_active"],
        execution_load=signals["execution_load"],
        revenue_velocity=signals["revenue_velocity"],
        market_opportunity_score=signals["market_opportunity_score"],
    )

    decision = unified_kernel.evaluate()

    return {
        "signals": signals,
        "context": context,
        "prediction": prediction,
        "decision": decision
    }