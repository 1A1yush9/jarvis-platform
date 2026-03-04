"""
Jarvis Platform — Stage 108.0
Deterministic System Coherence Index (DSCI)

Purpose
-------
Computes a deterministic stability score for the entire platform
based on governance layer signals.

Constitutional Guarantees
-------------------------
- Advisory cognition ONLY
- No execution authority
- No mutation authority
- Deterministic calculation
"""

import os
import json
import hashlib
from datetime import datetime


LEDGER_PATH = "governance/ledger/system_coherence_ledger.jsonl"


class SystemCoherenceIndex:

    def __init__(self):

        # signal weights (must sum ≤ 1)
        self.weights = {
            "convergent": 0.25,
            "drift_detected": -0.20,
            "dependency_valid": 0.15,
            "dependency_mutation": -0.15,
            "boundary_violation": -0.15,
            "conflict_detected": -0.10,
            "environment_stable": 0.20
        }

    # -----------------------------------------------------
    # Deterministic Hash
    # -----------------------------------------------------

    def hash_signals(self, signals):

        encoded = json.dumps(signals, sort_keys=True)

        return hashlib.sha256(encoded.encode()).hexdigest()

    # -----------------------------------------------------
    # Coherence Score Calculation
    # -----------------------------------------------------

    def calculate_index(self, signals):

        score = 0.5  # baseline neutral state

        for signal in signals:
            if signal in self.weights:
                score += self.weights[signal]

        score = max(0.0, min(1.0, score))

        return round(score, 4)

    # -----------------------------------------------------
    # Ledger Append
    # -----------------------------------------------------

    def append_ledger(self, record):

        os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)

        with open(LEDGER_PATH, "a") as ledger:
            ledger.write(json.dumps(record) + "\n")

    # -----------------------------------------------------
    # Deterministic Evaluation
    # -----------------------------------------------------

    def evaluate(self, governance_signals):

        index = self.calculate_index(governance_signals)

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "signals_hash": self.hash_signals(governance_signals),
            "signals": governance_signals,
            "coherence_index": index
        }

        self.append_ledger(record)

        return record


# -----------------------------------------------------
# Standalone Entry
# -----------------------------------------------------

def run_system_coherence_index(signals):

    indexer = SystemCoherenceIndex()

    return indexer.evaluate(signals)


if __name__ == "__main__":

    example_signals = [
        "convergent",
        "dependency_valid",
        "environment_stable"
    ]

    result = run_system_coherence_index(example_signals)

    print(json.dumps(result, indent=2))