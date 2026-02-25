# app/main.py

from fastapi import FastAPI
from typing import Dict, Any
import uuid

from core.session_manager import SessionManager
from core.memory import Memory
from core.persistent_memory import PersistentMemory

app = FastAPI(title="Jarvis Strategic Intelligence API")

# --------------------------------------------------
# SYSTEM MODULES
# --------------------------------------------------

session_manager = SessionManager()
memory = Memory()
persistent_memory = PersistentMemory()


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

    # SESSION
    session_id = payload.get("session_id") or str(uuid.uuid4())
    session_info = session_manager.get_session(session_id)

    # SIGNALS
    signals = payload.get("signals", {})

    # Simulated awareness output (existing pipeline)
    awareness = {"status": "processed"}

    # In-memory memory
    memory.store(signals, awareness)

    # Persistent memory (NEW)
    persistent_memory.store(signals, awareness)

    return {
        "session_id": session_id,
        "session_info": session_info,
        "memory_status": "stored",
        "persistent_records": len(persistent_memory.recent()),
        "notice": "Advisory intelligence only"
    }