from fastapi import FastAPI
from typing import Dict, Any

from core.executive_alignment_engine import ExecutiveAlignmentEngine
from core.strategic_memory import StrategicMemory
from core.executive_intent_model import ExecutiveIntentModel
from core.cognitive_consistency_governor import CognitiveConsistencyGovernor
from core.executive_foresight_engine import ExecutiveForesightEngine
from core.strategic_pressure_analyzer import StrategicPressureAnalyzer
from core.executive_equilibrium_engine import ExecutiveEquilibriumEngine

app = FastAPI(title="Jarvis Executive Intelligence API")

alignment_engine = ExecutiveAlignmentEngine()
strategic_memory = StrategicMemory()
intent_model = ExecutiveIntentModel()
consistency_governor = CognitiveConsistencyGovernor()
foresight_engine = ExecutiveForesightEngine()
pressure_analyzer = StrategicPressureAnalyzer()
equilibrium_engine = ExecutiveEquilibriumEngine()


@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE",
        "stage": "27.0",
        "mode": "Advisory Cognition Only",
    }


# ---------------------------------------------------
# Full Executive Cognitive Stack + Equilibrium
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

    consistency_result = consistency_governor.evaluate_consistency(
        alignment_result,
        intent_result,
        simulation_output,
    )

    foresight_result = foresight_engine.project_future(
        alignment_result,
        intent_result,
        consistency_result,
    )

    pressure_result = pressure_analyzer.analyze_pressure(
        alignment_result,
        intent_result,
        consistency_result,
        foresight_result,
    )

    equilibrium_result = equilibrium_engine.evaluate_equilibrium(
        alignment_result,
        consistency_result,
        foresight_result,
        pressure_result,
    )

    return {
        "stage": "27.0",
        "alignment_analysis": alignment_result,
        "strategic_memory": memory_result,
        "executive_intent": intent_result,
        "cognitive_consistency": consistency_result,
        "executive_foresight": foresight_result,
        "strategic_pressure": pressure_result,
        "executive_equilibrium": equilibrium_result,
    }