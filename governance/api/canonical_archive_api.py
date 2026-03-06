# governance/api/canonical_archive_api.py
# Stage-176.0 — Advisory API Interface (Safe)

from __future__ import annotations

from governance.canonical_archive_entrenchment import CanonicalArchiveEntrenchment


engine = CanonicalArchiveEntrenchment()


def entrench_epoch_archive(epoch_id: str) -> dict:
    record = engine.entrench_epoch(epoch_id)

    if not record:
        return {"status": "canonical_not_found", "epoch_id": epoch_id}

    return {
        "epoch_id": record.epoch_id,
        "canonical_hash": record.canonical_hash,
        "canonicalization_hash": record.canonicalization_hash,
        "archive_hash": record.archive_hash,
        "entrenched_at": record.entrenched_at,
    }


def verify_epoch_archive(epoch_id: str) -> dict:
    verified = engine.verify_archive(epoch_id)
    return {
        "epoch_id": epoch_id,
        "verified": verified,
    }