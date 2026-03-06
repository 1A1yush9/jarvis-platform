# governance/api/ledger_closure_api.py
# Stage-171.0 — Closure API (Advisory-Only Safe Interface)

from __future__ import annotations

from governance.immutable_ledger_closure import ImmutableLedgerClosure


closure_engine = ImmutableLedgerClosure()


def execute_epoch_closure(epoch_id: str) -> dict:
    record = closure_engine.close_epoch(epoch_id)
    return {
        "status": "closed",
        "epoch_id": record.epoch_id,
        "ledger_hash": record.ledger_hash,
        "entry_count": record.entry_count,
        "closure_timestamp": record.closure_timestamp,
        "closure_hash": record.closure_hash,
    }


def verify_epoch_closure(epoch_id: str) -> dict:
    verified = closure_engine.verify_closure(epoch_id)
    return {
        "epoch_id": epoch_id,
        "verified": verified,
    }