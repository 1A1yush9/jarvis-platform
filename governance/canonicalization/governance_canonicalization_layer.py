"""
Stage-170.0 — Civilizational Recursive Governance Canonicalization Layer (CRGCL)

Deterministic canonicalization advisory module providing:

• Recursive governance canonicalization validation
• Canonical coherence scoring
• Canonical variance detection
• Advisory governance signaling

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any
import hashlib
import json
import os
import time

from governance.canonicalization.canonicalization_model import CanonicalizationModel
from governance.telemetry.crgcl_telemetry import CRGCLTelemetryClient


# ============================================================
# Deterministic Utilities
# ============================================================

def _deterministic_hash(payload: Dict[str, Any]) -> str:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode()).hexdigest()


# ============================================================
# Data Structures
# ============================================================

@dataclass(frozen=True)
class CRGCLSignal:
    timestamp: float
    epoch_index: int
    canonical_vector: Dict[str, float]
    coherence_score: float
    variance_index: float
    canonical_state: str
    advisory_level: str
    hash: str


# ============================================================
# Canonicalization Layer
# ============================================================

class CivilizationalRecursiveGovernanceCanonicalizationLayer:

    def __init__(self):
        self._model = CanonicalizationModel()
        self._telemetry = CRGCLTelemetryClient()
        self._canonical_path = os.getenv("CRGCL_CANONICAL_PATH", "/tmp/crgcl_canonical.log")

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def canonicalize(self, attestation_signal: Dict[str, Any]) -> CRGCLSignal:
        """
        Deterministic recursive governance canonicalization synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = attestation_signal.get("epoch_index", 0)

        attestation_vector = attestation_signal.get("attestation_vector", {})

        canonical_vector = self._model.evaluate(attestation_vector)
        coherence_score = self._compute_coherence(canonical_vector)
        variance_index = self._compute_variance(canonical_vector)

        canonical_state = self._model.classify_state(
            coherence_score,
            variance_index
        )

        advisory_level = self._derive_advisory_level(
            coherence_score,
            variance_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "canonical_vector": canonical_vector,
            "coherence_score": coherence_score,
            "variance_index": variance_index,
            "canonical_state": canonical_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRGCLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            canonical_vector=canonical_vector,
            coherence_score=coherence_score,
            variance_index=variance_index,
            canonical_state=canonical_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._append_canonical(asdict(signal))
        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_coherence(self, vector: Dict[str, float]) -> float:
        if not vector:
            return 0.0
        return round(sum(vector.values()) / len(vector), 6)

    def _compute_variance(self, vector: Dict[str, float]) -> float:
        if not vector:
            return 0.0
        values = list(vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, coherence: float, variance: float) -> str:
        if coherence >= 0.998 and variance <= 0.006:
            return "CANONICAL_STABLE"
        if coherence >= 0.99 and variance <= 0.015:
            return "CANONICAL_MONITORED"
        return "CANONICAL_ATTENTION"

    # --------------------------------------------------------
    # Deterministic Canonical Append
    # --------------------------------------------------------

    def _append_canonical(self, payload: Dict[str, Any]) -> None:
        serialized = json.dumps(payload, sort_keys=True)
        with open(self._canonical_path, "a", encoding="utf-8") as f:
            f.write(serialized + "\n")