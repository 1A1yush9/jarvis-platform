# ============================================================
# Jarvis Platform — Stage 141.0
# Governance Civilization-Scale Stability Model (GCSM)
# Deterministic | Advisory-Only | Ledger-Compatible
# ============================================================

from __future__ import annotations

import hashlib
import json
import math
import time
from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple

# ============================================================
# Deterministic Constants
# ============================================================

MODEL_VERSION = "141.0"
HASH_SALT = "jarvis_gcsm_v141"

# Civilization domains (fixed deterministic ordering)
CIV_DOMAINS = [
    "economic",
    "infrastructure",
    "environmental",
    "cyber",
    "governance",
]

# Stability thresholds (deterministic)
CIV_COLLAPSE_THRESHOLD = 0.32
GLOBAL_CRITICAL_THRESHOLD = 0.45
REGIONAL_CRITICAL_THRESHOLD = 0.55


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class DomainSignal:
    domain: str
    stress_index: float  # 0.0–1.0
    volatility_index: float  # 0.0–1.0
    resilience_index: float  # 0.0–1.0


@dataclass(frozen=True)
class CivilizationState:
    timestamp: int
    domains: Tuple[DomainSignal, ...]


@dataclass(frozen=True)
class StabilityAssessment:
    civilization_score: float
    regional_score: float
    global_score: float
    collapse_risk: float
    escalation_level: str
    deterministic_hash: str


# ============================================================
# Deterministic Utilities
# ============================================================

def _stable_hash(payload: Dict) -> str:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256((HASH_SALT + serialized).encode()).hexdigest()


def _bounded(value: float) -> float:
    return max(0.0, min(1.0, value))


# ============================================================
# Civilization Stability Engine
# ============================================================

class CivilizationScaleStabilityModel:

    def __init__(self) -> None:
        self._last_assessment_hash: str | None = None

    # --------------------------------------------------------
    # Core Stability Calculation
    # --------------------------------------------------------

    def evaluate(self, state: CivilizationState) -> StabilityAssessment:

        domain_scores = self._compute_domain_scores(state.domains)

        civilization_score = self._civilization_stability(domain_scores)
        regional_score = self._regional_stability(domain_scores)
        global_score = self._global_stability(domain_scores)

        collapse_risk = self._collapse_probability(civilization_score)

        escalation_level = self._escalation_classification(
            civilization_score,
            global_score,
            collapse_risk
        )

        payload = {
            "civilization_score": civilization_score,
            "regional_score": regional_score,
            "global_score": global_score,
            "collapse_risk": collapse_risk,
            "escalation_level": escalation_level,
            "timestamp": state.timestamp,
        }

        deterministic_hash = _stable_hash(payload)

        self._last_assessment_hash = deterministic_hash

        return StabilityAssessment(
            civilization_score=civilization_score,
            regional_score=regional_score,
            global_score=global_score,
            collapse_risk=collapse_risk,
            escalation_level=escalation_level,
            deterministic_hash=deterministic_hash,
        )

    # --------------------------------------------------------
    # Domain Computation
    # --------------------------------------------------------

    def _compute_domain_scores(
        self,
        domains: Tuple[DomainSignal, ...]
    ) -> Dict[str, float]:

        scores: Dict[str, float] = {}

        for d in domains:

            stress_component = 1.0 - d.stress_index
            volatility_component = 1.0 - (d.volatility_index * 0.7)
            resilience_component = d.resilience_index

            score = (
                (stress_component * 0.4)
                + (volatility_component * 0.25)
                + (resilience_component * 0.35)
            )

            scores[d.domain] = _bounded(score)

        return scores

    # --------------------------------------------------------
    # Multi-Layer Stability Models
    # --------------------------------------------------------

    def _civilization_stability(self, domain_scores: Dict[str, float]) -> float:
        weights = {
            "economic": 0.22,
            "infrastructure": 0.24,
            "environmental": 0.18,
            "cyber": 0.16,
            "governance": 0.20,
        }

        score = sum(domain_scores[d] * weights[d] for d in CIV_DOMAINS)
        return _bounded(score)

    def _regional_stability(self, domain_scores: Dict[str, float]) -> float:
        return _bounded(sum(domain_scores.values()) / len(domain_scores))

    def _global_stability(self, domain_scores: Dict[str, float]) -> float:
        squared = [v ** 2 for v in domain_scores.values()]
        return _bounded(math.sqrt(sum(squared) / len(squared)))

    # --------------------------------------------------------
    # Collapse Risk Modeling (Deterministic)
    # --------------------------------------------------------

    def _collapse_probability(self, civilization_score: float) -> float:

        if civilization_score >= 0.7:
            return 0.05

        if civilization_score <= CIV_COLLAPSE_THRESHOLD:
            return 0.92

        scaled = (0.7 - civilization_score) / (0.7 - CIV_COLLAPSE_THRESHOLD)
        return _bounded(0.05 + scaled * 0.87)

    # --------------------------------------------------------
    # Escalation Logic
    # --------------------------------------------------------

    def _escalation_classification(
        self,
        civ_score: float,
        global_score: float,
        collapse_risk: float
    ) -> str:

        if collapse_risk > 0.85:
            return "CIVILIZATION_EMERGENCY"

        if civ_score < GLOBAL_CRITICAL_THRESHOLD:
            return "GLOBAL_CRITICAL"

        if global_score < REGIONAL_CRITICAL_THRESHOLD:
            return "REGIONAL_CRITICAL"

        if civ_score < 0.70:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner (Safe Advisory Mode)
# ============================================================

if __name__ == "__main__":

    sample_state = CivilizationState(
        timestamp=int(time.time()),
        domains=(
            DomainSignal("economic", 0.41, 0.37, 0.52),
            DomainSignal("infrastructure", 0.46, 0.31, 0.58),
            DomainSignal("environmental", 0.55, 0.42, 0.49),
            DomainSignal("cyber", 0.39, 0.44, 0.54),
            DomainSignal("governance", 0.43, 0.36, 0.56),
        ),
    )

    model = CivilizationScaleStabilityModel()
    result = model.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))