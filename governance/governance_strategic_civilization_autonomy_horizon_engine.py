# ============================================================
# Jarvis Platform — Stage 146.0
# Governance Strategic Civilization Autonomy Horizon Engine (SCAHE)
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

MODEL_VERSION = "146.0"
HASH_SALT = "jarvis_scahe_v146"

CIV_AUTONOMY_DOMAINS = [
    "resource_autonomy",
    "technological_autonomy",
    "infrastructural_autonomy",
    "governance_autonomy",
    "strategic_resilience",
]

HORIZON_CRITICAL_THRESHOLD = 0.34
HORIZON_WARNING_THRESHOLD = 0.52
HORIZON_STABLE_THRESHOLD = 0.70


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class CivilizationAutonomySignal:
    domain: str
    autonomy_index: float  # 0.0–1.0
    sustainability_index: float  # 0.0–1.0
    volatility_index: float  # 0.0–1.0
    adaptability_index: float  # 0.0–1.0


@dataclass(frozen=True)
class CivilizationAutonomyState:
    timestamp: int
    signals: Tuple[CivilizationAutonomySignal, ...]


@dataclass(frozen=True)
class AutonomyHorizonAssessment:
    autonomy_horizon_score: float
    drift_index: float
    endurance_envelope_index: float
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
# SCAHE Engine
# ============================================================

class StrategicCivilizationAutonomyHorizonEngine:

    def __init__(self) -> None:
        self._last_hash: str | None = None

    # --------------------------------------------------------
    # Public Evaluation Interface
    # --------------------------------------------------------

    def evaluate(self, state: CivilizationAutonomyState) -> AutonomyHorizonAssessment:

        normalized = self._normalize_signals(state.signals)

        horizon_score = self._compute_horizon_score(normalized)
        drift_index = self._compute_drift(normalized)
        endurance_index = self._compute_endurance_envelope(normalized)

        escalation = self._classify_escalation(
            horizon_score,
            drift_index,
            endurance_index
        )

        payload = {
            "timestamp": state.timestamp,
            "horizon_score": horizon_score,
            "drift_index": drift_index,
            "endurance_index": endurance_index,
            "escalation": escalation,
        }

        deterministic_hash = _stable_hash(payload)
        self._last_hash = deterministic_hash

        return AutonomyHorizonAssessment(
            autonomy_horizon_score=horizon_score,
            drift_index=drift_index,
            endurance_envelope_index=endurance_index,
            escalation_level=escalation,
            deterministic_hash=deterministic_hash,
        )

    # --------------------------------------------------------
    # Normalization Layer
    # --------------------------------------------------------

    def _normalize_signals(
        self,
        signals: Tuple[CivilizationAutonomySignal, ...]
    ) -> Dict[str, float]:

        domain_scores: Dict[str, float] = {}

        for s in signals:

            autonomy_component = s.autonomy_index * 0.35
            sustainability_component = s.sustainability_index * 0.30
            adaptability_component = s.adaptability_index * 0.20
            volatility_component = (1 - s.volatility_index) * 0.15

            score = _bounded(
                autonomy_component
                + sustainability_component
                + adaptability_component
                + volatility_component
            )

            if s.domain in CIV_AUTONOMY_DOMAINS:
                domain_scores[s.domain] = score

        return domain_scores

    # --------------------------------------------------------
    # Horizon Computation
    # --------------------------------------------------------

    def _compute_horizon_score(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 1.0

        return _bounded(sum(scores.values()) / len(scores))

    def _compute_drift(self, scores: Dict[str, float]) -> float:

        if len(scores) < 2:
            return 0.0

        values = list(scores.values())
        mean_val = sum(values) / len(values)

        variance = sum((v - mean_val) ** 2 for v in values) / len(values)
        return _bounded(math.sqrt(variance))

    def _compute_endurance_envelope(self, scores: Dict[str, float]) -> float:

        if not scores:
            return 0.0

        squared_sum = sum(v ** 2 for v in scores.values())
        return _bounded(math.sqrt(squared_sum / len(scores)))

    # --------------------------------------------------------
    # Escalation Logic
    # --------------------------------------------------------

    def _classify_escalation(
        self,
        horizon: float,
        drift: float,
        endurance: float
    ) -> str:

        if horizon < HORIZON_CRITICAL_THRESHOLD or drift > 0.65:
            return "CIVILIZATION_HORIZON_CRITICAL"

        if horizon < HORIZON_WARNING_THRESHOLD or drift > 0.45:
            return "CIVILIZATION_HORIZON_WARNING"

        if horizon < HORIZON_STABLE_THRESHOLD:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner (Safe Advisory Mode)
# ============================================================

if __name__ == "__main__":

    sample_state = CivilizationAutonomyState(
        timestamp=int(time.time()),
        signals=(
            CivilizationAutonomySignal("resource_autonomy", 0.63, 0.59, 0.42, 0.55),
            CivilizationAutonomySignal("technological_autonomy", 0.61, 0.57, 0.44, 0.54),
            CivilizationAutonomySignal("infrastructural_autonomy", 0.58, 0.56, 0.47, 0.52),
            CivilizationAutonomySignal("governance_autonomy", 0.55, 0.53, 0.48, 0.50),
            CivilizationAutonomySignal("strategic_resilience", 0.52, 0.51, 0.49, 0.49),
        ),
    )

    engine = StrategicCivilizationAutonomyHorizonEngine()
    result = engine.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))