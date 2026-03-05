"""
Stage-152.0 — Civilizational Continuity Forecasting Mesh (CCFM)

Deterministic forecasting module providing:

• Multi-horizon continuity forecasting
• Recursive epoch trajectory projection
• Long-cycle instability detection
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

from governance.forecasting.continuity_projection_model import ContinuityProjectionModel
from governance.telemetry.ccfm_telemetry import CCFMTelemetryClient


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
class CCFMSignal:
    timestamp: float
    epoch_index: int
    horizon_projections: Dict[str, float]
    instability_vector: Dict[str, float]
    advisory_level: str
    hash: str


# ============================================================
# Forecasting Mesh
# ============================================================

class CivilizationalContinuityForecastingMesh:

    def __init__(self):
        self._projection_model = ContinuityProjectionModel()
        self._telemetry = CCFMTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def forecast(self, governance_state: Dict[str, Any]) -> CCFMSignal:
        """
        Deterministic civilizational continuity forecast.
        """

        timestamp = round(time.time(), 3)
        epoch_index = governance_state.get("epoch_index", 0)

        horizon_projections = self._projection_model.project(governance_state)
        instability_vector = self._compute_instability_vector(horizon_projections)

        advisory_level = self._derive_advisory_level(instability_vector)

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "horizon_projections": horizon_projections,
            "instability_vector": instability_vector,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CCFMSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            horizon_projections=horizon_projections,
            instability_vector=instability_vector,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_instability_vector(self, projections: Dict[str, float]) -> Dict[str, float]:
        baseline = projections.get("near_term", 0.95)

        return {
            horizon: round(abs(score - baseline), 6)
            for horizon, score in projections.items()
        }

    def _derive_advisory_level(self, instability_vector: Dict[str, float]) -> str:
        max_instability = max(instability_vector.values())

        if max_instability <= 0.02:
            return "STABLE"

        if max_instability <= 0.05:
            return "MONITOR"

        return "ATTENTION"