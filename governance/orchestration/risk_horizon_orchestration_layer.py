"""
Stage-153.0 — Civilizational Risk Horizon Orchestration Layer (CRHOL)

Deterministic orchestration advisory module providing:

• Cross-horizon risk synthesis
• Cascading trajectory exposure analysis
• Deterministic risk horizon classification
• Advisory orchestration signaling

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any
import hashlib
import json
import time

from governance.orchestration.risk_horizon_model import RiskHorizonModel
from governance.telemetry.crhol_telemetry import CRHOLTelemetryClient


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
class CRHOLSignal:
    timestamp: float
    epoch_index: int
    normalized_vector: Dict[str, float]
    cascade_risk_score: float
    horizon_classification: str
    advisory_level: str
    hash: str


# ============================================================
# Orchestration Layer
# ============================================================

class CivilizationalRiskHorizonOrchestrationLayer:

    def __init__(self):
        self._model = RiskHorizonModel()
        self._telemetry = CRHOLTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def orchestrate(self, forecasting_signal: Dict[str, Any]) -> CRHOLSignal:
        """
        Deterministic risk horizon orchestration.
        """

        timestamp = round(time.time(), 3)
        epoch_index = forecasting_signal.get("epoch_index", 0)

        projections = forecasting_signal.get("horizon_projections", {})

        normalized_vector = self._normalize(projections)
        cascade_risk_score = self._compute_cascade_risk(normalized_vector)

        horizon_classification = self._model.classify(
            normalized_vector,
            cascade_risk_score
        )

        advisory_level = self._derive_advisory_level(cascade_risk_score)

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "normalized_vector": normalized_vector,
            "cascade_risk_score": cascade_risk_score,
            "horizon_classification": horizon_classification,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRHOLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            normalized_vector=normalized_vector,
            cascade_risk_score=cascade_risk_score,
            horizon_classification=horizon_classification,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _normalize(self, projections: Dict[str, float]) -> Dict[str, float]:
        total = sum(projections.values()) or 1.0
        return {
            k: round(v / total, 6)
            for k, v in projections.items()
        }

    def _compute_cascade_risk(self, normalized_vector: Dict[str, float]) -> float:
        values = list(normalized_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, cascade_risk_score: float) -> str:
        if cascade_risk_score <= 0.05:
            return "STABLE"
        if cascade_risk_score <= 0.12:
            return "MONITOR"
        return "ATTENTION"