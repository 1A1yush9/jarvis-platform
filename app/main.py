# app/main.py

"""
Jarvis Platform — Production Safe API Entry

IMPORTANT:
- This file ONLY orchestrates modules
- No intelligence logic written here
- Safe boot guaranteed (prevents Render crash)
"""

from fastapi import FastAPI
from typing import Dict, Any

# --------------------------------------------------
# CORE IMPORTS (MATCH YOUR REAL FILE STRUCTURE)
# --------------------------------------------------

from core.context_reasoner import ContextReasoner
from core.predictive_engine import PredictiveEngine
from core.priority_intelligence import PriorityIntelligence
from core.executive_layer import ExecutiveLayer

from core.meta_cognitive_awareness import MetaCognitiveAwareness
from core.memory import Memory
from core.adaptive_reasoning import AdaptiveReasoningCalibration
from core.strategic_orchestrator import StrategicOrchestrator
from core.execution_interface import ExecutionInterface


# --------------------------------------------------
# FASTAPI INIT
# --------------------------------------------------

app = FastAPI(
    title="Jarvis Strategic Intelligence API",
    version="15.1",
    description="Advisory Intelligence System (Execution Disabled)"
)

# --------------------------------------------------
# LOAD SYSTEM MODULES (BOOT ONCE)
# --------------------------------------------------

context_layer = ContextReasoner()
predictor = PredictiveEngine()
priority_engine = PriorityIntelligence()
executive_layer = ExecutiveLayer()

meta_awareness = MetaCognitiveAwareness()
memory = Memory()
adaptive = AdaptiveReasoningCalibration()
orchestrator = StrategicOrchestrator()
execution_interface = ExecutionInterface()


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/")
def health():
    return {
        "status": "Jarvis LIVE",
        "mode": "advisory",
        "api": "running"
    }


# --------------------------------------------------
# MAIN INTELLIGENCE ENDPOINT
# --------------------------------------------------

@app.post("/analyze")
def analyze(payload: Dict[str, Any]):

    # 1️⃣ Signals
    signals = payload.get("signals", {})

    # 2️⃣ Context Understanding
    context = context_layer.process(signals)

    # 3️⃣ Prediction
    prediction = predictor.analyze(context)

    # 4️⃣ Priority Evaluation
    priority = priority_engine.evaluate(prediction)

    # 5️⃣ Executive Framing
    executive = executive_layer.frame(priority)

    # 6️⃣ Meta Cognitive Awareness
    awareness = meta_awareness.generate_awareness(
        signals,
        context,
        prediction,
        priority
    )

    # 7️⃣ Memory Storage
    memory.store(signals, awareness)
    memory_summary = memory.summary()

    # 8️⃣ Adaptive Calibration
    calibration = adaptive.calibrate(memory_summary)

    # 9️⃣ Strategic Orchestration
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

    # 🔟 Safe API Output
    response = execution_interface.build_response(orchestrated)

    return response