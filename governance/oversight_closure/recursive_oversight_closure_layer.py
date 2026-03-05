"""
Stage-163.0 — Civilizational Recursive Oversight Closure Layer (CROCL)

Deterministic oversight-closure advisory module providing:

• Recursive oversight closure validation
• Cross-layer closure coherence scoring
• Closure drift detection
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

from governance.oversight_closure.recursive_closure_model import RecursiveClosureModel
from governance.telemetry.crocl_telemetry import CROCLTelemetryClient


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
class CROCLSignal:
    timestamp: float
    epoch_index: int
    closure_vector: Dict[str, float]
    coherence_score: float
    drift_index: float
    closure_state: str
    advisory_level: str
    hash: str


# ============================================================
# Closure Layer
# ============================================================

class CivilizationalRecursiveOversightClosureLayer:

    def __init__(self):
        self._model = RecursiveClosureModel()
        self._telemetry = CROCLTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def finalize(self, kernel_signal: Dict[str, Any]) -> CROCLSignal:
        """
        Deterministic recursive oversight closure synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = kernel_signal.get("epoch_index", 0)

        kernel_vector = kernel_signal.get("kernel_vector", {})

        closure_vector = self._model.evaluate(kernel_vector)
        coherence_score = self._compute_coherence(closure_vector)
        drift_index = self._compute_drift(closure_vector)

        closure_state = self._model.classify_state(
            coherence_score,
            drift_index
        )

        advisory_level = self._derive_advisory_level(
            coherence_score,
            drift_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "closure_vector": closure_vector,
            "coherence_score": coherence_score,
            "drift_index": drift_index,
            "closure_state": closure_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CROCLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            closure_vector=closure_vector,
            coherence_score=coherence_score,
            drift_index=drift_index,
            closure_state=closure_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_coherence(self, closure_vector: Dict[str, float]) -> float:
        if not closure_vector:
            return 0.0
        return round(sum(closure_vector.values()) / len(closure_vector), 6)

    def _compute_drift(self, closure_vector: Dict[str, float]) -> float:
        if not closure_vector:
            return 0.0
        values = list(closure_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, coherence: float, drift: float) -> str:
        if coherence >= 0.96 and drift <= 0.04:
            return "STABLE"
        if coherence >= 0.88 and drift <= 0.1:
            return "MONITOR"
        return "ATTENTION"