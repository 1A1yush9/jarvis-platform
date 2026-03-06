# governance/api/closure_audit_sync_api.py
# Stage-173.0 — Advisory API Interface

from __future__ import annotations

from governance.closure_audit_synchronizer import ClosureAuditSynchronizer


synchronizer = ClosureAuditSynchronizer()


def reconcile_external_closure(external_hash: str) -> dict:
    return synchronizer.reconcile_with_external(external_hash)


def verify_recursive_integrity() -> dict:
    return synchronizer.verify_recursive_closure_integrity()