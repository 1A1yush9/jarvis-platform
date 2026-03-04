"""
Jarvis Platform
Stage-129.0 — Governance Cross-Layer Causal Analysis Engine

Purpose
-------
Performs deterministic causal analysis across governance telemetry
signals to identify root influence chains between governance modules.

This module detects which governance layers are likely contributing
to systemic instability based on correlated signal degradation.

Key Guarantees
--------------
• Deterministic causal inference
• Read-only telemetry consumption
• Append-only ledger reporting
• No execution authority
• No mutation authority
"""

import hashlib
import json
import time
from typing import Dict, Any, List, Tuple


class GovernanceCrossLayerCausalAnalysisEngine:

    MODULE = "governance_cross_layer_causal_analysis_engine"
    STAGE = "129.0"

    def __init__(self, ledger):
        self.ledger = ledger

    # ------------------------------------------------------------

    def _hash(self, payload: Dict[str, Any]) -> str:
        encoded = json.dumps(payload, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    # ------------------------------------------------------------

    def _normalize(self, value: float) -> float:
        if value < 0:
            return 0.0
        if value > 1:
            return 1.0
        return round(value, 6)

    # ------------------------------------------------------------

    def _detect_causal_links(self, signals: Dict[str, float]) -> List[Tuple[str, str]]:
        """
        Identify deterministic causal relationships based on signal proximity.
        Modules degrading together are considered causally linked.
        """

        modules = list(signals.keys())
        links: List[Tuple[str, str]] = []

        for i in range(len(modules)):
            for j in range(i + 1, len(modules)):

                a = modules[i]
                b = modules[j]

                diff = abs(signals[a] - signals[b])

                if diff < 0.05:
                    links.append((a, b))

        return links

    # ------------------------------------------------------------

    def _identify_root_modules(self, signals: Dict[str, float]) -> List[str]:
        """
        Modules with lowest stability signals are considered root influences.
        """

        if not signals:
            return []

        min_val = min(signals.values())

        roots = []

        for module, value in signals.items():
            if abs(value - min_val) < 0.02:
                roots.append(module)

        return roots

    # ------------------------------------------------------------

    def analyze(self, telemetry_signals: Dict[str, float]) -> Dict[str, Any]:

        normalized = {}

        for module, value in telemetry_signals.items():
            normalized[module] = self._normalize(value)

        causal_links = self._detect_causal_links(normalized)

        root_modules = self._identify_root_modules(normalized)

        report = {
            "module": self.MODULE,
            "stage": self.STAGE,
            "timestamp": int(time.time()),
            "signals": normalized,
            "causal_links": causal_links,
            "root_influence_modules": root_modules
        }

        report["hash"] = self._hash(report)

        self.ledger.append(report)

        return report