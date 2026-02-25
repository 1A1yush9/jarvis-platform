# core/persistent_memory.py

"""
Stage-15.3 Persistent Intelligence Memory
SQLite-based storage (Render safe)
"""

import sqlite3
import json
from datetime import datetime
from typing import Dict, Any, List


class PersistentMemory:

    def __init__(self, db_path: str = "jarvis_memory.db"):
        self.db_path = db_path
        self._init_db()

    # --------------------------------------------------
    # Initialize Database
    # --------------------------------------------------
    def _init_db(self):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                signals TEXT,
                awareness TEXT
            )
        """)

        conn.commit()
        conn.close()

    # --------------------------------------------------
    # Store Record
    # --------------------------------------------------
    def store(self, signals: Dict[str, Any], awareness: Dict[str, Any]):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO memory (timestamp, signals, awareness) VALUES (?, ?, ?)",
            (
                datetime.utcnow().isoformat(),
                json.dumps(signals),
                json.dumps(awareness),
            ),
        )

        conn.commit()
        conn.close()

    # --------------------------------------------------
    # Load Recent Records
    # --------------------------------------------------
    def recent(self, limit: int = 20) -> List[Dict[str, Any]]:

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT timestamp, signals, awareness FROM memory ORDER BY id DESC LIMIT ?",
            (limit,),
        )

        rows = cursor.fetchall()
        conn.close()

        results = []
        for r in rows:
            results.append({
                "timestamp": r[0],
                "signals": json.loads(r[1]),
                "awareness": json.loads(r[2]),
            })

        return results