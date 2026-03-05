# ============================================================
# Jarvis Platform — Stage 149.0
# Governance Civilization Meta-Stability Guardian (CMG)
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

MODEL_VERSION = "149.0"
HASH_SALT = "jarvis_cmg_v149"

META_STABILITY_DOMAINS = [
    "systemic_resilience",
    "adaptive_capacity",
    "stability_coherence",
    "disturbance_absorption",
    "longwave_balance",
]

META_CRITICAL_THRESHOLD = 0.34
META_WARNING_THRESHOLD = 0.52
META_STABLE_THRESHOLD = 0.70


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class MetaStabilitySignal:
    domain: str
    stability_index: float
    oscillation_index: float
    resilience_index: float
    adaptability_index: float


@dataclass(frozen=True)
class CivilizationMetaStabilityState:
    timestamp: int
    signals: Tuple[MetaStabilitySignal, ...]


@dataclass(frozen=True)
class MetaStabilityAssessment:
    meta_stability_score: float
    oscillation_pressure_index: float
    resilience_decay_index: float
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
# CMG Engine
# ============================================================

class CivilizationMetaStabilityGuardian:

    def __init__(self) -> None:
        self._last_hash: str | None = None

    # --------------------------------------------------------
    # Public Evaluation Interface
    # --------------------------------------------------------

    def evaluate(self, state: CivilizationMetaStabilityState) -> MetaStabilityAssessment:

        normalized = self._normalize_signals(state.signals)

        meta_score = self._compute_meta_stability(normalized)
        oscillation_pressure = self._compute_oscillation_pressure(normalized)
        resilience_decay = self._compute_resilience_decay(normalized)

        escalation = self._classify_escalation(
            meta_score,
            oscillation_pressure,
            resilience_decay
        )

        payload = {
            "timestamp": state.timestamp,
            "meta_score": meta_score,
            "oscillation_pressure": oscillation_pressure,
            "resilience_decay": resilience_decay,
            "escalation": escalation,
        }

        deterministic_hash = _stable_hash(payload)
        self._last_hash = deterministic_hash

        return MetaStabilityAssessment(
            meta_stability_score=meta_score,
            oscillation_pressure_index=oscillation_pressure,
            resilience_decay_index=resilience_decay,
            escalation_level=escalation,
            deterministic_hash=deterministic_hash,
        )

    # --------------------------------------------------------
    # Signal Normalization
    # --------------------------------------------------------

    def _normalize_signals(
        self,
        signals: Tuple[MetaStabilitySignal, ...]
    ) -> Dict[str, float]:

        domain_scores: Dict[str, float] = {}

        for s in signals:

            stability_component = s.stability_index * 0.35
            oscillation_component = (1 - s.oscillation_index) * 0.30
            resilience_component = s.resilience_index * 0.20
            adaptability_component = s.adaptability_index * 0.15

            score = _bounded(
                stability_component
                + oscillation_component
                + resilience_component
                + adaptability_component
            )

            if s.domain in META_STABILITY_DOMAINS:
                domain_scores[s.domain] = score

        return domain_scores

    # --------------------------------------------------------
    # Meta-Stability Computation
    # --------------------------------------------------------

    def _compute_meta_stability(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 1.0

        return _bounded(sum(scores.values()) / len(scores))

    def _compute_oscillation_pressure(self, scores: Dict[str, float]) -> float:

        if len(scores) < 2:
            return 0.0

        values = list(scores.values())
        mean_val = sum(values) / len(values)

        variance = sum((v - mean_val) ** 2 for v in values) / len(values)
        return _bounded(math.sqrt(variance))

    def _compute_resilience_decay(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 0.0

        lowest = min(scores.values())
        highest = max(scores.values())

        return _bounded(highest - lowest)

    # --------------------------------------------------------
    # Escalation Logic
    # --------------------------------------------------------

    def _classify_escalation(
        self,
        meta_score: float,
        oscillation: float,
        decay: float
    ) -> str:

        if meta_score < META_CRITICAL_THRESHOLD or oscillation > 0.65:
            return "CIVILIZATION_META_CRITICAL"

        if meta_score < META_WARNING_THRESHOLD or oscillation > 0.45:
            return "CIVILIZATION_META_WARNING"

        if meta_score < META_STABLE_THRESHOLD:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner
# ============================================================

if __name__ == "__main__":

    sample_state = CivilizationMetaStabilityState(
        timestamp=int(time.time()),
        signals=(
            MetaStabilitySignal("systemic_resilience", 0.64, 0.42, 0.59, 0.55),
            MetaStabilitySignal("adaptive_capacity", 0.60, 0.45, 0.57, 0.54),
            MetaStabilitySignal("stability_coherence", 0.62, 0.41, 0.58, 0.56),
            MetaStabilitySignal("disturbance_absorption", 0.59, 0.44, 0.55, 0.52),
            MetaStabilitySignal("longwave_balance", 0.61, 0.43, 0.56, 0.53),
        ),
    )

    guardian = CivilizationMetaStabilityGuardian()
    result = guardian.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))