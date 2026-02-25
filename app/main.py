# app/main.py

from fastapi import FastAPI
from typing import Dict, Any
import uuid

from core.session_manager import SessionManager
from core.memory import Memory
from core.persistent_memory import PersistentMemory
from core.telemetry import Telemetry

app = FastAPI(title="Jarvis Strategic Intelligence API")

# --------------------------------------------------
# SYSTEM MODULES
# --------------------------------------------------

session_manager = SessionManager()
memory = Memory()
persistent_memory = PersistentMemory()
telemetry = Telemetry()


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/")
def health():
    return {
        "status": "Jarvis LIVE",
        "mode": "advisory",
        "telemetry": telemetry.status()
    }


# --------------------------------------------------
# INTELLIGENCE ENDPOINT
# --------------------------------------------------

@app.post("/analyze")
def analyze(payload: Dict[str, Any]):

    start = telemetry.start_timer()

    try:
        # SESSION
        session_id = payload.get("session_id") or str(uuid.uuid4())
        session_info = session_manager.get_session(session_id)

        # SIGNALS
        signals = payload.get("signals", {})

        # Existing pipeline placeholder
        awareness = {"status": "processed"}

        # MEMORY
        memory.store(signals, awareness)
        persistent_memory.store(signals, awareness)

        telemetry.end_timer(start)

        return {
            "session_id": session_id,
            "session_info": session_info,
            "telemetry": telemetry.status(),
            "notice": "Advisory intelligence only"
        }

    except Exception as e:
        telemetry.record_error()
        return {
            "error": str(e),
            "telemetry": telemetry.status()
        }