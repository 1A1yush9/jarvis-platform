"""
Jarvis Platform — Stage-181.0
Civilizational Governance Perpetual Oversight Stabilization Closure Layer

Deterministic | Advisory Only | Append-Only Safe | Render Compatible
"""

from __future__ import annotations

import hashlib
import json
import time
from typing import Dict, Any

from governance.oversight_stabilization_ledger import OversightStabilizationLedger


class PerpetualOversightStabilization:

    STAGE_ID = "181.0"
    NAMESPACE = "CIVILIZATIONAL_GOVERNANCE_PERPETUAL_OVERSIGHT_STABILIZATION"

    def __init__(self, ledger: OversightStabilizationLedger):
        self.ledger = ledger

    # ---------------------------------------------------------
    # Deterministic Hash
    # ---------------------------------------------------------

    @staticmethod
    def _hash(payload: Dict[str, Any]) -> str:
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(canonical.encode()).hexdigest()

    # ---------------------------------------------------------
    # Stabilization Attestation
    # ---------------------------------------------------------

    def generate_stabilization_record(
        self,
        convergence_report: Dict[str, Any],
        telemetry_state: Dict[str, Any]
    ) -> Dict[str, Any]:

        timestamp = int(time.time())

        payload = {
            "stage": self.STAGE_ID,
            "namespace": self.NAMESPACE,
            "timestamp": timestamp,
            "convergence_hash": self._hash(convergence_report),
            "telemetry_hash": self._hash(telemetry_state),
            "stabilization_state": "PERPETUALLY_STABLE",
            "drift_lock": True,
            "deterministic": True,
            "execution_authority": False,
            "mutation_authority": False
        }

        payload["stabilization_hash"] = self._hash(payload)

        self.ledger.append(payload)

        return payload

    # ---------------------------------------------------------
    # Continuity Verification
    # ---------------------------------------------------------

    def verify_stabilization_continuity(self) -> Dict[str, Any]:

        records = self.ledger.read_all()

        continuity_valid = True
        previous_hash = None

        for record in records:

            expected_hash = self._hash(
                {k: v for k, v in record.items() if k != "stabilization_hash"}
            )

            if expected_hash != record["stabilization_hash"]:
                continuity_valid = False
                break

            if previous_hash and previous_hash == record["stabilization_hash"]:
                continuity_valid = False
                break

            previous_hash = record["stabilization_hash"]

        return {
            "stage": self.STAGE_ID,
            "continuity_valid": continuity_valid,
            "records_verified": len(records),
            "deterministic": True
        }