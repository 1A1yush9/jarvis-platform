# app/monitoring/event_logger.py

import json
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("jarvis_events.json")


class EventLogger:
    """
    Stage-4.3 Logging Layer
    - Console logging
    - JSON persistent logging
    - Future DB hook ready
    """

    def log(self, event_type: str, payload: dict):

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "payload": payload,
        }

        # Console log
        print(f"[JARVIS EVENT] {record}")

        # File log (safe append)
        try:
            if LOG_PATH.exists():
                data = json.loads(LOG_PATH.read_text())
            else:
                data = []

            data.append(record)
            LOG_PATH.write_text(json.dumps(data, indent=2))

        except Exception as e:
            print(f"[LOGGER ERROR] {e}")

        # ---- FUTURE DATABASE HOOK (Stage-B ready) ----
        # self.send_to_database(record)


event_logger = EventLogger()