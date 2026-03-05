"""
Stage-156.0 — Civilizational Recursive Continuity Assurance Layer (CRCAL)

Deterministic assurance advisory module providing:

• Recursive continuity verification
• Structural discontinuity detection
• Deterministic assurance scoring
• Advisory assurance signaling

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any
import hashlib
import json
import time

from governance.assurance.continuity_assurance_model import ContinuityAssuranceModel
from governance.telemetry.crcal_telemetry import CRCALTelemetryClient


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
class CRCALSignal:
    timestamp: float
    epoch_index: int
    assurance_vector: Dict[str, float]
    continuity_score: float
    discontinuity_index: float
    assurance_state: str
    advisory_level: str
    hash: str


# ============================================================
# Assurance Layer
# ============================================================

class CivilizationalRecursiveContinuityAssuranceLayer:

    def __init__(self):
        self._model = ContinuityAssuranceModel()
        self._telemetry = CRCALTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def assure(self, convergence_signal: Dict[str, Any]) -> CRCALSignal:
        """
        Deterministic recursive continuity assurance synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = convergence_signal.get("epoch_index", 0)

        convergence_vector = convergence_signal.get("convergence_vector", {})

        assurance_vector = self._model.assure(convergence_vector)
        continuity_score = self._compute_continuity(assurance_vector)
        discontinuity_index = self._compute_discontinuity(assurance_vector)

        assurance_state = self._model.classify_state(
            continuity_score,
            discontinuity_index
        )

        advisory_level = self._derive_advisory_level(
            continuity_score,
            discontinuity_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "assurance_vector": assurance_vector,
            "continuity_score": continuity_score,
            "discontinuity_index": discontinuity_index,
            "assurance_state": assurance_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRCALSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            assurance_vector=assurance_vector,
            continuity_score=continuity_score,
            discontinuity_index=discontinuity_index,
            assurance_state=assurance_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_continuity(self, assurance_vector: Dict[str, float]) -> float:
        if not assurance_vector:
            return 0.0
        return round(sum(assurance_vector.values()) / len(assurance_vector), 6)

    def _compute_discontinuity(self, assurance_vector: Dict[str, float]) -> float:
        if not assurance_vector:
            return 0.0
        values = list(assurance_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, continuity: float, discontinuity: float) -> str:
        if continuity >= 0.9 and discontinuity <= 0.06:
            return "STABLE"
        if continuity >= 0.78 and discontinuity <= 0.14:
            return "MONITOR"
        return "ATTENTION"