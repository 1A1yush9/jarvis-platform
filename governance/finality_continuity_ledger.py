"""
Jarvis Platform — Stage-187.0
Finality Continuity Ledger (Append-Only)

Deterministic | Immutable Safe
"""

from __future__ import annotations

import json
import os
from typing import List, Dict, Any


class FinalityContinuityLedger:

    def __init__(self, path: str = "ledger/finality_continuity_ledger.jsonl"):
        self.path = path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def append(self, record: Dict[str, Any]) -> None:
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, separators=(",", ":")) + "\n")

    def read_all(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.path):
            return []

        with open(self.path, "r", encoding="utf-8") as f:
            return [json.loads(line.strip()) for line in f if line.strip()]