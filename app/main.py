# app/main.py

from fastapi import FastAPI
from typing import Dict, Any
import uuid

from core.session_manager import SessionManager
from core.persistent_memory import PersistentMemory
from core.telemetry import Telemetry
from core.control_plane import ControlPlane
from core.access_control import AccessControl
from core.client_isolation import ClientIsolation
from core.revenue_intelligence import RevenueIntelligence

app = FastAPI(title="Jarvis Strategic Intelligence API")

# --------------------------------------------------
# SYSTEM MODULES
# --------------------------------------------------

session_manager = SessionManager()
persistent_memory = PersistentMemory()
telemetry = Telemetry()
control_plane = ControlPlane()
access_control = AccessControl()
client_isolation = ClientIsolation()
revenue_intelligence = RevenueIntelligence()


# --------------------------------------------------
# HEALTH
# --------------------------------------------------

@app.get("/")
def health():
    return {
        "status": "Jarvis LIVE",
        "mode": control_plane.status(),
        "telemetry": telemetry.status()
    }


# --------------------------------------------------
# CONTROL MODE
# --------------------------------------------------

@app.post("/control/mode")
def change_mode(payload: Dict[str, Any]):

    role = access_control.get_role(payload.get("api_key", ""))

    if not access_control.allowed(role, "control"):
        return {"error": "permission_denied"}

    return control_plane.set_mode(payload.get("mode", ""))


# --------------------------------------------------
# ANALYZE
# --------------------------------------------------

@app.post("/analyze")
def analyze(payload: Dict[str, Any]):

    role = access_control.get_role(payload.get("api_key", ""))

    if not access_control.allowed(role, "analyze"):
        return {"error": "access_denied"}

    if not control_plane.allow_processing():
        return {"status": "maintenance_mode"}

    start = telemetry.start_timer()

    try:
        client_id = payload.get("client_id", "default_client")
        session_id = payload.get("session_id") or str(uuid.uuid4())

        session_manager.get_session(session_id)

        signals = payload.get("signals", {})
        awareness = {"status": "processed"}

        # Client isolated memory
        client_isolation.store_memory(
            client_id,
            {"signals": signals, "awareness": awareness}
        )

        # Persistent memory
        persistent_memory.store(signals, awareness)

        # Revenue intelligence (NEW)
        revenue_state = revenue_intelligence.evaluate(
            client_id,
            signals
        )

        telemetry.end_timer(start)

        return {
            "client": client_id,
            "revenue_intelligence": revenue_state,
            "telemetry": telemetry.status(),
            "notice": "Advisory intelligence only"
        }

    except Exception as e:
        telemetry.record_error()
        return {
            "error": str(e),
            "telemetry": telemetry.status()
        }