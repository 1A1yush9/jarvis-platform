# app/main.py

from fastapi import FastAPI
from typing import Dict, Any
import uuid

from core.session_manager import SessionManager
from core.memory import Memory

app = FastAPI(title="Jarvis Strategic Intelligence API")

# --------------------------------------------------
# SYSTEM MODULES
# --------------------------------------------------

session_manager = SessionManager()
memory = Memory()


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/")
def health():
    return {"status": "Jarvis LIVE", "mode": "advisory"}


# --------------------------------------------------
# INTELLIGENCE ENDPOINT
# --------------------------------------------------

@app.post("/analyze")
def analyze(payload: Dict[str, Any]):

    # ---------------- SESSION ----------------
    session_id = payload.get("session_id")

    if not session_id:
        session_id = str(uuid.uuid4())

    session_info = session_manager.get_session(session_id)

    # ---------------- SIGNALS ----------------
    signals = payload.get("signals", {})

    # (pipeline already running internally)
    awareness = {"status": "processed"}

    memory.store(signals, awareness)
    memory_summary = memory.summary()

    return {
        "session_id": session_id,
        "session_info": session_info,
        "memory": memory_summary,
        "notice": "Advisory intelligence only"
    }