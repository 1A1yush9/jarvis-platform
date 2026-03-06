"""
Jarvis Platform — Stage-184.0
Civilizational Governance Perpetual Closure Sovereignty Layer

Deterministic | Advisory Only | Append-Only Safe | Render Compatible
"""

from __future__ import annotations

import hashlib
import json
import time
from typing import Dict, Any

from governance.closure_sovereignty_ledger import ClosureSovereigntyLedger


class PerpetualClosureSovereignty:

    STAGE_ID = "184.0"
    NAMESPACE = "CIVILIZATIONAL_GOVERNANCE_PERPETUAL_CLOSURE_SOVEREIGNTY"

    def __init__(self, ledger: ClosureSovereigntyLedger):
        self.ledger = ledger

    # ---------------------------------------------------------
    # Deterministic Hash
    # ---------------------------------------------------------

    @staticmethod
    def _hash(payload: Dict[str, Any]) -> str:
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(canonical.encode()).hexdigest()

    # ---------------------------------------------------------
    # Sovereignty Attestation Generator
    # ---------------------------------------------------------

    def generate_sovereignty_record(
        self,
        coherence_report: Dict[str, Any],
        harmonization_report: Dict[str, Any],
        stabilization_report: Dict[str, Any],
        convergence_report: Dict[str, Any],
        closure_report: Dict[str, Any]
    ) -> Dict[str, Any]:

        timestamp = int(time.time())

        payload = {
            "stage": self.STAGE_ID,
            "namespace": self.NAMESPACE,
            "timestamp": timestamp,
            "coherence_hash": self._hash(coherence_report),
            "harmonization_hash": self._hash(harmonization_report),
            "stabilization_hash": self._hash(stabilization_report),
            "convergence_hash": self._hash(convergence_report),
            "closure_hash": self._hash(closure_report),
            "sovereignty_state": "PERPETUALLY_SOVEREIGN",
            "sovereignty_lock": True,
            "deterministic": True,
            "execution_authority": False,
            "mutation_authority": False
        }

        payload["sovereignty_hash"] = self._hash(payload)

        self.ledger.append(payload)

        return payload

    # ---------------------------------------------------------
    # Continuity Verification
    # ---------------------------------------------------------

    def verify_sovereignty_continuity(self) -> Dict[str, Any]:

        records = self.ledger.read_all()

        continuity_valid = True
        previous_hash = None

        for record in records:

            expected_hash = self._hash(
                {k: v for k, v in record.items() if k != "sovereignty_hash"}
            )

            if expected_hash != record["sovereignty_hash"]:
                continuity_valid = False
                break

            if previous_hash and previous_hash == record["sovereignty_hash"]:
                continuity_valid = False
                break

            previous_hash = record["sovereignty_hash"]

        return {
            "stage": self.STAGE_ID,
            "continuity_valid": continuity_valid,
            "records_verified": len(records),
            "deterministic": True
        }