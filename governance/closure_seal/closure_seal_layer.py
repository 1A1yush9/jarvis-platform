"""
Stage-165.0 — Civilizational Recursive Governance Closure Seal Layer (CRGCSL)

Deterministic closure-seal advisory module providing:

• Recursive governance closure sealing validation
• Closure immutability coherence scoring
• Post-seal drift detection
• Advisory governance signaling

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any
import hashlib
import json
import time

from governance.closure_seal.closure_seal_model import ClosureSealModel
from governance.telemetry.crgcsl_telemetry import CRGCSLTelemetryClient


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
class CRGCSLSignal:
    timestamp: float
    epoch_index: int
    seal_vector: Dict[str, float]
    immutability_score: float
    post_seal_drift_index: float
    seal_state: str
    advisory_level: str
    hash: str


# ============================================================
# Seal Layer
# ============================================================

class CivilizationalRecursiveGovernanceClosureSealLayer:

    def __init__(self):
        self._model = ClosureSealModel()
        self._telemetry = CRGCSLTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def seal(self, terminal_kernel_signal: Dict[str, Any]) -> CRGCSLSignal:
        """
        Deterministic recursive governance closure seal synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = terminal_kernel_signal.get("epoch_index", 0)

        terminal_kernel_vector = terminal_kernel_signal.get("terminal_kernel_vector", {})

        seal_vector = self._model.evaluate(terminal_kernel_vector)
        immutability_score = self._compute_immutability(seal_vector)
        post_seal_drift_index = self._compute_drift(seal_vector)

        seal_state = self._model.classify_state(
            immutability_score,
            post_seal_drift_index
        )

        advisory_level = self._derive_advisory_level(
            immutability_score,
            post_seal_drift_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "seal_vector": seal_vector,
            "immutability_score": immutability_score,
            "post_seal_drift_index": post_seal_drift_index,
            "seal_state": seal_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRGCSLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            seal_vector=seal_vector,
            immutability_score=immutability_score,
            post_seal_drift_index=post_seal_drift_index,
            seal_state=seal_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_immutability(self, seal_vector: Dict[str, float]) -> float:
        if not seal_vector:
            return 0.0
        return round(sum(seal_vector.values()) / len(seal_vector), 6)

    def _compute_drift(self, seal_vector: Dict[str, float]) -> float:
        if not seal_vector:
            return 0.0
        values = list(seal_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, immutability: float, drift: float) -> str:
        if immutability >= 0.98 and drift <= 0.02:
            return "SEALED_STABLE"
        if immutability >= 0.92 and drift <= 0.06:
            return "SEALED_MONITORED"
        return "SEALED_ATTENTION"