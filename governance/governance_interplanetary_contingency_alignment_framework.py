# ============================================================
# Jarvis Platform — Stage 143.0
# Governance Interplanetary Contingency Alignment Framework (ICAF)
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

MODEL_VERSION = "143.0"
HASH_SALT = "jarvis_icaf_v143"

INTERPLANETARY_THEATERS = [
    "earth",
    "cislunar",
    "lunar_surface",
    "mars_orbit",
    "mars_surface",
    "deep_space",
]

ALIGNMENT_CRITICAL_THRESHOLD = 0.40
ALIGNMENT_WARNING_THRESHOLD = 0.58
ALIGNMENT_STABLE_THRESHOLD = 0.72


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class ContingencySignal:
    theater: str
    readiness_index: float  # 0.0–1.0
    coordination_index: float  # 0.0–1.0
    logistics_index: float  # 0.0–1.0
    volatility_index: float  # 0.0–1.0


@dataclass(frozen=True)
class InterplanetaryContingencyState:
    timestamp: int
    signals: Tuple[ContingencySignal, ...]


@dataclass(frozen=True)
class AlignmentAssessment:
    alignment_score: float
    divergence_index: float
    interdependency_index: float
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
# ICAF Engine
# ============================================================

class InterplanetaryContingencyAlignmentFramework:

    def __init__(self) -> None:
        self._last_hash: str | None = None

    # --------------------------------------------------------
    # Public Evaluation Interface
    # --------------------------------------------------------

    def evaluate(self, state: InterplanetaryContingencyState) -> AlignmentAssessment:

        normalized = self._normalize_signals(state.signals)

        alignment_score = self._compute_alignment_score(normalized)
        divergence_index = self._compute_divergence(normalized)
        interdependency_index = self._compute_interdependency(normalized)

        escalation = self._classify_escalation(
            alignment_score,
            divergence_index,
            interdependency_index
        )

        payload = {
            "timestamp": state.timestamp,
            "alignment_score": alignment_score,
            "divergence_index": divergence_index,
            "interdependency_index": interdependency_index,
            "escalation": escalation,
        }

        deterministic_hash = _stable_hash(payload)
        self._last_hash = deterministic_hash

        return AlignmentAssessment(
            alignment_score=alignment_score,
            divergence_index=divergence_index,
            interdependency_index=interdependency_index,
            escalation_level=escalation,
            deterministic_hash=deterministic_hash,
        )

    # --------------------------------------------------------
    # Normalization Layer
    # --------------------------------------------------------

    def _normalize_signals(
        self,
        signals: Tuple[ContingencySignal, ...]
    ) -> Dict[str, float]:

        theater_scores: Dict[str, float] = {}

        for s in signals:

            readiness_component = s.readiness_index * 0.35
            coordination_component = s.coordination_index * 0.30
            logistics_component = s.logistics_index * 0.20
            volatility_component = (1 - s.volatility_index) * 0.15

            score = _bounded(
                readiness_component
                + coordination_component
                + logistics_component
                + volatility_component
            )

            if s.theater in INTERPLANETARY_THEATERS:
                theater_scores[s.theater] = score

        return theater_scores

    # --------------------------------------------------------
    # Alignment Computation
    # --------------------------------------------------------

    def _compute_alignment_score(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 1.0

        return _bounded(sum(scores.values()) / len(scores))

    def _compute_divergence(self, scores: Dict[str, float]) -> float:

        if len(scores) < 2:
            return 0.0

        values = list(scores.values())
        mean_val = sum(values) / len(values)
        variance = sum((v - mean_val) ** 2 for v in values) / len(values)

        return _bounded(math.sqrt(variance))

    def _compute_interdependency(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 0.0

        squared_sum = sum(v ** 2 for v in scores.values())
        return _bounded(math.sqrt(squared_sum / len(scores)))

    # --------------------------------------------------------
    # Escalation Logic
    # --------------------------------------------------------

    def _classify_escalation(
        self,
        alignment: float,
        divergence: float,
        interdependency: float
    ) -> str:

        if alignment < ALIGNMENT_CRITICAL_THRESHOLD or divergence > 0.65:
            return "INTERPLANETARY_CRITICAL"

        if alignment < ALIGNMENT_WARNING_THRESHOLD or divergence > 0.45:
            return "INTERPLANETARY_WARNING"

        if alignment < ALIGNMENT_STABLE_THRESHOLD:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner (Safe Advisory Mode)
# ============================================================

if __name__ == "__main__":

    sample_state = InterplanetaryContingencyState(
        timestamp=int(time.time()),
        signals=(
            ContingencySignal("earth", 0.61, 0.58, 0.55, 0.42),
            ContingencySignal("cislunar", 0.54, 0.49, 0.51, 0.46),
            ContingencySignal("lunar_surface", 0.52, 0.50, 0.48, 0.44),
            ContingencySignal("mars_orbit", 0.47, 0.45, 0.46, 0.51),
            ContingencySignal("mars_surface", 0.44, 0.42, 0.45, 0.53),
            ContingencySignal("deep_space", 0.40, 0.39, 0.41, 0.57),
        ),
    )

    framework = InterplanetaryContingencyAlignmentFramework()
    result = framework.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))