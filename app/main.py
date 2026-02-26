from fastapi import FastAPI
from typing import Dict, Any

# Existing systems assumed present
from core.executive_alignment_engine import ExecutiveAlignmentEngine

app = FastAPI(title="Jarvis Executive Intelligence API")

alignment_engine = ExecutiveAlignmentEngine()


@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE",
        "stage": "24.0",
        "mode": "Advisory Cognition Only",
    }


# ---------------------------------------------------
# Stage-24 Alignment Evaluation Endpoint
# ---------------------------------------------------
@app.post("/executive/alignment")
def executive_alignment(payload: Dict[str, Any]):

    strategic_context = payload.get("strategic_context", {})
    simulation_output = payload.get("simulation_output", {})
    narrative_output = payload.get("narrative_output", {})

    result = alignment_engine.evaluate_alignment(
        strategic_context,
        simulation_output,
        narrative_output,
    )

    return {
        "stage": "24.0",
        "alignment_analysis": result,
    }