# governance/api/immutable_continuity_api.py
# Stage-177.0 — Advisory API Interface (Safe)

from __future__ import annotations

from governance.immutable_continuity_assurance import ImmutableContinuityAssurance


engine = ImmutableContinuityAssurance()


def run_continuity_assurance() -> dict:
    results = engine.verify_continuity()

    return {
        "records_generated": len(results),
        "epochs_verified": [r.epoch_id for r in results],
    }


def verify_epoch_continuity(epoch_id: str) -> dict:
    verified = engine.verify_replay(epoch_id)
    return {
        "epoch_id": epoch_id,
        "verified": verified,
    }