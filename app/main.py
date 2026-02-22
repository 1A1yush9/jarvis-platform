# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.core.system_state import system_state
from app.core.action_gateway import action_gateway
from app.core.client_context import client_context
from app.core.auth_manager import auth_manager
from app.core.usage_meter import usage_meter
from app.monitoring.event_logger import event_logger
from app.observer.activity_observer import observer
from app.observer.adaptive_engine import adaptive_engine

app = FastAPI(title="Jarvis Platform", version="5.2")


class ActionRequest(BaseModel):
    client_id: str
    api_key: str
    action: str
    payload: dict = {}


@app.get("/")
def root():
    return {"message": "Jarvis Platform Running"}


@app.get("/system/status")
def system_status():
    return system_state.health()


@app.get("/observer/summary")
def observer_summary():
    return observer.system_summary()


@app.get("/adaptive/recommendations")
def adaptive_recommendations():
    return adaptive_engine.generate_recommendations()


@app.get("/usage/{client_id}")
def usage_summary(client_id: str):
    return usage_meter.summary(client_id)


@app.post("/action")
def execute_action(request: ActionRequest):

    try:
        # 🔐 Authenticate
        auth_manager.verify(request.client_id, request.api_key)

        # 👤 Client context
        client_context.get_client(request.client_id)

        # 💰 Record usage
        usage_meter.record(request.client_id, request.action)

        # 🧠 Validate action
        action_gateway.validate(request.action, request.payload)

        result = {
            "client_id": request.client_id,
            "message": "Action executed successfully",
            "action": request.action,
            "payload": request.payload,
        }

        event_logger.log(
            "action_executed",
            result,
            client_id=request.client_id,
        )

        return result

    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))

    except Exception as e:
        raise e