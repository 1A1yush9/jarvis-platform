from fastapi import FastAPI, Request

from brains.signal_awareness import signal_awareness
from brains.memory_buffer import memory_buffer

app = FastAPI(title="Jarvis Core")


# =====================================================
# STARTUP EVENT
# =====================================================
@app.on_event("startup")
async def startup_event():
    signal_awareness.observe_event("system_startup")


# =====================================================
# SIGNAL LISTENER (PASSIVE)
# =====================================================
@app.middleware("http")
async def signal_listener(request: Request, call_next):

    # observe request
    signal_awareness.observe_request(
        path=request.url.path,
        method=request.method
    )

    response = await call_next(request)

    # store snapshot AFTER response (non-blocking)
    memory_buffer.store_snapshot(
        signal_awareness.report()
    )

    return response


# =====================================================
# BASIC ENDPOINTS
# =====================================================
@app.get("/")
def root():
    return {"message": "Jarvis Core Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


# =====================================================
# SIGNAL REPORT
# =====================================================
@app.get("/signals/report")
def signal_report():
    return signal_awareness.report()


# =====================================================
# MEMORY REPORT (NEW)
# =====================================================
@app.get("/memory/report")
def memory_report():
    return memory_buffer.report()