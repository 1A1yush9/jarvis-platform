# app/monitoring/event_logger.py

import json
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("jarvis_events.json")


class EventLogger:

    def log(self, event_type: str, payload: dict, client_id: str = "global"):

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "client_id": client_id,
            "event_type": event_type,
            "payload": payload,
        }

        print(f"[JARVIS EVENT] {record}")

        try:
            if LOG_PATH.exists():
                data = json.loads(LOG_PATH.read_text())
            else:
                data = []

            data.append(record)
            LOG_PATH.write_text(json.dumps(data, indent=2))

        except Exception as e:
            print(f"[LOGGER ERROR] {e}")


event_logger = EventLogger()