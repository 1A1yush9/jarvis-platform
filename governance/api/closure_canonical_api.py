# governance/api/closure_canonical_api.py
# Stage-175.0 — Advisory API Interface (Safe)

from __future__ import annotations

from governance.closure_canonicalizer import ClosureCanonicalizer


engine = ClosureCanonicalizer()


def finalize_epoch_closure(epoch_id: str, consensus_hash: str, attestation_count: int) -> dict:
    record = engine.finalize_canonical_closure(epoch_id, consensus_hash, attestation_count)
    return {
        "epoch_id": record.epoch_id,
        "canonical_hash": record.canonical_hash,
        "attestation_count": record.attestation_count,
        "finalized_at": record.finalized_at,
        "canonicalization_hash": record.canonicalization_hash,
    }


def verify_epoch_canonical(epoch_id: str) -> dict:
    verified = engine.verify_canonical_closure(epoch_id)
    return {
        "epoch_id": epoch_id,
        "verified": verified,
    }