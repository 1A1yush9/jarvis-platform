# app/main.py

from fastapi import FastAPI
from typing import Dict, Any
import uuid

from core.session_manager import SessionManager
from core.memory import Memory
from core.persistent_memory import PersistentMemory
from core.telemetry import Telemetry
from core.control_plane import ControlPlane
from core.access_control import AccessControl

app = FastAPI(title="Jarvis Strategic Intelligence API")

# --------------------------------------------------
# SYSTEM MODULES
# --------------------------------------------------

session_manager = SessionManager()
memory = Memory()
persistent_memory = PersistentMemory()
telemetry = Telemetry()
control_plane = ControlPlane()
access_control = AccessControl()


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/")
def health():
    return {
        "status": "Jarvis LIVE",
        "mode": control_plane.status(),
        "telemetry": telemetry.status()
    }


# --------------------------------------------------
# CHANGE MODE (OWNER ONLY)
# --------------------------------------------------

@app.post("/control/mode")
def change_mode(payload: Dict[str, Any]):

    api_key = payload.get("api_key", "")
    role = access_control.get_role(api_key)

    if not access_control.allowed(role, "control"):
        return {"error": "permission_denied"}

    return control_plane.set_mode(payload.get("mode", ""))


# --------------------------------------------------
# INTELLIGENCE ENDPOINT
# --------------------------------------------------

@app.post("/analyze")
def analyze(payload: Dict[str, Any]):

    api_key = payload.get("api_key", "")
    role = access_control.get_role(api_key)

    if not access_control.allowed(role, "analyze"):
        return {"error": "access_denied"}

    if not control_plane.allow_processing():
        return {
            "status": "maintenance_mode",
            "message": "Processing disabled"
        }

    start = telemetry.start_timer()

    try:
        session_id = payload.get("session_id") or str(uuid.uuid4())
        session_info = session_manager.get_session(session_id)

        signals = payload.get("signals", {})
        awareness = {"status": "processed"}

        memory.store(signals, awareness)
        persistent_memory.store(signals, awareness)

        telemetry.end_timer(start)

        return {
            "role": role,
            "session_id": session_id,
            "telemetry": telemetry.status(),
            "notice": "Advisory intelligence only"
        }

    except Exception as e:
        telemetry.record_error()
        return {
            "error": str(e),
            "telemetry": telemetry.status()
        }