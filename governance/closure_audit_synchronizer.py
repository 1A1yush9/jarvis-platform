# governance/closure_audit_synchronizer.py
# Stage-173.0 — Civilizational Recursive Governance Closure Audit Synchronization
# Deterministic • Append-Only • Replay-Safe • Render-Compatible

from __future__ import annotations

import hashlib
import json
import os
import threading
import time
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

from governance.immutable_ledger_closure import ImmutableLedgerClosure


CLOSURE_PATH = "governance/ledger/governance_closures.jsonl"
SYNC_LOG_PATH = "governance/ledger/closure_sync_audit.jsonl"

_lock = threading.Lock()


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass(frozen=True)
class ClosureSyncEvent:
    timestamp: int
    event_type: str
    epoch_id: str
    local_hash: str
    external_hash: Optional[str]
    reconciled: bool


class ClosureAuditSynchronizer:
    """
    Stage-173.0 Synchronization Engine

    Guarantees:

    • Deterministic closure audit alignment
    • Cross-node reconciliation support
    • Replay-consistent validation
    • Append-only audit telemetry
    """

    def __init__(self) -> None:
        self.closure_engine = ImmutableLedgerClosure()
        os.makedirs(os.path.dirname(SYNC_LOG_PATH), exist_ok=True)

    # ---------------------------------------
    # Resolve Latest Closure Record
    # ---------------------------------------

    def _latest_closure(self) -> Optional[Dict]:
        if not os.path.exists(CLOSURE_PATH):
            return None

        latest = None

        with open(CLOSURE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                latest = json.loads(line)

        return latest

    # ---------------------------------------
    # Deterministic Local Closure Hash
    # ---------------------------------------

    def compute_local_closure_hash(self) -> Optional[str]:
        latest = self._latest_closure()
        if not latest:
            return None

        canonical_blob = json.dumps(latest, sort_keys=True).encode("utf-8")
        return _sha256(canonical_blob)

    # ---------------------------------------
    # External Alignment Check
    # ---------------------------------------

    def reconcile_with_external(self, external_hash: str) -> Dict:
        with _lock:
            latest = self._latest_closure()

            if not latest:
                return {"status": "no_local_closure"}

            epoch_id = latest["epoch_id"]
            local_hash = self.compute_local_closure_hash()

            reconciled = local_hash == external_hash

            self._log_event(
                ClosureSyncEvent(
                    timestamp=int(time.time()),
                    event_type="RECONCILE",
                    epoch_id=epoch_id,
                    local_hash=local_hash or "",
                    external_hash=external_hash,
                    reconciled=reconciled,
                )
            )

            return {
                "epoch_id": epoch_id,
                "local_hash": local_hash,
                "external_hash": external_hash,
                "reconciled": reconciled,
            }

    # ---------------------------------------
    # Continuous Replay Validation
    # ---------------------------------------

    def verify_recursive_closure_integrity(self) -> Dict:
        with _lock:
            latest = self._latest_closure()

            if not latest:
                return {"status": "no_closure"}

            epoch_id = latest["epoch_id"]
            verified = self.closure_engine.verify_closure(epoch_id)

            self._log_event(
                ClosureSyncEvent(
                    timestamp=int(time.time()),
                    event_type="RECURSIVE_VERIFY",
                    epoch_id=epoch_id,
                    local_hash=self.compute_local_closure_hash() or "",
                    external_hash=None,
                    reconciled=verified,
                )
            )

            return {
                "epoch_id": epoch_id,
                "recursive_verified": verified,
            }

    # ---------------------------------------
    # Append-Only Logging
    # ---------------------------------------

    def _log_event(self, event: ClosureSyncEvent) -> None:
        with open(SYNC_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(event), sort_keys=True) + "\n")