"""
Stage-162.0 — Civilizational Recursive Governance Continuity Kernel (CRGCK)

Deterministic kernel advisory module providing:

• Recursive governance continuity invariant enforcement
• Structural continuity coherence validation
• Deterministic kernel scoring
• Advisory kernel signaling

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any
import hashlib
import json
import time

from governance.kernel.continuity_kernel_model import ContinuityKernelModel
from governance.telemetry.crgck_telemetry import CRGCKTelemetryClient


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
class CRGCKSignal:
    timestamp: float
    epoch_index: int
    kernel_vector: Dict[str, float]
    continuity_score: float
    invariant_drift_index: float
    kernel_state: str
    advisory_level: str
    hash: str


# ============================================================
# Kernel Layer
# ============================================================

class CivilizationalRecursiveGovernanceContinuityKernel:

    def __init__(self):
        self._model = ContinuityKernelModel()
        self._telemetry = CRGCKTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def enforce(self, reinit_signal: Dict[str, Any]) -> CRGCKSignal:
        """
        Deterministic recursive governance continuity kernel synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = reinit_signal.get("epoch_index", 0)

        reinit_vector = reinit_signal.get("reinit_vector", {})

        kernel_vector = self._model.evaluate(reinit_vector)
        continuity_score = self._compute_continuity(kernel_vector)
        invariant_drift_index = self._compute_drift(kernel_vector)

        kernel_state = self._model.classify_state(
            continuity_score,
            invariant_drift_index
        )

        advisory_level = self._derive_advisory_level(
            continuity_score,
            invariant_drift_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "kernel_vector": kernel_vector,
            "continuity_score": continuity_score,
            "invariant_drift_index": invariant_drift_index,
            "kernel_state": kernel_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRGCKSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            kernel_vector=kernel_vector,
            continuity_score=continuity_score,
            invariant_drift_index=invariant_drift_index,
            kernel_state=kernel_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_continuity(self, kernel_vector: Dict[str, float]) -> float:
        if not kernel_vector:
            return 0.0
        return round(sum(kernel_vector.values()) / len(kernel_vector), 6)

    def _compute_drift(self, kernel_vector: Dict[str, float]) -> float:
        if not kernel_vector:
            return 0.0
        values = list(kernel_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, continuity: float, drift: float) -> str:
        if continuity >= 0.95 and drift <= 0.04:
            return "STABLE"
        if continuity >= 0.86 and drift <= 0.1:
            return "MONITOR"
        return "ATTENTION"