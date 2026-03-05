"""
Stage-157.0 — Civilizational Terminal Stability Governance Layer (CTSG)

Deterministic terminal-governance advisory module providing:

• Terminal stability convergence evaluation
• End-state instability detection
• Deterministic terminal scoring
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

from governance.terminal.terminal_stability_model import TerminalStabilityModel
from governance.telemetry.ctsg_telemetry import CTSGTelemetryClient


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
class CTSGSignal:
    timestamp: float
    epoch_index: int
    terminal_vector: Dict[str, float]
    terminal_score: float
    instability_index: float
    terminal_state: str
    advisory_level: str
    hash: str


# ============================================================
# Governance Layer
# ============================================================

class CivilizationalTerminalStabilityGovernanceLayer:

    def __init__(self):
        self._model = TerminalStabilityModel()
        self._telemetry = CTSGTelemetryClient()

    # --------------------------------------------------------
    # Public Interface
    # --------------------------------------------------------

    def govern(self, assurance_signal: Dict[str, Any]) -> CTSGSignal:
        """
        Deterministic terminal stability governance synthesis.
        """

        timestamp = round(time.time(), 3)
        epoch_index = assurance_signal.get("epoch_index", 0)

        assurance_vector = assurance_signal.get("assurance_vector", {})

        terminal_vector = self._model.evaluate(assurance_vector)
        terminal_score = self._compute_terminal_score(terminal_vector)
        instability_index = self._compute_instability(terminal_vector)

        terminal_state = self._model.classify_state(
            terminal_score,
            instability_index
        )

        advisory_level = self._derive_advisory_level(
            terminal_score,
            instability_index
        )

        payload = {
            "timestamp": timestamp,
            "epoch_index": epoch_index,
            "terminal_vector": terminal_vector,
            "terminal_score": terminal_score,
            "instability_index": instability_index,
            "terminal_state": terminal_state,
            "advisory_level": advisory_level,
        }

        signal_hash = _deterministic_hash(payload)

        signal = CTSGSignal(
            timestamp=timestamp,
            epoch_index=epoch_index,
            terminal_vector=terminal_vector,
            terminal_score=terminal_score,
            instability_index=instability_index,
            terminal_state=terminal_state,
            advisory_level=advisory_level,
            hash=signal_hash,
        )

        self._telemetry.emit(asdict(signal))

        return signal

    # --------------------------------------------------------
    # Deterministic Analysis
    # --------------------------------------------------------

    def _compute_terminal_score(self, terminal_vector: Dict[str, float]) -> float:
        if not terminal_vector:
            return 0.0
        return round(sum(terminal_vector.values()) / len(terminal_vector), 6)

    def _compute_instability(self, terminal_vector: Dict[str, float]) -> float:
        if not terminal_vector:
            return 0.0
        values = list(terminal_vector.values())
        return round(max(values) - min(values), 6)

    def _derive_advisory_level(self, score: float, instability: float) -> str:
        if score >= 0.92 and instability <= 0.05:
            return "STABLE"
        if score >= 0.8 and instability <= 0.12:
            return "MONITOR"
        return "ATTENTION"