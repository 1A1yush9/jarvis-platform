"""
Stage-151.0 — Governance Post-Civilizational Stability Oversight Layer (PCSOL)

Deterministic oversight module providing:

• Cross-epoch governance coherence verification
• Civilizational stability envelope validation
• Recursive drift detection
• Advisory foresight synthesis

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any, List
import hashlib
import json
import time

from governance.oversight.civilizational_envelope_model import CivilizationalEnvelopeModel
from governance.telemetry.pcsol_telemetry import PCSOTelemetryClient


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
class PCSOLSignal:
    timestamp: float
    epoch_index: int
    coherence_score: float
    drift_score: float
    envelope_status: str
    advisory_level: str
    hash: str


# ============================================================
# Oversight Layer
# ============================================================

class PostCivilizationalStabilityLayer:

    def __init__(self):
        self._envelope_model = CivilizationalEnvelopeModel()
        self._telemetry = PCSOTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def evaluate(self, governance_state: Dict[str, Any]) -> PCSOLSignal:
        """
        Deterministic civilizational oversight evaluation.
        """

        timestamp = round(time.time(), 3)
        epoch_index = governance_state.get("epoch_index", 0)

        coherence_score = self._compute_coherence(governance_state)
        drift_score = self._compute_drift(governance_state)

        envelope_status = self._envelope_model.evaluate(
            coherence_score=coherence_score,
            drift_score=drift_score
        )

        advisory_level = self._derive_advisory_level(coherence_score, drift_score)

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "coherence_score": coherence_score,
            "drift_score": drift_score,
            "envelope_status": envelope_status,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = PCSOLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            coherence_score=coherence_score,
            drift_score=drift_score,
            envelope_status=envelope_status,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Scoring
    # --------------------------------------------------------

    def _compute_coherence(self, governance_state: Dict[str, Any]) -> float:
        base = governance_state.get("coherence_index", 0.95)
        stability = governance_state.get("stability_index", 0.95)
        foresight = governance_state.get("foresight_index", 0.95)

        return round((base + stability + foresight) / 3.0, 6)

    def _compute_drift(self, governance_state: Dict[str, Any]) -> float:
        recursion_entropy = governance_state.get("recursion_entropy", 0.02)
        signal_variance = governance_state.get("signal_variance", 0.02)

        return round((recursion_entropy + signal_variance) / 2.0, 6)

    def _derive_advisory_level(self, coherence: float, drift: float) -> str:
        if coherence >= 0.97 and drift <= 0.02:
            return "STABLE"
        if coherence >= 0.94 and drift <= 0.04:
            return "MONITOR"
        return "ATTENTION"