from fastapi import FastAPI
from typing import Dict, Any

from core.executive_alignment_engine import ExecutiveAlignmentEngine
from core.strategic_memory import StrategicMemory
from core.executive_intent_model import ExecutiveIntentModel

app = FastAPI(title="Jarvis Executive Intelligence API")

alignment_engine = ExecutiveAlignmentEngine()
strategic_memory = StrategicMemory()
intent_model = ExecutiveIntentModel()


@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE",
        "stage": "25.0",
        "mode": "Advisory Cognition Only",
    }


# ---------------------------------------------------
# Alignment + Memory + Intent Modeling
# ---------------------------------------------------
@app.post("/executive/alignment")
def executive_alignment(payload: Dict[str, Any]):

    strategic_context = payload.get("strategic_context", {})
    simulation_output = payload.get("simulation_output", {})
    narrative_output = payload.get("narrative_output", {})

    alignment_result = alignment_engine.evaluate_alignment(
        strategic_context,
        simulation_output,
        narrative_output,
    )

    memory_result = strategic_memory.store_snapshot(alignment_result)

    intent_result = intent_model.model_intent()

    return {
        "stage": "25.0",
        "alignment_analysis": alignment_result,
        "strategic_memory": memory_result,
        "executive_intent": intent_result,
    }