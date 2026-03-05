"""
Stage-158.0 — Civilizational Closure Assurance & Legacy Preservation Layer (CCALPL)

Deterministic closure advisory module providing:

• Terminal governance closure verification
• Legacy preservation synthesis
• Closure degradation detection
• Advisory closure signaling

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any
import hashlib
import json
import time

from governance.closure.closure_integrity_model import ClosureIntegrityModel
from governance.telemetry.ccalpl_telemetry import CCALPLTelemetryClient


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
class CCALPLSignal:
    timestamp: float
    epoch_index: int
    closure_vector: Dict[str, float]
    legacy_score: float
    degradation_index: float
    closure_state: str
    advisory_level: str
    hash: str


# ============================================================
# Closure Layer
# ============================================================

class CivilizationalClosureAssuranceLegacyLayer:

    def __init__(self):
        self._model = ClosureIntegrityModel()
        self._telemetry = CCALPLTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def close(self, terminal_signal: Dict[str, Any]) -> CCALPLSignal:
        """
        Deterministic closure assurance synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = terminal_signal.get("epoch_index", 0)

        terminal_vector = terminal_signal.get("terminal_vector", {})

        closure_vector = self._model.evaluate(terminal_vector)
        legacy_score = self._compute_legacy_score(closure_vector)
        degradation_index = self._compute_degradation(closure_vector)

        closure_state = self._model.classify_state(
            legacy_score,
            degradation_index
        )

        advisory_level = self._derive_advisory_level(
            legacy_score,
            degradation_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "closure_vector": closure_vector,
            "legacy_score": legacy_score,
            "degradation_index": degradation_index,
            "closure_state": closure_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CCALPLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            closure_vector=closure_vector,
            legacy_score=legacy_score,
            degradation_index=degradation_index,
            closure_state=closure_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_legacy_score(self, closure_vector: Dict[str, float]) -> float:
        if not closure_vector:
            return 0.0
        return round(sum(closure_vector.values()) / len(closure_vector), 6)

    def _compute_degradation(self, closure_vector: Dict[str, float]) -> float:
        if not closure_vector:
            return 0.0
        values = list(closure_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, legacy: float, degradation: float) -> str:
        if legacy >= 0.93 and degradation <= 0.04:
            return "STABLE"
        if legacy >= 0.82 and degradation <= 0.1:
            return "MONITOR"
        return "ATTENTION"