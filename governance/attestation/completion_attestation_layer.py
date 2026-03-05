"""
Stage-169.0 — Civilizational Recursive Governance Completion Attestation Layer (CRGCAL)

Deterministic attestation advisory module providing:

• Recursive governance completion attestation validation
• Attestation coherence scoring
• Residual variance detection
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

from governance.attestation.attestation_model import AttestationModel
from governance.telemetry.crgcal_telemetry import CRGCALTelemetryClient


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
class CRGCALSignal:
    timestamp: float
    epoch_index: int
    attestation_vector: Dict[str, float]
    coherence_score: float
    variance_index: float
    attestation_state: str
    advisory_level: str
    hash: str


# ============================================================
# Attestation Layer
# ============================================================

class CivilizationalRecursiveGovernanceCompletionAttestationLayer:

    def __init__(self):
        self._model = AttestationModel()
        self._telemetry = CRGCALTelemetryClient()
        self._attestation_path = os.getenv("CRGCAL_ATTEST_PATH", "/tmp/crgcal_attest.log")

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def attest(self, finalization_signal: Dict[str, Any]) -> CRGCALSignal:
        """
        Deterministic recursive governance completion attestation synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = finalization_signal.get("epoch_index", 0)

        finalization_vector = finalization_signal.get("finalization_vector", {})

        attestation_vector = self._model.evaluate(finalization_vector)
        coherence_score = self._compute_coherence(attestation_vector)
        variance_index = self._compute_variance(attestation_vector)

        attestation_state = self._model.classify_state(
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
            "attestation_vector": attestation_vector,
            "coherence_score": coherence_score,
            "variance_index": variance_index,
            "attestation_state": attestation_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRGCALSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            attestation_vector=attestation_vector,
            coherence_score=coherence_score,
            variance_index=variance_index,
            attestation_state=attestation_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._append_attestation(asdict(signal))
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
        if coherence >= 0.997 and variance <= 0.008:
            return "ATTESTED_STABLE"
        if coherence >= 0.985 and variance <= 0.02:
            return "ATTESTED_MONITORED"
        return "ATTESTED_ATTENTION"

    # --------------------------------------------------------
    # Deterministic Attestation Append
    # --------------------------------------------------------

    def _append_attestation(self, payload: Dict[str, Any]) -> None:
        serialized = json.dumps(payload, sort_keys=True)
        with open(self._attestation_path, "a", encoding="utf-8") as f:
            f.write(serialized + "\n")