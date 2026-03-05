"""
CTSG Telemetry Client

Append-only deterministic governance telemetry.
Render-safe implementation.
"""

import json
import os
from typing import Dict, Any


class CTSGTelemetryClient:

    def __init__(self):
        self._log_path = os.getenv(
            "CTSG_TELEMETRY_PATH",
            "/tmp/ctsg_telemetry.log"
        )

    def emit(self, payload: Dict[str, Any]) -> None:
        serialized = json.dumps(payload, sort_keys=True)

        with open(self._log_path, "a", encoding="utf-8") as f:
            f.write(serialized + "\n")