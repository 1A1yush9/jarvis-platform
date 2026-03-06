# governance/api/closure_consensus_api.py
# Stage-174.0 — Advisory API Interface (Safe)

from __future__ import annotations

from governance.closure_consensus_attestation import ClosureConsensusAttestation


engine = ClosureConsensusAttestation()


def submit_attestation(epoch_id: str, node_id: str, closure_hash: str) -> dict:
    record = engine.append_attestation(epoch_id, node_id, closure_hash)
    return {
        "epoch_id": record.epoch_id,
        "node_id": record.node_id,
        "closure_hash": record.closure_hash,
        "attested_at": record.attested_at,
        "attestation_hash": record.attestation_hash,
    }


def resolve_epoch_consensus(epoch_id: str, threshold: int) -> dict:
    result = engine.resolve_consensus(epoch_id, threshold)
    return {
        "epoch_id": result.epoch_id,
        "consensus_hash": result.consensus_hash,
        "attestation_count": result.attestation_count,
        "reached": result.reached,
        "resolved_at": result.resolved_at,
    }