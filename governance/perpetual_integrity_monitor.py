# governance/perpetual_integrity_monitor.py
# Stage-178.0 — Civilizational Governance Perpetual Integrity Monitoring Layer
# Deterministic • Append-Only • Replay-Safe • Render-Compatible

from __future__ import annotations

import json
import os
import threading
import time
from dataclasses import dataclass, asdict
from typing import Dict, List

from governance.immutable_ledger_closure import ImmutableLedgerClosure
from governance.closure_canonicalizer import ClosureCanonicalizer
from governance.canonical_archive_entrenchment import CanonicalArchiveEntrenchment
from governance.immutable_continuity_assurance import ImmutableContinuityAssurance


INTEGRITY_LEDGER_PATH = "governance/ledger/perpetual_integrity_ledger.jsonl"

_lock = threading.Lock()


@dataclass(frozen=True)
class IntegrityEvent:
    timestamp: int
    component: str
    epoch_id: str
    verified: bool
    details: Dict


class PerpetualIntegrityMonitor:
    """
    Stage-178.0 Integrity Engine

    Guarantees:

    • Continuous multi-layer deterministic verification
    • Cross-ledger replay alignment
    • Append-only integrity telemetry
    """

    def __init__(self) -> None:
        os.makedirs(os.path.dirname(INTEGRITY_LEDGER_PATH), exist_ok=True)
        self.closure_engine = ImmutableLedgerClosure()
        self.canonical_engine = ClosureCanonicalizer()
        self.archive_engine = CanonicalArchiveEntrenchment()
        self.continuity_engine = ImmutableContinuityAssurance()

    # -----------------------------------
    # Resolve All Epochs
    # -----------------------------------

    def _resolve_epochs(self) -> List[str]:
        path = "governance/ledger/closure_canonical_registry.jsonl"
        if not os.path.exists(path):
            return []

        epochs = []

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                epochs.append(data["epoch_id"])

        return epochs

    # -----------------------------------
    # Continuous Integrity Verification
    # -----------------------------------

    def run_integrity_cycle(self) -> Dict:
        with _lock:
            epochs = self._resolve_epochs()
            results = []

            for epoch_id in epochs:
                closure_ok = self.closure_engine.verify_closure(epoch_id)
                canonical_ok = self.canonical_engine.verify_canonical_closure(epoch_id)
                archive_ok = self.archive_engine.verify_archive(epoch_id)
                continuity_ok = self.continuity_engine.verify_replay(epoch_id)

                overall = all([closure_ok, canonical_ok, archive_ok, continuity_ok])

                event = IntegrityEvent(
                    timestamp=int(time.time()),
                    component="perpetual_integrity",
                    epoch_id=epoch_id,
                    verified=overall,
                    details={
                        "closure": closure_ok,
                        "canonical": canonical_ok,
                        "archive": archive_ok,
                        "continuity": continuity_ok,
                    },
                )

                self._append_event(event)
                results.append(asdict(event))

            return {
                "epochs_checked": len(results),
                "results": results,
            }

    # -----------------------------------
    # Append-Only Event Logging
    # -----------------------------------

    def _append_event(self, event: IntegrityEvent) -> None:
        with open(INTEGRITY_LEDGER_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(event), sort_keys=True) + "\n")