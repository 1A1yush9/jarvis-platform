# governance/immutable_ledger_closure.py
# Stage-171.0 — Civilizational Recursive Governance Immutable Ledger Closure
# Deterministic • Append-Only • Replay-Verifiable • Render-Compatible

from __future__ import annotations

import hashlib
import json
import os
import threading
import time
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional


LEDGER_PATH = "governance/ledger/governance_ledger.jsonl"
CLOSURE_PATH = "governance/ledger/governance_closures.jsonl"
SNAPSHOT_DIR = "governance/ledger/snapshots"


_lock = threading.Lock()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(data: Dict) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


@dataclass(frozen=True)
class LedgerClosureRecord:
    epoch_id: str
    ledger_hash: str
    entry_count: int
    closure_timestamp: int
    closure_hash: str


class ImmutableLedgerClosure:
    """
    Stage-171.0 Closure Engine

    Responsibilities:

    • Deterministic ledger sealing
    • Canonical snapshot generation
    • Cryptographic closure attestation
    • Replay-safe verification
    """

    def __init__(self) -> None:
        os.makedirs(SNAPSHOT_DIR, exist_ok=True)

    # -------------------------------
    # Ledger Read (Deterministic)
    # -------------------------------

    def _read_ledger(self) -> List[str]:
        if not os.path.exists(LEDGER_PATH):
            return []

        with open(LEDGER_PATH, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f]

    # -------------------------------
    # Canonical Ledger Hash
    # -------------------------------

    def compute_ledger_hash(self) -> str:
        entries = self._read_ledger()
        canonical_blob = "\n".join(entries).encode("utf-8")
        return _sha256(canonical_blob)

    # -------------------------------
    # Snapshot Generation
    # -------------------------------

    def _create_snapshot(self, epoch_id: str, entries: List[str]) -> str:
        snapshot_path = os.path.join(SNAPSHOT_DIR, f"ledger_snapshot_{epoch_id}.json")

        snapshot_payload = {
            "epoch_id": epoch_id,
            "entries": entries,
        }

        with open(snapshot_path, "w", encoding="utf-8") as f:
            json.dump(snapshot_payload, f, sort_keys=True, indent=2)

        return snapshot_path

    # -------------------------------
    # Closure Execution (Deterministic)
    # -------------------------------

    def close_epoch(self, epoch_id: str) -> LedgerClosureRecord:
        with _lock:
            entries = self._read_ledger()

            ledger_hash = self.compute_ledger_hash()
            entry_count = len(entries)
            closure_timestamp = int(time.time())

            closure_payload = {
                "epoch_id": epoch_id,
                "ledger_hash": ledger_hash,
                "entry_count": entry_count,
                "closure_timestamp": closure_timestamp,
            }

            closure_hash = _sha256(_canonical_json(closure_payload))

            record = LedgerClosureRecord(
                epoch_id=epoch_id,
                ledger_hash=ledger_hash,
                entry_count=entry_count,
                closure_timestamp=closure_timestamp,
                closure_hash=closure_hash,
            )

            self._append_closure_record(record)
            self._create_snapshot(epoch_id, entries)

            return record

    # -------------------------------
    # Append-Only Closure Record
    # -------------------------------

    def _append_closure_record(self, record: LedgerClosureRecord) -> None:
        os.makedirs(os.path.dirname(CLOSURE_PATH), exist_ok=True)

        with open(CLOSURE_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(record), sort_keys=True) + "\n")

    # -------------------------------
    # Deterministic Replay Verification
    # -------------------------------

    def verify_closure(self, epoch_id: str) -> bool:
        if not os.path.exists(CLOSURE_PATH):
            return False

        target: Optional[LedgerClosureRecord] = None

        with open(CLOSURE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                if data["epoch_id"] == epoch_id:
                    target = LedgerClosureRecord(**data)

        if not target:
            return False

        snapshot_path = os.path.join(SNAPSHOT_DIR, f"ledger_snapshot_{epoch_id}.json")
        if not os.path.exists(snapshot_path):
            return False

        with open(snapshot_path, "r", encoding="utf-8") as f:
            snapshot_data = json.load(f)

        canonical_blob = "\n".join(snapshot_data["entries"]).encode("utf-8")
        replay_hash = _sha256(canonical_blob)

        return replay_hash == target.ledger_hash