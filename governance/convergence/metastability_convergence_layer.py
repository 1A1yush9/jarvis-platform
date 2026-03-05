"""
Stage-155.0 — Civilizational Meta-Stability Convergence Layer (CMSCL)

Deterministic convergence advisory module providing:

• Cross-layer meta-stability synthesis
• Systemic divergence detection
• Deterministic convergence scoring
• Advisory convergence signaling

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any
import hashlib
import json
import time

from governance.convergence.metastability_model import MetaStabilityModel
from governance.telemetry.cmscl_telemetry import CMSCLTelemetryClient


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
class CMSCLSignal:
    timestamp: float
    epoch_index: int
    convergence_vector: Dict[str, float]
    metastability_score: float
    divergence_index: float
    convergence_state: str
    advisory_level: str
    hash: str


# ============================================================
# Convergence Layer
# ============================================================

class CivilizationalMetaStabilityConvergenceLayer:

    def __init__(self):
        self._model = MetaStabilityModel()
        self._telemetry = CMSCLTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def converge(self, coordination_signal: Dict[str, Any]) -> CMSCLSignal:
        """
        Deterministic meta-stability convergence synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = coordination_signal.get("epoch_index", 0)

        alignment_vector = coordination_signal.get("alignment_vector", {})

        convergence_vector = self._model.converge(alignment_vector)
        metastability_score = self._compute_metastability(convergence_vector)
        divergence_index = self._compute_divergence(convergence_vector)

        convergence_state = self._model.classify_state(
            metastability_score,
            divergence_index
        )

        advisory_level = self._derive_advisory_level(
            metastability_score,
            divergence_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "convergence_vector": convergence_vector,
            "metastability_score": metastability_score,
            "divergence_index": divergence_index,
            "convergence_state": convergence_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CMSCLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            convergence_vector=convergence_vector,
            metastability_score=metastability_score,
            divergence_index=divergence_index,
            convergence_state=convergence_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_metastability(self, convergence_vector: Dict[str, float]) -> float:
        if not convergence_vector:
            return 0.0
        return round(sum(convergence_vector.values()) / len(convergence_vector), 6)

    def _compute_divergence(self, convergence_vector: Dict[str, float]) -> float:
        if not convergence_vector:
            return 0.0
        values = list(convergence_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, metastability: float, divergence: float) -> str:
        if metastability >= 0.88 and divergence <= 0.07:
            return "STABLE"
        if metastability >= 0.75 and divergence <= 0.15:
            return "MONITOR"
        return "ATTENTION"