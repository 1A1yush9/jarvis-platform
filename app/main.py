# app/main.py

"""
Jarvis Platform — SAFE BOOT API
Auto-detects core classes to prevent import crashes.
"""

from fastapi import FastAPI
from typing import Dict, Any
import importlib


# --------------------------------------------------
# SAFE CLASS LOADER (PREVENTS RENDER CRASH)
# --------------------------------------------------

def load_class(module_name, possible_classes):
    module = importlib.import_module(module_name)

    for name in possible_classes:
        if hasattr(module, name):
            return getattr(module, name)()

    raise Exception(f"No valid class found in {module_name}")


# --------------------------------------------------
# FASTAPI INIT
# --------------------------------------------------

app = FastAPI(
    title="Jarvis Strategic Intelligence API",
    version="15.1",
    description="Advisory Intelligence System"
)

# --------------------------------------------------
# LOAD CORE MODULES SAFELY
# (AUTO MATCH CLASS NAMES)
# --------------------------------------------------

context_layer = load_class(
    "core.context_reasoner",
    ["ContextReasoner", "ContextEngine", "ContextBrain", "ContextProcessor"]
)

predictor = load_class(
    "core.predictive_engine",
    ["PredictiveEngine", "Predictor", "PredictionEngine"]
)

priority_engine = load_class(
    "core.priority_intelligence",
    ["PriorityIntelligence", "PriorityEngine"]
)

executive_layer = load_class(
    "core.executive_layer",
    ["ExecutiveLayer", "ExecutiveEngine"]
)

meta_awareness = load_class(
    "core.meta_cognitive_awareness",
    ["MetaCognitiveAwareness"]
)

memory = load_class(
    "core.memory",
    ["Memory", "MemoryEngine"]
)

adaptive = load_class(
    "core.adaptive_reasoning",
    ["AdaptiveReasoningCalibration"]
)

orchestrator = load_class(
    "core.strategic_orchestrator",
    ["StrategicOrchestrator"]
)

execution_interface = load_class(
    "core.execution_interface",
    ["ExecutionInterface"]
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
# INTELLIGENCE ENDPOINT
# --------------------------------------------------

@app.post("/analyze")
def analyze(payload: Dict[str, Any]):

    signals = payload.get("signals", {})

    context = context_layer.process(signals)
    prediction = predictor.analyze(context)
    priority = priority_engine.evaluate(prediction)
    executive = executive_layer.frame(priority)

    awareness = meta_awareness.generate_awareness(
        signals, context, prediction, priority
    )

    memory.store(signals, awareness)
    memory_summary = memory.summary()

    calibration = adaptive.calibrate(memory_summary)

    orchestrated = orchestrator.orchestrate(
        signals,
        context,
        prediction,
        priority,
        executive,
        awareness,
        memory_summary,
        calibration
    )

    response = execution_interface.build_response(orchestrated)

    return response