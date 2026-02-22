# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.core.system_state import system_state
from app.core.action_gateway import action_gateway
from app.monitoring.event_logger import event_logger

app = FastAPI(title="Jarvis Platform", version="4.3")


# ---------------------------
# Request Schema
# ---------------------------
class ActionRequest(BaseModel):
    action: str
    payload: dict = {}


# ---------------------------
# System Health Endpoint
# ---------------------------
@app.get("/system/status")
def system_status():
    return system_state.health()


# ---------------------------
# Core Action Endpoint
# ---------------------------
@app.post("/action")
def execute_action(request: ActionRequest):

    try:
        # Validate action
        action_gateway.validate(request.action, request.payload)

        # Simulated execution (Stage-4.3 base)
        result = {
            "message": "Action executed successfully",
            "action": request.action,
            "payload": request.payload,
        }

        event_logger.log(
            "action_executed",
            result,
        )

        return result

    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ---------------------------
# Root Endpoint
# ---------------------------
@app.get("/")
def root():
    return {"message": "Jarvis API Running"}