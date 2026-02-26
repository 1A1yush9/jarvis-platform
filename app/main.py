from fastapi import FastAPI
from typing import Dict, Any

from core.executive_alignment_engine import ExecutiveAlignmentEngine
from core.strategic_memory import StrategicMemory
from core.executive_intent_model import ExecutiveIntentModel
from core.cognitive_consistency_governor import CognitiveConsistencyGovernor
from core.executive_foresight_engine import ExecutiveForesightEngine
from core.strategic_pressure_analyzer import StrategicPressureAnalyzer
from core.executive_equilibrium_engine import ExecutiveEquilibriumEngine
from core.meta_strategy_synthesizer import MetaStrategySynthesizer
from core.executive_self_calibration import ExecutiveSelfCalibration
from core.strategic_awareness_loop import StrategicAwarenessLoop
from core.executive_meta_reasoning import ExecutiveMetaReasoning
from core.executive_cognitive_stability import ExecutiveCognitiveStability
from core.executive_intelligence_convergence import ExecutiveIntelligenceConvergence
from core.executive_continuity_kernel import ExecutiveContinuityKernel
from core.executive_strategic_consciousness import ExecutiveStrategicConsciousness

app = FastAPI(title="Jarvis Executive Intelligence API")

alignment_engine = ExecutiveAlignmentEngine()
strategic_memory = StrategicMemory()
intent_model = ExecutiveIntentModel()
consistency_governor = CognitiveConsistencyGovernor()
foresight_engine = ExecutiveForesightEngine()
pressure_analyzer = StrategicPressureAnalyzer()
equilibrium_engine = ExecutiveEquilibriumEngine()
meta_synthesizer = MetaStrategySynthesizer()
self_calibration = ExecutiveSelfCalibration()
awareness_loop = StrategicAwarenessLoop()
meta_reasoning = ExecutiveMetaReasoning()
cognitive_stability = ExecutiveCognitiveStability()
convergence_engine = ExecutiveIntelligenceConvergence()
continuity_kernel = ExecutiveContinuityKernel()
strategic_consciousness = ExecutiveStrategicConsciousness()


@app.get("/")
def root():
    return {
        "status": "Jarvis LIVE",
        "stage": "31.0",
        "mode": "Advisory Cognition Only",
    }


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

    meta_strategy_result = meta_synthesizer.synthesize(
        alignment_result,
        intent_result,
        consistency_result,
        foresight_result,
        pressure_result,
        equilibrium_result,
    )

    calibration_result = self_calibration.calibrate(
        alignment_result,
        consistency_result,
        foresight_result,
        pressure_result,
        equilibrium_result,
        meta_strategy_result,
    )

    awareness_result = awareness_loop.update_awareness(
        calibration_result
    )

    meta_reasoning_result = meta_reasoning.evaluate_reasoning(
        meta_strategy_result,
        calibration_result,
        awareness_result,
    )

    stability_result = cognitive_stability.update_stability(
        meta_reasoning_result
    )

    convergence_result = convergence_engine.converge(
        alignment_result,
        consistency_result,
        foresight_result,
        pressure_result,
        equilibrium_result,
        meta_strategy_result,
        calibration_result,
        meta_reasoning_result,
        stability_result,
    )

    continuity_result = continuity_kernel.update_continuity(
        convergence_result
    )

    consciousness_result = strategic_consciousness.update_consciousness(
        convergence_result,
        continuity_result,
    )

    return {
        "stage": "31.0",
        "alignment_analysis": alignment_result,
        "strategic_memory": memory_result,
        "executive_intent": intent_result,
        "cognitive_consistency": consistency_result,
        "executive_foresight": foresight_result,
        "strategic_pressure": pressure_result,
        "executive_equilibrium": equilibrium_result,
        "meta_strategy": meta_strategy_result,
        "self_calibration": calibration_result,
        "strategic_awareness": awareness_result,
        "meta_reasoning": meta_reasoning_result,
        "cognitive_stability": stability_result,
        "executive_intelligence": convergence_result,
        "executive_continuity": continuity_result,
        "strategic_consciousness": consciousness_result,
    }