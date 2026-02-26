"""
Jarvis Platform API
Production Safe — Stage 17.5 Integrated
"""

from fastapi import FastAPI
from typing import Dict, Any, List

# Existing engines (assumed already present)
from core.strategic_alignment_engine import StrategicAlignmentEngine

app = FastAPI(
    title="Jarvis Intelligence Platform",
    version="17.5",
)

# -----------------------------------------------------
# Engine Initialization
# -----------------------------------------------------

alignment_engine = StrategicAlignmentEngine()


# -----------------------------------------------------
# Root Health
# -----------------------------------------------------
@app.get("/")
def root():
    return {
        "platform": "Jarvis",
        "status": "LIVE",
        "mode": "advisory_only",
        "stage": "17.5",
    }


# -----------------------------------------------------
# Alignment Engine Status
# -----------------------------------------------------
@app.get("/alignment/status")
def alignment_status():
    return alignment_engine.status()


# -----------------------------------------------------
# Strategic Alignment Evaluation
# -----------------------------------------------------
@app.post("/alignment/evaluate")
def evaluate_alignment(payload: Dict[str, Any]):

    decisions: List[Dict[str, Any]] = payload.get("decisions", [])

    objectives = payload.get(
        "objectives",
        {
            "revenue_focus": True,
            "safety_priority": True,
        },
    )

    result = alignment_engine.evaluate_alignment(
        decisions=decisions,
        platform_objectives=objectives,
    )

    return result