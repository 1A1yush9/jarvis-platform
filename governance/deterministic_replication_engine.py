# deterministic_replication_engine.py
# Deterministic Replication Engine (Stage-171.0 Compatible)

from __future__ import annotations

import hashlib
import json
import os
from typing import List


LEDGER_PATH = "governance/ledger/governance_ledger.jsonl"


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class DeterministicReplicationEngine:
    """
    Guarantees:

    • Replay determinism
    • Hash-consistent replication
    • Immutable governance alignment
    """

    def __init__(self) -> None:
        pass

    def read_ledger(self) -> List[str]:
        if not os.path.exists(LEDGER_PATH):
            return []

        with open(LEDGER_PATH, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f]

    def compute_state_hash(self) -> str:
        entries = self.read_ledger()
        canonical_blob = "\n".join(entries).encode("utf-8")
        return _sha256(canonical_blob)

    def deterministic_replay(self) -> dict:
        entries = self.read_ledger()
        return {
            "entry_count": len(entries),
            "state_hash": self.compute_state_hash(),
        }

    def verify_external_state(self, external_hash: str) -> bool:
        return self.compute_state_hash() == external_hash