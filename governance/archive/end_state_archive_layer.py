"""
Stage-166.0 — Civilizational Recursive Governance End-State Archive Layer (CRGEAL)

Deterministic archival advisory module providing:

• Recursive governance end-state archival validation
• Archival integrity coherence scoring
• Post-archive deviation detection
• Advisory governance signaling

Authority Model:
ADVISORY ONLY — ZERO execution authority.
"""

from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, Any
import hashlib
import json
import os
import time

from governance.archive.archive_integrity_model import ArchiveIntegrityModel
from governance.telemetry.crgeal_telemetry import CRGEALTelemetryClient


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
class CRGEALSignal:
    timestamp: float
    epoch_index: int
    archive_vector: Dict[str, float]
    integrity_score: float
    deviation_index: float
    archive_state: str
    advisory_level: str
    hash: str


# ============================================================
# Archive Layer
# ============================================================

class CivilizationalRecursiveGovernanceEndStateArchiveLayer:

    def __init__(self):
        self._model = ArchiveIntegrityModel()
        self._telemetry = CRGEALTelemetryClient()
        self._archive_path = os.getenv("CRGEAL_ARCHIVE_PATH", "/tmp/crgeal_archive.log")

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def archive(self, seal_signal: Dict[str, Any]) -> CRGEALSignal:
        """
        Deterministic recursive governance end-state archival synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = seal_signal.get("epoch_index", 0)

        seal_vector = seal_signal.get("seal_vector", {})

        archive_vector = self._model.evaluate(seal_vector)
        integrity_score = self._compute_integrity(archive_vector)
        deviation_index = self._compute_deviation(archive_vector)

        archive_state = self._model.classify_state(
            integrity_score,
            deviation_index
        )

        advisory_level = self._derive_advisory_level(
            integrity_score,
            deviation_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "archive_vector": archive_vector,
            "integrity_score": integrity_score,
            "deviation_index": deviation_index,
            "archive_state": archive_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRGEALSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            archive_vector=archive_vector,
            integrity_score=integrity_score,
            deviation_index=deviation_index,
            archive_state=archive_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._append_archive(asdict(signal))
        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_integrity(self, archive_vector: Dict[str, float]) -> float:
        if not archive_vector:
            return 0.0
        return round(sum(archive_vector.values()) / len(archive_vector), 6)

    def _compute_deviation(self, archive_vector: Dict[str, float]) -> float:
        if not archive_vector:
            return 0.0
        values = list(archive_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, integrity: float, deviation: float) -> str:
        if integrity >= 0.99 and deviation <= 0.015:
            return "ARCHIVED_STABLE"
        if integrity >= 0.94 and deviation <= 0.05:
            return "ARCHIVED_MONITORED"
        return "ARCHIVED_ATTENTION"

    # --------------------------------------------------------
    # Deterministic Archive Append
    # --------------------------------------------------------

    def _append_archive(self, payload: Dict[str, Any]) -> None:
        serialized = json.dumps(payload, sort_keys=True)
        with open(self._archive_path, "a", encoding="utf-8") as f:
            f.write(serialized + "\n")