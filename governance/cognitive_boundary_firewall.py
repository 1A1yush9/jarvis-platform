"""
Jarvis Platform — Stage 106.0
Deterministic Cognitive Boundary Firewall (DCBF)

Purpose
-------
Observes cognitive outputs and verifies they remain within
constitutional advisory scope.

Constitutional Guarantees
-------------------------
- Advisory cognition ONLY
- No execution authority
- No mutation authority
- Deterministic verification
"""

import hashlib
import json
import os
from datetime import datetime

LEDGER_PATH = "governance/ledger/cognitive_boundary_ledger.jsonl"


class CognitiveBoundaryFirewall:

    def __init__(self):

        # prohibited intent signals
        self.execution_markers = [
            "execute",
            "run command",
            "modify system",
            "install dependency",
            "delete file",
            "write file",
            "update configuration",
            "change environment",
        ]

    # -------------------------------------------------------
    # Deterministic Hash
    # -------------------------------------------------------

    def hash_output(self, output):

        return hashlib.sha256(output.encode()).hexdigest()

    # -------------------------------------------------------
    # Boundary Inspection
    # -------------------------------------------------------

    def inspect_output(self, output):

        lower = output.lower()

        violations = []

        for marker in self.execution_markers:

            if marker in lower:
                violations.append(marker)

        result = {
            "timestamp": datetime.utcnow().isoformat(),
            "output_hash": self.hash_output(output),
            "violation_detected": len(violations) > 0,
            "violations": violations
        }

        return result

    # -------------------------------------------------------
    # Ledger Append
    # -------------------------------------------------------

    def append_ledger(self, result):

        os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)

        with open(LEDGER_PATH, "a") as ledger:
            ledger.write(json.dumps(result) + "\n")

    # -------------------------------------------------------
    # Deterministic Verification Cycle
    # -------------------------------------------------------

    def verify(self, output):

        result = self.inspect_output(output)

        self.append_ledger(result)

        return result


# -------------------------------------------------------
# Standalone Entry
# -------------------------------------------------------

def verify_cognitive_output(output):

    firewall = CognitiveBoundaryFirewall()

    return firewall.verify(output)


if __name__ == "__main__":

    example = "System suggests executing a command."

    result = verify_cognitive_output(example)

    print(json.dumps(result, indent=2))