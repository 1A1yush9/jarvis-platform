from fastapi import FastAPI, Request

from brains.signal_awareness import signal_awareness
from brains.memory_buffer import memory_buffer
from brains.pattern_observer import pattern_observer
from brains.intent_classifier import intent_classifier
from brains.adaptive_awareness import adaptive_awareness
from brains.stability_guardian import stability_guardian
from brains.decision_simulator import decision_simulator
from brains.strategic_thinker import strategic_thinker
from brains.meta_cognition import meta_cognition
from brains.capability_gate import capability_gate

app = FastAPI(title="Jarvis Core")


@app.on_event("startup")
async def startup_event():
    signal_awareness.observe_event("system_startup")


@app.middleware("http")
async def signal_listener(request: Request, call_next):

    signal_awareness.observe_request(
        path=request.url.path,
        method=request.method
    )

    response = await call_next(request)

    memory_buffer.store_snapshot(
        signal_awareness.report()
    )

    return response


@app.get("/")
def root():
    return {"message": "Jarvis Core Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/meta/report")
def meta():

    memory_data = memory_buffer.report()
    pattern_data = pattern_observer.analyze(
        memory_data["recent_memory"]
    )

    intent_data = intent_classifier.classify(pattern_data)
    awareness_data = adaptive_awareness.evaluate(intent_data)

    guardian_data = stability_guardian.evaluate(
        memory_data, pattern_data
    )

    decision_data = decision_simulator.simulate(
        awareness_data,
        guardian_data
    )

    strategy_data = strategic_thinker.project(decision_data)

    return meta_cognition.reflect(
        awareness_data,
        strategy_data
    )


# ---------------------------------
# NEW: Capability Gate Status
# ---------------------------------
@app.get("/gate/status")
def gate_status():
    return capability_gate.get_status()