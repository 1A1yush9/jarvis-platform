"""
Stage-160.0 — Civilizational Epoch Transition Governance Layer (CETGL)

Deterministic transition-governance advisory module providing:

• Epoch-boundary readiness evaluation
• Transitional instability detection
• Deterministic transition scoring
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

from governance.transition.epoch_transition_model import EpochTransitionModel
from governance.telemetry.cetgl_telemetry import CETGLTelemetryClient


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
class CETGLSignal:
    timestamp: float
    epoch_index: int
    transition_vector: Dict[str, float]
    readiness_score: float
    instability_index: float
    transition_state: str
    advisory_level: str
    hash: str


# ============================================================
# Governance Layer
# ============================================================

class CivilizationalEpochTransitionGovernanceLayer:

    def __init__(self):
        self._model = EpochTransitionModel()
        self._telemetry = CETGLTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def evaluate_transition(self, observational_signal: Dict[str, Any]) -> CETGLSignal:
        """
        Deterministic epoch transition governance synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = observational_signal.get("epoch_index", 0)

        observation_vector = observational_signal.get("observation_vector", {})

        transition_vector = self._model.evaluate(observation_vector)
        readiness_score = self._compute_readiness(transition_vector)
        instability_index = self._compute_instability(transition_vector)

        transition_state = self._model.classify_state(
            readiness_score,
            instability_index
        )

        advisory_level = self._derive_advisory_level(
            readiness_score,
            instability_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "transition_vector": transition_vector,
            "readiness_score": readiness_score,
            "instability_index": instability_index,
            "transition_state": transition_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CETGLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            transition_vector=transition_vector,
            readiness_score=readiness_score,
            instability_index=instability_index,
            transition_state=transition_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_readiness(self, transition_vector: Dict[str, float]) -> float:
        if not transition_vector:
            return 0.0
        return round(sum(transition_vector.values()) / len(transition_vector), 6)

    def _compute_instability(self, transition_vector: Dict[str, float]) -> float:
        if not transition_vector:
            return 0.0
        values = list(transition_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, readiness: float, instability: float) -> str:
        if readiness >= 0.93 and instability <= 0.05:
            return "STABLE"
        if readiness >= 0.82 and instability <= 0.12:
            return "MONITOR"
        return "ATTENTION"