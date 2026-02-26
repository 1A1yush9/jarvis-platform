from fastapi import FastAPI
from typing import Dict, Any

from core.executive_alignment_engine import ExecutiveAlignmentEngine
from core.strategic_memory import StrategicMemory

app = FastAPI(title="Jarvis Executive Intelligence API")

alignment_engine = ExecutiveAlignmentEngine()
strategic_memory = StrategicMemory()


@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE",
        "stage": "24.5",
        "mode": "Advisory Cognition Only",
    }


# ---------------------------------------------------
# Executive Alignment + Memory Consolidation
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

    return {
        "stage": "24.5",
        "alignment_analysis": alignment_result,
        "strategic_memory": memory_result,
    }