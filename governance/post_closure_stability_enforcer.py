# governance/post_closure_stability_enforcer.py
# Stage-172.0 — Civilizational Governance Post-Closure Stability Enforcement
# Deterministic • Append-Only • Replay-Safe • Render-Compatible

from __future__ import annotations

import json
import os
import threading
import time
from dataclasses import dataclass, asdict
from typing import Dict, Optional

from governance.immutable_ledger_closure import ImmutableLedgerClosure


LEDGER_PATH = "governance/ledger/governance_ledger.jsonl"
CLOSURE_PATH = "governance/ledger/governance_closures.jsonl"
ENFORCEMENT_LOG_PATH = "governance/ledger/post_closure_enforcement.jsonl"

_lock = threading.Lock()


@dataclass(frozen=True)
class EnforcementEvent:
    timestamp: int
    event_type: str
    epoch_id: str
    details: Dict


class PostClosureStabilityEnforcer:
    """
    Stage-172.0 Enforcement Engine

    Guarantees:

    • Closed epoch immutability enforcement
    • Deterministic violation rejection
    • Replay-safe state verification
    • Continuous stability monitoring
    """

    def __init__(self) -> None:
        self.closure_engine = ImmutableLedgerClosure()
        os.makedirs(os.path.dirname(ENFORCEMENT_LOG_PATH), exist_ok=True)

    # -----------------------------------
    # Active Closed Epoch Resolution
    # -----------------------------------

    def _latest_closed_epoch(self) -> Optional[str]:
        if not os.path.exists(CLOSURE_PATH):
            return None

        latest_epoch = None

        with open(CLOSURE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                data = json.loads(line)
                latest_epoch = data["epoch_id"]

        return latest_epoch

    # -----------------------------------
    # Ledger Mutation Guard
    # -----------------------------------

    def assert_write_allowed(self, target_epoch: str) -> bool:
        """
        Deterministic write gate:
        Reject writes to closed epoch.
        """
        with _lock:
            closed_epoch = self._latest_closed_epoch()

            if closed_epoch is None:
                return True

            if target_epoch <= closed_epoch:
                self._log_event(
                    "WRITE_REJECTED",
                    target_epoch,
                    {"reason": "epoch_closed", "closed_epoch": closed_epoch},
                )
                return False

            return True

    # -----------------------------------
    # Continuous Stability Verification
    # -----------------------------------

    def verify_post_closure_stability(self) -> Dict:
        with _lock:
            closed_epoch = self._latest_closed_epoch()

            if not closed_epoch:
                return {"status": "no_closed_epoch"}

            verified = self.closure_engine.verify_closure(closed_epoch)

            result = {
                "closed_epoch": closed_epoch,
                "closure_integrity_verified": verified,
                "timestamp": int(time.time()),
            }

            self._log_event("STABILITY_CHECK", closed_epoch, result)

            return result

    # -----------------------------------
    # Enforcement Event Logging (Append-Only)
    # -----------------------------------

    def _log_event(self, event_type: str, epoch_id: str, details: Dict) -> None:
        event = EnforcementEvent(
            timestamp=int(time.time()),
            event_type=event_type,
            epoch_id=epoch_id,
            details=details,
        )

        with open(ENFORCEMENT_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(event), sort_keys=True) + "\n")