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
from brains.action_sandbox import action_sandbox

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


@app.get("/gate/status")
def gate_status():
    return capability_gate.get_status()


# ---------------------------------
# NEW: Sandbox Action Attempt
# ---------------------------------
@app.get("/action/test")
def action_test():
    return action_sandbox.execute("test_action")


@app.get("/action/report")
def action_report():
    return action_sandbox.report()