# jarvis/main.py

from fastapi import FastAPI, Request
import time

# ---- Existing Observer import (keep if already used) ----
try:
    from jarvis.brains.observer import observer_brain
except Exception:
    observer_brain = None

# ---- NEW Signal Awareness ----
from .brains.signal_awareness import signal_awareness


app = FastAPI(title="Jarvis Core")


# =========================================================
# HEARTBEAT LOOP (SAFE BACKGROUND)
# =========================================================
@app.on_event("startup")
async def startup_event():
    signal_awareness.observe_event("system_startup")


# =========================================================
# SIGNAL LISTENER MIDDLEWARE (PASSIVE)
# =========================================================
@app.middleware("http")
async def signal_listener(request: Request, call_next):

    # observe request safely
    signal_awareness.observe_request(
        path=request.url.path,
        method=request.method
    )

    response = await call_next(request)
    return response


# =========================================================
# BASIC ENDPOINTS
# =========================================================
@app.get("/")
def root():
    return {"message": "Jarvis Core Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


# =========================================================
# OBSERVER REPORT (if exists)
# =========================================================
@app.get("/observer/report")
def observer_report():
    if observer_brain:
        return observer_brain.report()
    return {"observer": "not_loaded"}


# =========================================================
# SIGNAL REPORT (NEW)
# =========================================================
@app.get("/signals/report")
def signal_report():
    return signal_awareness.report()