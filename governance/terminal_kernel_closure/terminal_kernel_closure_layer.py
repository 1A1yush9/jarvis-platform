"""
Stage-164.0 — Civilizational Recursive Governance Terminal Kernel Closure (CRGTKC)

Deterministic terminal kernel closure advisory module providing:

• Recursive governance kernel lifecycle closure validation
• Terminal kernel coherence scoring
• Terminal kernel drift detection
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

from governance.terminal_kernel_closure.terminal_kernel_model import TerminalKernelModel
from governance.telemetry.crgtkc_telemetry import CRGTKCTelemetryClient


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
class CRGTKCSignal:
    timestamp: float
    epoch_index: int
    terminal_kernel_vector: Dict[str, float]
    coherence_score: float
    drift_index: float
    terminal_state: str
    advisory_level: str
    hash: str


# ============================================================
# Closure Layer
# ============================================================

class CivilizationalRecursiveGovernanceTerminalKernelClosureLayer:

    def __init__(self):
        self._model = TerminalKernelModel()
        self._telemetry = CRGTKCTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def finalize_kernel(self, closure_signal: Dict[str, Any]) -> CRGTKCSignal:
        """
        Deterministic terminal kernel closure synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = closure_signal.get("epoch_index", 0)

        closure_vector = closure_signal.get("closure_vector", {})

        terminal_kernel_vector = self._model.evaluate(closure_vector)
        coherence_score = self._compute_coherence(terminal_kernel_vector)
        drift_index = self._compute_drift(terminal_kernel_vector)

        terminal_state = self._model.classify_state(
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
            "terminal_kernel_vector": terminal_kernel_vector,
            "coherence_score": coherence_score,
            "drift_index": drift_index,
            "terminal_state": terminal_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRGTKCSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            terminal_kernel_vector=terminal_kernel_vector,
            coherence_score=coherence_score,
            drift_index=drift_index,
            terminal_state=terminal_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_coherence(self, vector: Dict[str, float]) -> float:
        if not vector:
            return 0.0
        return round(sum(vector.values()) / len(vector), 6)

    def _compute_drift(self, vector: Dict[str, float]) -> float:
        if not vector:
            return 0.0
        values = list(vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, coherence: float, drift: float) -> str:
        if coherence >= 0.97 and drift <= 0.03:
            return "STABLE"
        if coherence >= 0.9 and drift <= 0.08:
            return "MONITOR"
        return "ATTENTION"