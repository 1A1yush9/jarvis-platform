# ============================================================
# Jarvis Platform — Stage 142.0
# Governance Planetary-Risk Synchronization Grid (PRSG)
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

MODEL_VERSION = "142.0"
HASH_SALT = "jarvis_prsg_v142"

PLANETARY_RISK_DOMAINS = [
    "geopolitical",
    "economic",
    "environmental",
    "cyber",
    "infrastructure",
    "biosphere",
]

SYNC_CRITICAL_THRESHOLD = 0.42
SYNC_WARNING_THRESHOLD = 0.58
SYNC_STABLE_THRESHOLD = 0.72


# ============================================================
# Dataclasses
# ============================================================

@dataclass(frozen=True)
class PlanetaryRiskSignal:
    node_id: str
    domain: str
    severity: float  # 0.0–1.0
    velocity: float  # 0.0–1.0
    resilience: float  # 0.0–1.0


@dataclass(frozen=True)
class PlanetaryRiskState:
    timestamp: int
    signals: Tuple[PlanetaryRiskSignal, ...]


@dataclass(frozen=True)
class SynchronizationAssessment:
    synchronization_score: float
    drift_index: float
    convergence_index: float
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
# PRSG Engine
# ============================================================

class PlanetaryRiskSynchronizationGrid:

    def __init__(self) -> None:
        self._last_hash: str | None = None

    # --------------------------------------------------------
    # Public Evaluation Interface
    # --------------------------------------------------------

    def evaluate(self, state: PlanetaryRiskState) -> SynchronizationAssessment:

        normalized = self._normalize_signals(state.signals)

        sync_score = self._compute_sync_score(normalized)
        drift_index = self._compute_drift_index(normalized)
        convergence_index = self._compute_convergence(sync_score, drift_index)

        escalation = self._classify_escalation(sync_score, drift_index)

        payload = {
            "timestamp": state.timestamp,
            "sync_score": sync_score,
            "drift_index": drift_index,
            "convergence_index": convergence_index,
            "escalation": escalation,
        }

        deterministic_hash = _stable_hash(payload)
        self._last_hash = deterministic_hash

        return SynchronizationAssessment(
            synchronization_score=sync_score,
            drift_index=drift_index,
            convergence_index=convergence_index,
            escalation_level=escalation,
            deterministic_hash=deterministic_hash,
        )

    # --------------------------------------------------------
    # Normalization Layer
    # --------------------------------------------------------

    def _normalize_signals(
        self,
        signals: Tuple[PlanetaryRiskSignal, ...]
    ) -> Dict[str, List[float]]:

        domain_map: Dict[str, List[float]] = {d: [] for d in PLANETARY_RISK_DOMAINS}

        for s in signals:

            severity_component = s.severity
            velocity_component = s.velocity * 0.6
            resilience_component = (1 - s.resilience) * 0.4

            composite = _bounded(
                severity_component * 0.5
                + velocity_component * 0.3
                + resilience_component * 0.2
            )

            if s.domain in domain_map:
                domain_map[s.domain].append(composite)

        return domain_map

    # --------------------------------------------------------
    # Synchronization Computation
    # --------------------------------------------------------

    def _compute_sync_score(self, domain_map: Dict[str, List[float]]) -> float:

        domain_scores = []

        for domain in PLANETARY_RISK_DOMAINS:

            values = domain_map.get(domain, [])

            if not values:
                domain_scores.append(1.0)
                continue

            mean_val = sum(values) / len(values)
            variance = sum((v - mean_val) ** 2 for v in values) / len(values)

            sync = _bounded(1 - math.sqrt(variance))
            domain_scores.append(sync)

        return _bounded(sum(domain_scores) / len(domain_scores))

    def _compute_drift_index(self, domain_map: Dict[str, List[float]]) -> float:

        drift_vals = []

        for values in domain_map.values():

            if len(values) < 2:
                continue

            drift_vals.append(max(values) - min(values))

        if not drift_vals:
            return 0.0

        return _bounded(sum(drift_vals) / len(drift_vals))

    def _compute_convergence(self, sync: float, drift: float) -> float:
        return _bounded((sync * 0.7) + ((1 - drift) * 0.3))

    # --------------------------------------------------------
    # Escalation Logic
    # --------------------------------------------------------

    def _classify_escalation(self, sync: float, drift: float) -> str:

        if sync < SYNC_CRITICAL_THRESHOLD or drift > 0.65:
            return "PLANETARY_CRITICAL"

        if sync < SYNC_WARNING_THRESHOLD or drift > 0.45:
            return "PLANETARY_WARNING"

        if sync < SYNC_STABLE_THRESHOLD:
            return "ELEVATED_MONITORING"

        return "STABLE"


# ============================================================
# Deterministic Example Runner (Safe Advisory Mode)
# ============================================================

if __name__ == "__main__":

    sample_state = PlanetaryRiskState(
        timestamp=int(time.time()),
        signals=(
            PlanetaryRiskSignal("node-1", "economic", 0.44, 0.36, 0.61),
            PlanetaryRiskSignal("node-2", "economic", 0.48, 0.41, 0.58),
            PlanetaryRiskSignal("node-1", "environmental", 0.52, 0.47, 0.55),
            PlanetaryRiskSignal("node-3", "cyber", 0.39, 0.44, 0.63),
            PlanetaryRiskSignal("node-2", "infrastructure", 0.46, 0.38, 0.57),
            PlanetaryRiskSignal("node-4", "biosphere", 0.50, 0.43, 0.56),
        ),
    )

    grid = PlanetaryRiskSynchronizationGrid()
    result = grid.evaluate(sample_state)

    print(json.dumps(asdict(result), indent=2))