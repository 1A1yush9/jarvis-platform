# ============================================================
# Jarvis Platform — Stage 147.0
# Governance Civilization Continuity Singularity Framework (CCSF)
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

MODEL_VERSION = "147.0"
HASH_SALT = "jarvis_ccsf_v147"

CIV_CONTINUITY_DOMAINS = [
    "infrastructure_continuity",
    "knowledge_continuity",
    "biosphere_continuity",
    "governance_continuity",
    "technological_continuity",
]

SINGULARITY_CRITICAL_THRESHOLD = 0.33
SINGULARITY_WARNING_THRESHOLD = 0.52
SINGULARITY_STABLE_THRESHOLD = 0.70


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class ContinuitySignal:
    domain: str
    continuity_index: float  # 0.0–1.0
    acceleration_index: float  # 0.0–1.0
    irreversibility_index: float  # 0.0–1.0
    resilience_index: float  # 0.0–1.0


@dataclass(frozen=True)
class CivilizationContinuityState:
    timestamp: int
    signals: Tuple[ContinuitySignal, ...]


@dataclass(frozen=True)
class SingularityAssessment:
    singularity_score: float
    convergence_acceleration_index: float
    stabilization_envelope_index: float
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
# CCSF Engine
# ============================================================

class CivilizationContinuitySingularityFramework:

    def __init__(self) -> None:
        self._last_hash: str | None = None

    # --------------------------------------------------------
    # Public Evaluation Interface
    # --------------------------------------------------------

    def evaluate(self, state: CivilizationContinuityState) -> SingularityAssessment:

        normalized = self._normalize_signals(state.signals)

        singularity_score = self._compute_singularity_score(normalized)
        convergence_acceleration_index = self._compute_acceleration(normalized)
        stabilization_envelope_index = self._compute_stabilization_envelope(normalized)

        escalation = self._classify_escalation(
            singularity_score,
            convergence_acceleration_index,
            stabilization_envelope_index
        )

        payload = {
            "timestamp": state.timestamp,
            "singularity_score": singularity_score,
            "acceleration_index": convergence_acceleration_index,
            "stabilization_index": stabilization_envelope_index,
            "escalation": escalation,
        }

        deterministic_hash = _stable_hash(payload)
        self._last_hash = deterministic_hash

        return SingularityAssessment(
            singularity_score=singularity_score,
            convergence_acceleration_index=convergence_acceleration_index,
            stabilization_envelope_index=stabilization_envelope_index,
            escalation_level=escalation,
            deterministic_hash=deterministic_hash,
        )

    # --------------------------------------------------------
    # Normalization Layer
    # --------------------------------------------------------

    def _normalize_signals(
        self,
        signals: Tuple[ContinuitySignal, ...]
    ) -> Dict[str, float]:

        domain_scores: Dict[str, float] = {}

        for s in signals:

            continuity_component = s.continuity_index * 0.35
            acceleration_component = s.acceleration_index * 0.25
            irreversibility_component = (1 - s.irreversibility_index) * 0.20
            resilience_component = s.resilience_index * 0.20

            score = _bounded(
                continuity_component
                + acceleration_component
                + irreversibility_component
                + resilience_component
            )

            if s.domain in CIV_CONTINUITY_DOMAINS:
                domain_scores[s.domain] = score

        return domain_scores

    # --------------------------------------------------------
    # Singularity Computation
    # --------------------------------------------------------

    def _compute_singularity_score(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 1.0

        return _bounded(sum(scores.values()) / len(scores))

    def _compute_acceleration(self, scores: Dict[str, float]) -> float:

        if len(scores) < 2:
            return 0.0

        values = list(scores.values())
        mean_val = sum(values) / len(values)
        variance = sum((v - mean_val) ** 2 for v in values) / len(values)

        return _bounded(math.sqrt(variance))

    def _compute_stabilization_envelope(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 0.0

        squared_sum = sum(v ** 2 for v in scores.values())
        return _bounded(math.sqrt(squared_sum / len(scores)))

    # --------------------------------------------------------
    # Escalation Logic
    # --------------------------------------------------------

    def _classify_escalation(
        self,
        singularity: float,
        acceleration: float,
        stabilization: float
    ) -> str:

        if singularity < SINGULARITY_CRITICAL_THRESHOLD or acceleration > 0.65:
            return "CIVILIZATION_SINGULARITY_CRITICAL"

        if singularity < SINGULARITY_WARNING_THRESHOLD or acceleration > 0.45:
            return "CIVILIZATION_SINGULARITY_WARNING"

        if singularity < SINGULARITY_STABLE_THRESHOLD:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner (Safe Advisory Mode)
# ============================================================

if __name__ == "__main__":

    sample_state = CivilizationContinuityState(
        timestamp=int(time.time()),
        signals=(
            ContinuitySignal("infrastructure_continuity", 0.62, 0.55, 0.44, 0.58),
            ContinuitySignal("knowledge_continuity", 0.60, 0.53, 0.46, 0.57),
            ContinuitySignal("biosphere_continuity", 0.57, 0.52, 0.48, 0.54),
            ContinuitySignal("governance_continuity", 0.55, 0.50, 0.49, 0.53),
            ContinuitySignal("technological_continuity", 0.58, 0.54, 0.47, 0.55),
        ),
    )

    framework = CivilizationContinuitySingularityFramework()
    result = framework.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))