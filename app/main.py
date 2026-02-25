# app/main.py

"""
Jarvis Platform — ULTRA SAFE API ENTRY
Module-based loading (no class assumptions)
Guaranteed boot stability on Render.
"""

from fastapi import FastAPI
from typing import Dict, Any

# --------------------------------------------------
# IMPORT MODULES (NOT CLASSES)
# --------------------------------------------------

import core.context_reasoner as context_module
import core.predictive_engine as predictive_module
import core.priority_intelligence as priority_module
import core.executive_layer as executive_module

import core.meta_cognitive_awareness as meta_module
import core.memory as memory_module
import core.adaptive_reasoning as adaptive_module
import core.strategic_orchestrator as orchestrator_module
import core.execution_interface as interface_module


# --------------------------------------------------
# FASTAPI INIT
# --------------------------------------------------

app = FastAPI(
    title="Jarvis Strategic Intelligence API",
    version="15.1",
    description="Advisory Intelligence System"
)

# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/")
def health():
    return {
        "status": "Jarvis LIVE",
        "mode": "advisory"
    }


# --------------------------------------------------
# SAFE FUNCTION CALLER
# --------------------------------------------------

def safe_call(module, func_name, default, *args):
    if hasattr(module, func_name):
        return getattr(module, func_name)(*args)
    return default


# --------------------------------------------------
# INTELLIGENCE ENDPOINT
# --------------------------------------------------

@app.post("/analyze")
def analyze(payload: Dict[str, Any]):

    signals = payload.get("signals", {})

    # Context
    context = safe_call(
        context_module,
        "process",
        {},
        signals
    )

    # Prediction
    prediction = safe_call(
        predictive_module,
        "analyze",
        {},
        context
    )

    # Priority
    priority = safe_call(
        priority_module,
        "evaluate",
        {},
        prediction
    )

    # Executive
    executive = safe_call(
        executive_module,
        "frame",
        {},
        priority
    )

    # Meta Awareness
    awareness = safe_call(
        meta_module,
        "generate_awareness",
        {},
        signals, context, prediction, priority
    )

    # Memory
    safe_call(memory_module, "store", None, signals, awareness)
    memory_summary = safe_call(memory_module, "summary", {},)

    # Adaptive Calibration
    calibration = safe_call(
        adaptive_module,
        "calibrate",
        {},
        memory_summary
    )

    # Orchestration
    orchestrated = safe_call(
        orchestrator_module,
        "orchestrate",
        {},
        signals,
        context,
        prediction,
        priority,
        executive,
        awareness,
        memory_summary,
        calibration
    )

    # Interface Output
    response = safe_call(
        interface_module,
        "build_response",
        {},
        orchestrated
    )

    return response