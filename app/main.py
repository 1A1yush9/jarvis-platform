# app/main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import time

# ---- Jarvis Core Imports ----
from app.core.execution_pipeline import (
    propose_action,
    execute_with_token
)

from app.core.human_authorization import approve_token


# ==========================================================
# FASTAPI APPLICATION
# ==========================================================

app = FastAPI(
    title="Jarvis Cognitive System",
    description="Human-Governed AI Execution Platform",
    version="4.3"
)

START_TIME = time.time()


# ==========================================================
# ROOT + HEALTH CHECK
# ==========================================================

@app.get("/")
def root():
    return {
        "system": "Jarvis",
        "status": "ONLINE",
        "stage": "4.3 - Human Authorization Layer Active"
    }


@app.get("/health")
def health():
    uptime = round(time.time() - START_TIME, 2)

    return {
        "status": "healthy",
        "uptime_seconds": uptime,
        "execution_mode": "HUMAN_AUTH_REQUIRED"
    }


@app.get("/jarvis/status")
def jarvis_status():
    return {
        "cognitive_stack": "ACTIVE",
        "autonomous_execution": False,
        "human_authorization": "REQUIRED",
        "sandbox": "ENABLED",
        "capability_gate": "ENFORCED"
    }


# ==========================================================
# HUMAN AUTHORIZATION FLOW
# ==========================================================

@app.post("/jarvis/propose")
def jarvis_propose(action: dict):
    """
    Jarvis proposes an action.
    Execution waits for human approval.
    """
    try:
        response = propose_action(action)
        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "ERROR",
                "message": str(e)
            }
        )


@app.post("/jarvis/approve/{token}")
def jarvis_approve(token: str):
    """
    Human approves proposed action.
    """
    try:
        result = approve_token(token)
        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "ERROR",
                "message": str(e)
            }
        )


@app.post("/jarvis/execute/{token}")
def jarvis_execute(token: str):
    """
    Executes only after approval token validation.
    """
    try:
        result = execute_with_token(token)
        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "ERROR",
                "message": str(e)
            }
        )


# ==========================================================
# GLOBAL ERROR HANDLER (PREVENT RENDER RESTART LOOPS)
# ==========================================================

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "status": "SYSTEM_ERROR",
            "detail": str(exc)
        },
    )