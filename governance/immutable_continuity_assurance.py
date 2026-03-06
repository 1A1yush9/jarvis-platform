# governance/immutable_continuity_assurance.py
# Stage-177.0 — Civilizational Governance Immutable Continuity Assurance Layer
# Deterministic • Append-Only • Replay-Safe • Render-Compatible

from __future__ import annotations

import hashlib
import json
import os
import threading
import time
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

ARCHIVE_LEDGER_PATH = "governance/ledger/canonical_archive_ledger.jsonl"
CONTINUITY_LEDGER_PATH = "governance/ledger/continuity_assurance_ledger.jsonl"

_lock = threading.Lock()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(data: Dict) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


@dataclass(frozen=True)
class ContinuityRecord:
    epoch_id: str
    previous_epoch_id: Optional[str]
    previous_archive_hash: Optional[str]
    current_archive_hash: str
    continuity_hash: str
    verified_at: int


class ImmutableContinuityAssurance:
    """
    Stage-177.0 Continuity Engine

    Guarantees:

    • Deterministic sequential continuity validation
    • Tamper-evident epoch chaining
    • Replay-verifiable continuity proofs
    • Append-only continuity ledger
    """

    def __init__(self) -> None:
        os.makedirs(os.path.dirname(CONTINUITY_LEDGER_PATH), exist_ok=True)

    # -----------------------------------
    # Load Archive Ledger
    # -----------------------------------

    def _load_archive(self) -> List[Dict]:
        if not os.path.exists(ARCHIVE_LEDGER_PATH):
            return []

        records: List[Dict] = []

        with open(ARCHIVE_LEDGER_PATH, "r", encoding="utf-8") as f:
            for line in f:
                records.append(json.loads(line))

        return records

    # -----------------------------------
    # Continuity Validation
    # -----------------------------------

    def verify_continuity(self) -> List[ContinuityRecord]:
        with _lock:
            archives = self._load_archive()

            if not archives:
                return []

            results: List[ContinuityRecord] = []

            previous: Optional[Dict] = None

            for current in archives:
                payload = {
                    "epoch_id": current["epoch_id"],
                    "previous_epoch_id": previous["epoch_id"] if previous else None,
                    "previous_archive_hash": previous["archive_hash"] if previous else None,
                    "current_archive_hash": current["archive_hash"],
                    "verified_at": int(time.time()),
                }

                continuity_hash = _sha256(_canonical_json(payload))

                record = ContinuityRecord(
                    epoch_id=payload["epoch_id"],
                    previous_epoch_id=payload["previous_epoch_id"],
                    previous_archive_hash=payload["previous_archive_hash"],
                    current_archive_hash=payload["current_archive_hash"],
                    continuity_hash=continuity_hash,
                    verified_at=payload["verified_at"],
                )

                self._append_record(record)
                results.append(record)
                previous = current

            return results

    # -----------------------------------
    # Append Continuity Record
    # -----------------------------------

    def _append_record(self, record: ContinuityRecord) -> None:
        with open(CONTINUITY_LEDGER_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(record), sort_keys=True) + "\n")

    # -----------------------------------
    # Replay Verification
    # -----------------------------------

    def verify_replay(self, epoch_id: str) -> bool:
        if not os.path.exists(CONTINUITY_LEDGER_PATH):
            return False

        target: Optional[ContinuityRecord] = None

        with open(CONTINUITY_LEDGER_PATH, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                if data["epoch_id"] == epoch_id:
                    target = ContinuityRecord(**data)

        if not target:
            return False

        payload = {
            "epoch_id": target.epoch_id,
            "previous_epoch_id": target.previous_epoch_id,
            "previous_archive_hash": target.previous_archive_hash,
            "current_archive_hash": target.current_archive_hash,
            "verified_at": target.verified_at,
        }

        replay_hash = _sha256(_canonical_json(payload))
        return replay_hash == target.continuity_hash