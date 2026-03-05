# ============================================================
# Jarvis Platform — Stage 144.0
# Governance Multisystem Strategic Continuity Engine (MSCE)
# Deterministic | Advisory-Only | Ledger-Compatible
# ============================================================

from __future__ import annotations

import hashlib
import json
import math
import time
from dataclasses import dataclass, asdict
from typing import Dict, Tuple, List

# ============================================================
# Deterministic Constants
# ============================================================

MODEL_VERSION = "144.0"
HASH_SALT = "jarvis_msce_v144"

MULTISYSTEM_THEATERS = [
    "earth_system",
    "orbital_system",
    "lunar_system",
    "mars_system",
    "deep_space_system",
]

CONTINUITY_CRITICAL_THRESHOLD = 0.38
CONTINUITY_WARNING_THRESHOLD = 0.55
CONTINUITY_STABLE_THRESHOLD = 0.70


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class StrategicContinuitySignal:
    system: str
    survivability_index: float  # 0.0–1.0
    redundancy_index: float  # 0.0–1.0
    adaptability_index: float  # 0.0–1.0
    disruption_index: float  # 0.0–1.0


@dataclass(frozen=True)
class MultisystemContinuityState:
    timestamp: int
    signals: Tuple[StrategicContinuitySignal, ...]


@dataclass(frozen=True)
class ContinuityAssessment:
    continuity_score: float
    cascade_risk_index: float
    resilience_envelope_index: float
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
# MSCE Engine
# ============================================================

class MultisystemStrategicContinuityEngine:

    def __init__(self) -> None:
        self._last_hash: str | None = None

    # --------------------------------------------------------
    # Public Evaluation Interface
    # --------------------------------------------------------

    def evaluate(self, state: MultisystemContinuityState) -> ContinuityAssessment:

        normalized = self._normalize_signals(state.signals)

        continuity_score = self._compute_continuity_score(normalized)
        cascade_risk_index = self._compute_cascade_risk(normalized)
        resilience_envelope_index = self._compute_resilience_envelope(normalized)

        escalation = self._classify_escalation(
            continuity_score,
            cascade_risk_index,
            resilience_envelope_index
        )

        payload = {
            "timestamp": state.timestamp,
            "continuity_score": continuity_score,
            "cascade_risk_index": cascade_risk_index,
            "resilience_envelope_index": resilience_envelope_index,
            "escalation": escalation,
        }

        deterministic_hash = _stable_hash(payload)
        self._last_hash = deterministic_hash

        return ContinuityAssessment(
            continuity_score=continuity_score,
            cascade_risk_index=cascade_risk_index,
            resilience_envelope_index=resilience_envelope_index,
            escalation_level=escalation,
            deterministic_hash=deterministic_hash,
        )

    # --------------------------------------------------------
    # Normalization Layer
    # --------------------------------------------------------

    def _normalize_signals(
        self,
        signals: Tuple[StrategicContinuitySignal, ...]
    ) -> Dict[str, float]:

        system_scores: Dict[str, float] = {}

        for s in signals:

            survivability_component = s.survivability_index * 0.35
            redundancy_component = s.redundancy_index * 0.25
            adaptability_component = s.adaptability_index * 0.25
            disruption_component = (1 - s.disruption_index) * 0.15

            score = _bounded(
                survivability_component
                + redundancy_component
                + adaptability_component
                + disruption_component
            )

            if s.system in MULTISYSTEM_THEATERS:
                system_scores[s.system] = score

        return system_scores

    # --------------------------------------------------------
    # Continuity Computation
    # --------------------------------------------------------

    def _compute_continuity_score(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 1.0

        return _bounded(sum(scores.values()) / len(scores))

    def _compute_cascade_risk(self, scores: Dict[str, float]) -> float:

        if len(scores) < 2:
            return 0.0

        values = list(scores.values())
        worst = min(values)
        best = max(values)

        return _bounded(best - worst)

    def _compute_resilience_envelope(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 0.0

        squared_sum = sum(v ** 2 for v in scores.values())
        return _bounded(math.sqrt(squared_sum / len(scores)))

    # --------------------------------------------------------
    # Escalation Logic
    # --------------------------------------------------------

    def _classify_escalation(
        self,
        continuity: float,
        cascade: float,
        envelope: float
    ) -> str:

        if continuity < CONTINUITY_CRITICAL_THRESHOLD or cascade > 0.65:
            return "MULTISYSTEM_CRITICAL"

        if continuity < CONTINUITY_WARNING_THRESHOLD or cascade > 0.45:
            return "MULTISYSTEM_WARNING"

        if continuity < CONTINUITY_STABLE_THRESHOLD:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner (Safe Advisory Mode)
# ============================================================

if __name__ == "__main__":

    sample_state = MultisystemContinuityState(
        timestamp=int(time.time()),
        signals=(
            StrategicContinuitySignal("earth_system", 0.64, 0.58, 0.55, 0.39),
            StrategicContinuitySignal("orbital_system", 0.56, 0.52, 0.50, 0.44),
            StrategicContinuitySignal("lunar_system", 0.53, 0.49, 0.48, 0.46),
            StrategicContinuitySignal("mars_system", 0.48, 0.45, 0.46, 0.50),
            StrategicContinuitySignal("deep_space_system", 0.44, 0.42, 0.43, 0.52),
        ),
    )

    engine = MultisystemStrategicContinuityEngine()
    result = engine.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))