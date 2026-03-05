"""
Stage-161.0 — Civilizational Recursive Epoch Reinitialization Layer (CRERL)

Deterministic reinitialization-governance advisory module providing:

• Recursive epoch reset viability evaluation
• Reset instability detection
• Deterministic reinitialization scoring
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

from governance.reinitialization.recursive_epoch_model import RecursiveEpochModel
from governance.telemetry.crerl_telemetry import CRERLTelemetryClient


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
class CRERLSignal:
    timestamp: float
    epoch_index: int
    reinit_vector: Dict[str, float]
    readiness_score: float
    instability_index: float
    reinit_state: str
    advisory_level: str
    hash: str


# ============================================================
# Governance Layer
# ============================================================

class CivilizationalRecursiveEpochReinitializationLayer:

    def __init__(self):
        self._model = RecursiveEpochModel()
        self._telemetry = CRERLTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def evaluate_reinitialization(self, transition_signal: Dict[str, Any]) -> CRERLSignal:
        """
        Deterministic recursive epoch reinitialization governance synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = transition_signal.get("epoch_index", 0)

        transition_vector = transition_signal.get("transition_vector", {})

        reinit_vector = self._model.evaluate(transition_vector)
        readiness_score = self._compute_readiness(reinit_vector)
        instability_index = self._compute_instability(reinit_vector)

        reinit_state = self._model.classify_state(
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
            "reinit_vector": reinit_vector,
            "readiness_score": readiness_score,
            "instability_index": instability_index,
            "reinit_state": reinit_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRERLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            reinit_vector=reinit_vector,
            readiness_score=readiness_score,
            instability_index=instability_index,
            reinit_state=reinit_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_readiness(self, reinit_vector: Dict[str, float]) -> float:
        if not reinit_vector:
            return 0.0
        return round(sum(reinit_vector.values()) / len(reinit_vector), 6)

    def _compute_instability(self, reinit_vector: Dict[str, float]) -> float:
        if not reinit_vector:
            return 0.0
        values = list(reinit_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, readiness: float, instability: float) -> str:
        if readiness >= 0.94 and instability <= 0.05:
            return "STABLE"
        if readiness >= 0.85 and instability <= 0.12:
            return "MONITOR"
        return "ATTENTION"