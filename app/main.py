# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.core.system_state import system_state
from app.core.action_gateway import action_gateway
from app.monitoring.event_logger import event_logger
from app.observer.activity_observer import observer
from app.observer.adaptive_engine import adaptive_engine

app = FastAPI(title="Jarvis Platform", version="4.5")


class ActionRequest(BaseModel):
    action: str
    payload: dict = {}


@app.get("/")
def root():
    return {"message": "Jarvis API Running"}


@app.get("/system/status")
def system_status():
    return system_state.health()


@app.get("/observer/summary")
def observer_summary():
    return observer.system_summary()


@app.get("/adaptive/recommendations")
def adaptive_recommendations():
    return adaptive_engine.generate_recommendations()


@app.post("/action")
def execute_action(request: ActionRequest):

    try:
        action_gateway.validate(request.action, request.payload)

        result = {
            "message": "Action executed successfully",
            "action": request.action,
            "payload": request.payload,
        }

        event_logger.log("action_executed", result)

        return result

    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))