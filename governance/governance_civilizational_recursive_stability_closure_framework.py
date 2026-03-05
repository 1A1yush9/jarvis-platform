# ============================================================
# Jarvis Platform — Stage 150.0
# Governance Civilizational Recursive Stability Closure Framework (RSCF)
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

MODEL_VERSION = "150.0"
HASH_SALT = "jarvis_rscf_v150"

RECURSIVE_STABILITY_DOMAINS = [
    "layer_convergence",
    "recursive_coherence",
    "stability_persistence",
    "drift_containment",
    "closure_integrity",
]

CLOSURE_CRITICAL_THRESHOLD = 0.34
CLOSURE_WARNING_THRESHOLD = 0.52
CLOSURE_STABLE_THRESHOLD = 0.70


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class RecursiveStabilitySignal:
    domain: str
    convergence_index: float
    persistence_index: float
    drift_index: float
    coherence_index: float


@dataclass(frozen=True)
class RecursiveStabilityState:
    timestamp: int
    signals: Tuple[RecursiveStabilitySignal, ...]


@dataclass(frozen=True)
class RecursiveClosureAssessment:
    closure_score: float
    recursive_drift_index: float
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
# RSCF Engine
# ============================================================

class CivilizationalRecursiveStabilityClosureFramework:

    def __init__(self) -> None:
        self._last_hash: str | None = None

    # --------------------------------------------------------
    # Public Evaluation Interface
    # --------------------------------------------------------

    def evaluate(self, state: RecursiveStabilityState) -> RecursiveClosureAssessment:

        normalized = self._normalize_signals(state.signals)

        closure_score = self._compute_closure_score(normalized)
        recursive_drift_index = self._compute_recursive_drift(normalized)
        stabilization_envelope = self._compute_stabilization_envelope(normalized)

        escalation = self._classify_escalation(
            closure_score,
            recursive_drift_index,
            stabilization_envelope
        )

        payload = {
            "timestamp": state.timestamp,
            "closure_score": closure_score,
            "recursive_drift_index": recursive_drift_index,
            "stabilization_envelope": stabilization_envelope,
            "escalation": escalation,
        }

        deterministic_hash = _stable_hash(payload)
        self._last_hash = deterministic_hash

        return RecursiveClosureAssessment(
            closure_score=closure_score,
            recursive_drift_index=recursive_drift_index,
            stabilization_envelope_index=stabilization_envelope,
            escalation_level=escalation,
            deterministic_hash=deterministic_hash,
        )

    # --------------------------------------------------------
    # Signal Normalization
    # --------------------------------------------------------

    def _normalize_signals(
        self,
        signals: Tuple[RecursiveStabilitySignal, ...]
    ) -> Dict[str, float]:

        domain_scores: Dict[str, float] = {}

        for s in signals:

            convergence_component = s.convergence_index * 0.35
            persistence_component = s.persistence_index * 0.25
            drift_component = (1 - s.drift_index) * 0.25
            coherence_component = s.coherence_index * 0.15

            score = _bounded(
                convergence_component
                + persistence_component
                + drift_component
                + coherence_component
            )

            if s.domain in RECURSIVE_STABILITY_DOMAINS:
                domain_scores[s.domain] = score

        return domain_scores

    # --------------------------------------------------------
    # Recursive Stability Computation
    # --------------------------------------------------------

    def _compute_closure_score(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 1.0

        return _bounded(sum(scores.values()) / len(scores))

    def _compute_recursive_drift(self, scores: Dict[str, float]) -> float:

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
        closure: float,
        drift: float,
        envelope: float
    ) -> str:

        if closure < CLOSURE_CRITICAL_THRESHOLD or drift > 0.65:
            return "CIVILIZATION_CLOSURE_CRITICAL"

        if closure < CLOSURE_WARNING_THRESHOLD or drift > 0.45:
            return "CIVILIZATION_CLOSURE_WARNING"

        if closure < CLOSURE_STABLE_THRESHOLD:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner
# ============================================================

if __name__ == "__main__":

    sample_state = RecursiveStabilityState(
        timestamp=int(time.time()),
        signals=(
            RecursiveStabilitySignal("layer_convergence", 0.65, 0.60, 0.42, 0.57),
            RecursiveStabilitySignal("recursive_coherence", 0.63, 0.58, 0.44, 0.55),
            RecursiveStabilitySignal("stability_persistence", 0.61, 0.57, 0.45, 0.54),
            RecursiveStabilitySignal("drift_containment", 0.59, 0.55, 0.46, 0.53),
            RecursiveStabilitySignal("closure_integrity", 0.62, 0.59, 0.43, 0.56),
        ),
    )

    framework = CivilizationalRecursiveStabilityClosureFramework()
    result = framework.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))