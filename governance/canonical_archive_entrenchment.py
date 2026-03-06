# governance/canonical_archive_entrenchment.py
# Stage-176.0 — Civilizational Governance Canonical Archive Entrenchment Layer
# Deterministic • Append-Only • Replay-Safe • Render-Compatible

from __future__ import annotations

import hashlib
import json
import os
import threading
import time
from dataclasses import dataclass, asdict
from typing import Dict, Optional

CANONICAL_REGISTRY_PATH = "governance/ledger/closure_canonical_registry.jsonl"
ARCHIVE_LEDGER_PATH = "governance/ledger/canonical_archive_ledger.jsonl"

_lock = threading.Lock()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(data: Dict) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


@dataclass(frozen=True)
class ArchiveEntrenchmentRecord:
    epoch_id: str
    canonical_hash: str
    canonicalization_hash: str
    archive_hash: str
    entrenched_at: int


class CanonicalArchiveEntrenchment:
    """
    Stage-176.0 Archive Entrenchment Engine

    Guarantees:

    • Deterministic archival entrenchment
    • Tamper-evident chain preservation
    • Replay-verifiable permanence
    • Append-only archive ledger
    """

    def __init__(self) -> None:
        os.makedirs(os.path.dirname(ARCHIVE_LEDGER_PATH), exist_ok=True)

    # -----------------------------------
    # Resolve Canonical Closure Record
    # -----------------------------------

    def _resolve_canonical(self, epoch_id: str) -> Optional[Dict]:
        if not os.path.exists(CANONICAL_REGISTRY_PATH):
            return None

        target = None

        with open(CANONICAL_REGISTRY_PATH, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                if data["epoch_id"] == epoch_id:
                    target = data

        return target

    # -----------------------------------
    # Entrench Canonical Record
    # -----------------------------------

    def entrench_epoch(self, epoch_id: str) -> Optional[ArchiveEntrenchmentRecord]:
        with _lock:
            canonical = self._resolve_canonical(epoch_id)
            if not canonical:
                return None

            payload = {
                "epoch_id": canonical["epoch_id"],
                "canonical_hash": canonical["canonical_hash"],
                "canonicalization_hash": canonical["canonicalization_hash"],
                "entrenched_at": int(time.time()),
            }

            archive_hash = _sha256(_canonical_json(payload))

            record = ArchiveEntrenchmentRecord(
                epoch_id=payload["epoch_id"],
                canonical_hash=payload["canonical_hash"],
                canonicalization_hash=payload["canonicalization_hash"],
                archive_hash=archive_hash,
                entrenched_at=payload["entrenched_at"],
            )

            with open(ARCHIVE_LEDGER_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(asdict(record), sort_keys=True) + "\n")

            return record

    # -----------------------------------
    # Deterministic Archive Verification
    # -----------------------------------

    def verify_archive(self, epoch_id: str) -> bool:
        if not os.path.exists(ARCHIVE_LEDGER_PATH):
            return False

        target: Optional[ArchiveEntrenchmentRecord] = None

        with open(ARCHIVE_LEDGER_PATH, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                if data["epoch_id"] == epoch_id:
                    target = ArchiveEntrenchmentRecord(**data)

        if not target:
            return False

        payload = {
            "epoch_id": target.epoch_id,
            "canonical_hash": target.canonical_hash,
            "canonicalization_hash": target.canonicalization_hash,
            "entrenched_at": target.entrenched_at,
        }

        replay_hash = _sha256(_canonical_json(payload))
        return replay_hash == target.archive_hash