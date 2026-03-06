# governance/closure_canonicalizer.py
# Stage-175.0 — Civilizational Governance Closure Canonicalization Final Layer
# Deterministic • Append-Only • Replay-Safe • Render-Compatible

from __future__ import annotations

import hashlib
import json
import os
import threading
import time
from dataclasses import dataclass, asdict
from typing import Dict, Optional

CANONICAL_LEDGER_PATH = "governance/ledger/closure_canonical_registry.jsonl"

_lock = threading.Lock()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(data: Dict) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


@dataclass(frozen=True)
class CanonicalClosureRecord:
    epoch_id: str
    canonical_hash: str
    attestation_count: int
    finalized_at: int
    canonicalization_hash: str


class ClosureCanonicalizer:
    """
    Stage-175.0 Canonicalization Engine

    Guarantees:

    • Final deterministic closure anchor
    • Consensus-aligned canonical materialization
    • Replay-verifiable finalization
    • Append-only canonical registry
    """

    def __init__(self) -> None:
        os.makedirs(os.path.dirname(CANONICAL_LEDGER_PATH), exist_ok=True)

    # -----------------------------------
    # Canonicalization Execution
    # -----------------------------------

    def finalize_canonical_closure(
        self,
        epoch_id: str,
        consensus_hash: str,
        attestation_count: int,
    ) -> CanonicalClosureRecord:

        with _lock:
            payload = {
                "epoch_id": epoch_id,
                "canonical_hash": consensus_hash,
                "attestation_count": attestation_count,
                "finalized_at": int(time.time()),
            }

            canonicalization_hash = _sha256(_canonical_json(payload))

            record = CanonicalClosureRecord(
                epoch_id=epoch_id,
                canonical_hash=consensus_hash,
                attestation_count=attestation_count,
                finalized_at=payload["finalized_at"],
                canonicalization_hash=canonicalization_hash,
            )

            with open(CANONICAL_LEDGER_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(asdict(record), sort_keys=True) + "\n")

            return record

    # -----------------------------------
    # Deterministic Replay Verification
    # -----------------------------------

    def verify_canonical_closure(self, epoch_id: str) -> bool:
        if not os.path.exists(CANONICAL_LEDGER_PATH):
            return False

        target: Optional[CanonicalClosureRecord] = None

        with open(CANONICAL_LEDGER_PATH, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                if data["epoch_id"] == epoch_id:
                    target = CanonicalClosureRecord(**data)

        if not target:
            return False

        payload = {
            "epoch_id": target.epoch_id,
            "canonical_hash": target.canonical_hash,
            "attestation_count": target.attestation_count,
            "finalized_at": target.finalized_at,
        }

        replay_hash = _sha256(_canonical_json(payload))

        return replay_hash == target.canonicalization_hash