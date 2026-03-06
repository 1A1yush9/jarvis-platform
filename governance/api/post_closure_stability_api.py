# governance/api/post_closure_stability_api.py
# Stage-172.0 — Advisory API (Safe Interface)

from __future__ import annotations

from governance.post_closure_stability_enforcer import PostClosureStabilityEnforcer


enforcer = PostClosureStabilityEnforcer()


def enforce_write_guard(epoch_id: str) -> dict:
    allowed = enforcer.assert_write_allowed(epoch_id)
    return {
        "epoch_id": epoch_id,
        "write_allowed": allowed,
    }


def run_stability_check() -> dict:
    return enforcer.verify_post_closure_stability()