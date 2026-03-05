"""
Stage-167.0 — Civilizational Recursive Governance Memory Preservation Layer (CRGMPL)

Deterministic preservation advisory module providing:

• Recursive governance memory preservation validation
• Lineage continuity integrity scoring
• Memory erosion detection
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

from governance.memory.memory_integrity_model import MemoryIntegrityModel
from governance.telemetry.crgmpl_telemetry import CRGMPLTelemetryClient


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
class CRGMPLSignal:
    timestamp: float
    epoch_index: int
    memory_vector: Dict[str, float]
    continuity_score: float
    erosion_index: float
    memory_state: str
    advisory_level: str
    hash: str


# ============================================================
# Memory Layer
# ============================================================

class CivilizationalRecursiveGovernanceMemoryPreservationLayer:

    def __init__(self):
        self._model = MemoryIntegrityModel()
        self._telemetry = CRGMPLTelemetryClient()
        self._memory_path = os.getenv("CRGMPL_MEMORY_PATH", "/tmp/crgmpl_memory.log")

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def preserve(self, archive_signal: Dict[str, Any]) -> CRGMPLSignal:
        """
        Deterministic recursive governance memory preservation synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = archive_signal.get("epoch_index", 0)

        archive_vector = archive_signal.get("archive_vector", {})

        memory_vector = self._model.evaluate(archive_vector)
        continuity_score = self._compute_continuity(memory_vector)
        erosion_index = self._compute_erosion(memory_vector)

        memory_state = self._model.classify_state(
            continuity_score,
            erosion_index
        )

        advisory_level = self._derive_advisory_level(
            continuity_score,
            erosion_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "memory_vector": memory_vector,
            "continuity_score": continuity_score,
            "erosion_index": erosion_index,
            "memory_state": memory_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CRGMPLSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            memory_vector=memory_vector,
            continuity_score=continuity_score,
            erosion_index=erosion_index,
            memory_state=memory_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._append_memory(asdict(signal))
        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_continuity(self, memory_vector: Dict[str, float]) -> float:
        if not memory_vector:
            return 0.0
        return round(sum(memory_vector.values()) / len(memory_vector), 6)

    def _compute_erosion(self, memory_vector: Dict[str, float]) -> float:
        if not memory_vector:
            return 0.0
        values = list(memory_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, continuity: float, erosion: float) -> str:
        if continuity >= 0.99 and erosion <= 0.015:
            return "MEMORY_STABLE"
        if continuity >= 0.94 and erosion <= 0.05:
            return "MEMORY_MONITORED"
        return "MEMORY_ATTENTION"

    # --------------------------------------------------------
    # Deterministic Memory Append
    # --------------------------------------------------------

    def _append_memory(self, payload: Dict[str, Any]) -> None:
        serialized = json.dumps(payload, sort_keys=True)
        with open(self._memory_path, "a", encoding="utf-8") as f:
            f.write(serialized + "\n")