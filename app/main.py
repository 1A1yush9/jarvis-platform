from fastapi import FastAPI
from datetime import datetime

from core.unified_kernel import unified_kernel
from core.signal_fusion import signal_fusion
from core.context_reasoner import context_reasoner

app = FastAPI(title="Jarvis Cognitive Core")

# ---------------------------------------------------
# ROOT
# ---------------------------------------------------

@app.get("/")
def root():
    return {
        "system": "Jarvis Platform",
        "status": "LIVE",
        "stage": "14.2 - Contextual Reasoning Layer",
        "timestamp": datetime.utcnow().isoformat()
    }


# ---------------------------------------------------
# SIGNAL STATUS
# ---------------------------------------------------

@app.get("/fusion/status")
def fusion_status():
    return signal_fusion.status()


# ---------------------------------------------------
# CONTEXT STATUS
# ---------------------------------------------------

@app.get("/context/status")
def context_status():
    return context_reasoner.status()


# ---------------------------------------------------
# KERNEL STATUS
# ---------------------------------------------------

@app.get("/kernel/status")
def kernel_status():
    return unified_kernel.status()


# ---------------------------------------------------
# FULL COGNITIVE EVALUATION
# ---------------------------------------------------

@app.post("/kernel/evaluate")
def kernel_evaluate():

    # 1️⃣ Collect fused signals
    signals = signal_fusion.collect_signals()

    # 2️⃣ Generate contextual reasoning
    context = context_reasoner.analyze(signals)

    # 3️⃣ Feed kernel
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
        "decision": decision
    }