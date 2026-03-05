# ============================================================
# Jarvis Platform — Stage 148.0
# Governance Civilization Equilibrium Preservation Architecture (CEPA)
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

MODEL_VERSION = "148.0"
HASH_SALT = "jarvis_cepa_v148"

CIV_EQUILIBRIUM_DOMAINS = [
    "resource_equilibrium",
    "ecological_equilibrium",
    "infrastructure_equilibrium",
    "governance_equilibrium",
    "technological_equilibrium",
]

EQUILIBRIUM_CRITICAL_THRESHOLD = 0.35
EQUILIBRIUM_WARNING_THRESHOLD = 0.52
EQUILIBRIUM_STABLE_THRESHOLD = 0.70


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class EquilibriumSignal:
    domain: str
    balance_index: float
    pressure_index: float
    resilience_index: float
    adaptability_index: float


@dataclass(frozen=True)
class CivilizationEquilibriumState:
    timestamp: int
    signals: Tuple[EquilibriumSignal, ...]


@dataclass(frozen=True)
class EquilibriumAssessment:
    equilibrium_score: float
    disequilibrium_pressure_index: float
    stability_envelope_index: float
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
# CEPA Engine
# ============================================================

class CivilizationEquilibriumPreservationArchitecture:

    def __init__(self) -> None:
        self._last_hash: str | None = None

    # --------------------------------------------------------
    # Public Evaluation Interface
    # --------------------------------------------------------

    def evaluate(self, state: CivilizationEquilibriumState) -> EquilibriumAssessment:

        normalized = self._normalize_signals(state.signals)

        equilibrium_score = self._compute_equilibrium_score(normalized)
        pressure_index = self._compute_disequilibrium_pressure(normalized)
        stability_envelope = self._compute_stability_envelope(normalized)

        escalation = self._classify_escalation(
            equilibrium_score,
            pressure_index,
            stability_envelope
        )

        payload = {
            "timestamp": state.timestamp,
            "equilibrium_score": equilibrium_score,
            "pressure_index": pressure_index,
            "stability_envelope": stability_envelope,
            "escalation": escalation
        }

        deterministic_hash = _stable_hash(payload)
        self._last_hash = deterministic_hash

        return EquilibriumAssessment(
            equilibrium_score=equilibrium_score,
            disequilibrium_pressure_index=pressure_index,
            stability_envelope_index=stability_envelope,
            escalation_level=escalation,
            deterministic_hash=deterministic_hash
        )

    # --------------------------------------------------------
    # Signal Normalization
    # --------------------------------------------------------

    def _normalize_signals(
        self,
        signals: Tuple[EquilibriumSignal, ...]
    ) -> Dict[str, float]:

        domain_scores: Dict[str, float] = {}

        for s in signals:

            balance_component = s.balance_index * 0.35
            pressure_component = (1 - s.pressure_index) * 0.30
            resilience_component = s.resilience_index * 0.20
            adaptability_component = s.adaptability_index * 0.15

            score = _bounded(
                balance_component
                + pressure_component
                + resilience_component
                + adaptability_component
            )

            if s.domain in CIV_EQUILIBRIUM_DOMAINS:
                domain_scores[s.domain] = score

        return domain_scores

    # --------------------------------------------------------
    # Equilibrium Computations
    # --------------------------------------------------------

    def _compute_equilibrium_score(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 1.0

        return _bounded(sum(scores.values()) / len(scores))

    def _compute_disequilibrium_pressure(self, scores: Dict[str, float]) -> float:

        if len(scores) < 2:
            return 0.0

        values = list(scores.values())

        mean_val = sum(values) / len(values)
        variance = sum((v - mean_val) ** 2 for v in values) / len(values)

        return _bounded(math.sqrt(variance))

    def _compute_stability_envelope(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 0.0

        squared_sum = sum(v ** 2 for v in scores.values())
        return _bounded(math.sqrt(squared_sum / len(scores)))

    # --------------------------------------------------------
    # Escalation Logic
    # --------------------------------------------------------

    def _classify_escalation(
        self,
        equilibrium: float,
        pressure: float,
        stability: float
    ) -> str:

        if equilibrium < EQUILIBRIUM_CRITICAL_THRESHOLD or pressure > 0.65:
            return "CIVILIZATION_EQUILIBRIUM_CRITICAL"

        if equilibrium < EQUILIBRIUM_WARNING_THRESHOLD or pressure > 0.45:
            return "CIVILIZATION_EQUILIBRIUM_WARNING"

        if equilibrium < EQUILIBRIUM_STABLE_THRESHOLD:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner
# ============================================================

if __name__ == "__main__":

    sample_state = CivilizationEquilibriumState(
        timestamp=int(time.time()),
        signals=(
            EquilibriumSignal("resource_equilibrium", 0.63, 0.42, 0.58, 0.55),
            EquilibriumSignal("ecological_equilibrium", 0.58, 0.48, 0.54, 0.50),
            EquilibriumSignal("infrastructure_equilibrium", 0.61, 0.44, 0.57, 0.53),
            EquilibriumSignal("governance_equilibrium", 0.56, 0.46, 0.55, 0.52),
            EquilibriumSignal("technological_equilibrium", 0.60, 0.43, 0.56, 0.54),
        ),
    )

    engine = CivilizationEquilibriumPreservationArchitecture()
    result = engine.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))