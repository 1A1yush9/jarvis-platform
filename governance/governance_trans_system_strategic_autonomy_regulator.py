# ============================================================
# Jarvis Platform — Stage 145.0
# Governance Trans-System Strategic Autonomy Regulator (TSAR)
# Deterministic | Advisory-Only | Ledger-Compatible
# ============================================================

from __future__ import annotations

import hashlib
import json
import math
import time
from dataclasses import dataclass, asdict
from typing import Dict, Tuple

# ============================================================
# Deterministic Constants
# ============================================================

MODEL_VERSION = "145.0"
HASH_SALT = "jarvis_tsar_v145"

TRANS_SYSTEMS = [
    "earth_system",
    "orbital_system",
    "lunar_system",
    "mars_system",
    "deep_space_system",
]

AUTONOMY_CRITICAL_THRESHOLD = 0.36
AUTONOMY_WARNING_THRESHOLD = 0.54
AUTONOMY_STABLE_THRESHOLD = 0.70


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class StrategicAutonomySignal:
    system: str
    self_sufficiency_index: float  # 0.0–1.0
    dependency_index: float  # 0.0–1.0
    resilience_index: float  # 0.0–1.0
    adaptability_index: float  # 0.0–1.0


@dataclass(frozen=True)
class TransSystemAutonomyState:
    timestamp: int
    signals: Tuple[StrategicAutonomySignal, ...]


@dataclass(frozen=True)
class AutonomyAssessment:
    autonomy_score: float
    dependency_pressure_index: float
    sustainment_envelope_index: float
    escalation_level: str
    deterministic_hash: str


# ============================================================
# Deterministic Utilities
# ============================================================

def _stable_hash(payload: Dict) -> str:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256((HASH_SALT + serialized).encode()).hexdigest()


def _bounded(v: float) -> float:
    return max(0.0, min(1.0, v))


# ============================================================
# TSAR Engine
# ============================================================

class TransSystemStrategicAutonomyRegulator:

    def __init__(self) -> None:
        self._last_hash: str | None = None

    # --------------------------------------------------------
    # Public Evaluation Interface
    # --------------------------------------------------------

    def evaluate(self, state: TransSystemAutonomyState) -> AutonomyAssessment:

        normalized = self._normalize_signals(state.signals)

        autonomy_score = self._compute_autonomy_score(normalized)
        dependency_pressure_index = self._compute_dependency_pressure(normalized)
        sustainment_envelope_index = self._compute_sustainment_envelope(normalized)

        escalation = self._classify_escalation(
            autonomy_score,
            dependency_pressure_index,
            sustainment_envelope_index
        )

        payload = {
            "timestamp": state.timestamp,
            "autonomy_score": autonomy_score,
            "dependency_pressure_index": dependency_pressure_index,
            "sustainment_envelope_index": sustainment_envelope_index,
            "escalation": escalation,
        }

        deterministic_hash = _stable_hash(payload)
        self._last_hash = deterministic_hash

        return AutonomyAssessment(
            autonomy_score=autonomy_score,
            dependency_pressure_index=dependency_pressure_index,
            sustainment_envelope_index=sustainment_envelope_index,
            escalation_level=escalation,
            deterministic_hash=deterministic_hash,
        )

    # --------------------------------------------------------
    # Normalization Layer
    # --------------------------------------------------------

    def _normalize_signals(
        self,
        signals: Tuple[StrategicAutonomySignal, ...]
    ) -> Dict[str, float]:

        system_scores: Dict[str, float] = {}

        for s in signals:

            self_sufficiency_component = s.self_sufficiency_index * 0.35
            dependency_component = (1 - s.dependency_index) * 0.30
            resilience_component = s.resilience_index * 0.20
            adaptability_component = s.adaptability_index * 0.15

            score = _bounded(
                self_sufficiency_component
                + dependency_component
                + resilience_component
                + adaptability_component
            )

            if s.system in TRANS_SYSTEMS:
                system_scores[s.system] = score

        return system_scores

    # --------------------------------------------------------
    # Autonomy Computation
    # --------------------------------------------------------

    def _compute_autonomy_score(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 1.0

        return _bounded(sum(scores.values()) / len(scores))

    def _compute_dependency_pressure(self, scores: Dict[str, float]) -> float:

        if len(scores) < 2:
            return 0.0

        values = list(scores.values())
        return _bounded(max(values) - min(values))

    def _compute_sustainment_envelope(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 0.0

        squared_sum = sum(v ** 2 for v in scores.values())
        return _bounded(math.sqrt(squared_sum / len(scores)))

    # --------------------------------------------------------
    # Escalation Logic
    # --------------------------------------------------------

    def _classify_escalation(
        self,
        autonomy: float,
        dependency_pressure: float,
        sustainment_envelope: float
    ) -> str:

        if autonomy < AUTONOMY_CRITICAL_THRESHOLD or dependency_pressure > 0.65:
            return "TRANS_SYSTEM_CRITICAL"

        if autonomy < AUTONOMY_WARNING_THRESHOLD or dependency_pressure > 0.45:
            return "TRANS_SYSTEM_WARNING"

        if autonomy < AUTONOMY_STABLE_THRESHOLD:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner (Safe Advisory Mode)
# ============================================================

if __name__ == "__main__":

    sample_state = TransSystemAutonomyState(
        timestamp=int(time.time()),
        signals=(
            StrategicAutonomySignal("earth_system", 0.66, 0.41, 0.58, 0.54),
            StrategicAutonomySignal("orbital_system", 0.57, 0.48, 0.52, 0.50),
            StrategicAutonomySignal("lunar_system", 0.53, 0.51, 0.49, 0.47),
            StrategicAutonomySignal("mars_system", 0.49, 0.54, 0.46, 0.44),
            StrategicAutonomySignal("deep_space_system", 0.45, 0.58, 0.43, 0.41),
        ),
    )

    regulator = TransSystemStrategicAutonomyRegulator()
    result = regulator.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))