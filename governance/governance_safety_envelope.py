"""
Jarvis Platform — Stage 110.0
Deterministic Governance Safety Envelope (DGSE)

Purpose
-------
Ensures all governance signals remain within the
approved constitutional signal space.

Constitutional Guarantees
-------------------------
- Advisory cognition ONLY
- No execution authority
- No mutation authority
- Deterministic validation
"""

import os
import json
import hashlib
from datetime import datetime


LEDGER_PATH = "governance/ledger/governance_safety_envelope.jsonl"


class GovernanceSafetyEnvelope:

    def __init__(self):

        # approved governance signal space
        self.allowed_signals = {
            "convergent",
            "environment_stable",
            "drift_detected",
            "dependency_valid",
            "dependency_mutation",
            "boundary_violation",
            "conflict_detected"
        }

    # -----------------------------------------------------
    # Deterministic Hash
    # -----------------------------------------------------

    def hash_signals(self, signals):

        encoded = json.dumps(signals, sort_keys=True)

        return hashlib.sha256(encoded.encode()).hexdigest()

    # -----------------------------------------------------
    # Envelope Validation
    # -----------------------------------------------------

    def validate(self, signals):

        out_of_envelope = []

        for s in signals:
            if s not in self.allowed_signals:
                out_of_envelope.append(s)

        result = {
            "timestamp": datetime.utcnow().isoformat(),
            "signals_hash": self.hash_signals(signals),
            "signals": signals,
            "out_of_envelope_detected": len(out_of_envelope) > 0,
            "out_of_envelope_signals": out_of_envelope
        }

        return result

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

    def evaluate(self, signals):

        result = self.validate(signals)

        self.append_ledger(result)

        return result


# -----------------------------------------------------
# Standalone Entry
# -----------------------------------------------------

def run_governance_safety_envelope(signals):

    envelope = GovernanceSafetyEnvelope()

    return envelope.evaluate(signals)


if __name__ == "__main__":

    example_signals = [
        "convergent",
        "environment_stable",
        "dependency_valid"
    ]

    result = run_governance_safety_envelope(example_signals)

    print(json.dumps(result, indent=2))