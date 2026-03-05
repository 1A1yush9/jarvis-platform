"""
Stage-159.0 — Civilizational Post-Closure Observational Layer (CPCOL)

Deterministic observational advisory module providing:

• Post-closure governance monitoring
• Persistence integrity validation
• Latent instability resurgence detection
• Advisory observational signaling

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any
import hashlib
import json
import time

from governance.observation.post_closure_model import PostClosureModel
from governance.telemetry.cpcol_telemetry import CPCOLTelemetryClient


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
class CPCOLSignal:
    timestamp: float
    epoch_index: int
    observation_vector: Dict[str, float]
    persistence_score: float
    resurgence_index: float
    observation_state: str
    advisory_level: str
    hash: str


# ============================================================
# Observational Layer
# ============================================================

class CivilizationalPostClosureObservationalLayer:

    def __init__(self):
        self._model = PostClosureModel()
        self._telemetry = CPCOLTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def observe(self, closure_signal: Dict[str, Any]) -> CPCOLSignal:
        """
        Deterministic post-closure observational synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = closure_signal.get("epoch_index", 0)

        closure_vector = closure_signal.get("closure_vector", {})

        observation_vector = self._model.observe(closure_vector)
        persistence_score = self._compute_persistence(observation_vector)
        resurgence_index = self._compute_resurgence(observation_vector)

        observation_state = self._model.classify_state(
            persistence_score,
            resurgence_index
        )

        advisory_level = self._derive_advisory_level(
            persistence_score,
            resurgence_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "observation_vector": observation_vector,
            "persistence_score": persistence_score,
            "resurgence_index": resurgence_index,
            "observation_state": observation_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CPCOLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            observation_vector=observation_vector,
            persistence_score=persistence_score,
            resurgence_index=resurgence_index,
            observation_state=observation_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_persistence(self, observation_vector: Dict[str, float]) -> float:
        if not observation_vector:
            return 0.0
        return round(sum(observation_vector.values()) / len(observation_vector), 6)

    def _compute_resurgence(self, observation_vector: Dict[str, float]) -> float:
        if not observation_vector:
            return 0.0
        values = list(observation_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, persistence: float, resurgence: float) -> str:
        if persistence >= 0.94 and resurgence <= 0.04:
            return "STABLE"
        if persistence >= 0.85 and resurgence <= 0.1:
            return "MONITOR"
        return "ATTENTION"