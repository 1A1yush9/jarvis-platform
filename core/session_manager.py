# core/session_manager.py

"""
Stage-15.2 — Intelligence Session Tracking
Maintains lightweight session continuity.
Render-safe (in-memory only).
"""

from datetime import datetime
from typing import Dict, Any


class SessionManager:

    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}

    # --------------------------------------------------
    # Get or Create Session
    # --------------------------------------------------
    def get_session(self, session_id: str):

        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "created_at": datetime.utcnow().isoformat(),
                "request_count": 0,
                "last_activity": None,
            }

        self.sessions[session_id]["request_count"] += 1
        self.sessions[session_id]["last_activity"] = (
            datetime.utcnow().isoformat()
        )

        return self.sessions[session_id]

    # --------------------------------------------------
    # Session Summary
    # --------------------------------------------------
    def summary(self, session_id: str):

        return self.sessions.get(
            session_id,
            {"status": "unknown_session"}
        )