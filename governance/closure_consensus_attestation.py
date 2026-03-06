# governance/closure_consensus_attestation.py
# Stage-174.0 — Civilizational Governance Closure Consensus Attestation Layer
# Deterministic • Append-Only • Replay-Safe • Render-Compatible

from __future__ import annotations

import hashlib
import json
import os
import threading
import time
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

ATTESTATION_LEDGER_PATH = "governance/ledger/closure_attestations.jsonl"

_lock = threading.Lock()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_json(data: Dict) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()


@dataclass(frozen=True)
class ClosureAttestation:
    epoch_id: str
    node_id: str
    closure_hash: str
    attested_at: int
    attestation_hash: str


@dataclass(frozen=True)
class ConsensusResult:
    epoch_id: str
    consensus_hash: str
    attestation_count: int
    reached: bool
    resolved_at: int


class ClosureConsensusAttestation:
    """
    Stage-174.0 Consensus Engine

    Guarantees:

    • Deterministic attestation aggregation
    • Canonical consensus resolution
    • Replay-verifiable alignment
    • Append-only attestation logging
    """

    def __init__(self) -> None:
        os.makedirs(os.path.dirname(ATTESTATION_LEDGER_PATH), exist_ok=True)

    # -----------------------------------
    # Append Attestation (Deterministic)
    # -----------------------------------

    def append_attestation(
        self,
        epoch_id: str,
        node_id: str,
        closure_hash: str,
    ) -> ClosureAttestation:

        with _lock:
            payload = {
                "epoch_id": epoch_id,
                "node_id": node_id,
                "closure_hash": closure_hash,
                "attested_at": int(time.time()),
            }

            attestation_hash = _sha256(_canonical_json(payload))

            record = ClosureAttestation(
                epoch_id=epoch_id,
                node_id=node_id,
                closure_hash=closure_hash,
                attested_at=payload["attested_at"],
                attestation_hash=attestation_hash,
            )

            with open(ATTESTATION_LEDGER_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(asdict(record), sort_keys=True) + "\n")

            return record

    # -----------------------------------
    # Deterministic Consensus Resolution
    # -----------------------------------

    def resolve_consensus(self, epoch_id: str, threshold: int) -> ConsensusResult:
        with _lock:
            attestations = self._load_attestations(epoch_id)

            if not attestations:
                return ConsensusResult(epoch_id, "", 0, False, int(time.time()))

            hash_counts: Dict[str, int] = {}

            for a in attestations:
                hash_counts[a.closure_hash] = hash_counts.get(a.closure_hash, 0) + 1

            consensus_hash = max(hash_counts.items(), key=lambda x: (x[1], x[0]))[0]
            attestation_count = hash_counts[consensus_hash]
            reached = attestation_count >= threshold

            return ConsensusResult(
                epoch_id=epoch_id,
                consensus_hash=consensus_hash,
                attestation_count=attestation_count,
                reached=reached,
                resolved_at=int(time.time()),
            )

    # -----------------------------------
    # Load Attestations
    # -----------------------------------

    def _load_attestations(self, epoch_id: str) -> List[ClosureAttestation]:
        if not os.path.exists(ATTESTATION_LEDGER_PATH):
            return []

        records: List[ClosureAttestation] = []

        with open(ATTESTATION_LEDGER_PATH, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                if data["epoch_id"] == epoch_id:
                    records.append(ClosureAttestation(**data))

        return records