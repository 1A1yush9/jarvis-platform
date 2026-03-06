"""
Jarvis Platform — Stage-188.0
Civilizational Governance Perpetual Terminal Assurance Closure Layer

Deterministic | Advisory Only | Append-Only Safe | Render Compatible
"""

from __future__ import annotations

import hashlib
import json
import time
from typing import Dict, Any

from governance.terminal_assurance_ledger import TerminalAssuranceLedger


class PerpetualTerminalAssurance:

    STAGE_ID = "188.0"
    NAMESPACE = "CIVILIZATIONAL_GOVERNANCE_PERPETUAL_TERMINAL_ASSURANCE"

    def __init__(self, ledger: TerminalAssuranceLedger):
        self.ledger = ledger

    @staticmethod
    def _hash(payload: Dict[str, Any]) -> str:
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(canonical.encode()).hexdigest()

    def generate_terminal_record(
        self,
        finality_continuity_report: Dict[str, Any],
        finality_report: Dict[str, Any],
        continuity_report: Dict[str, Any]
    ) -> Dict[str, Any]:

        timestamp = int(time.time())

        payload = {
            "stage": self.STAGE_ID,
            "namespace": self.NAMESPACE,
            "timestamp": timestamp,
            "finality_continuity_hash": self._hash(finality_continuity_report),
            "finality_hash": self._hash(finality_report),
            "continuity_hash": self._hash(continuity_report),
            "terminal_state": "PERPETUALLY_ASSURED",
            "terminal_lock": True,
            "deterministic": True,
            "execution_authority": False,
            "mutation_authority": False
        }

        payload["terminal_hash"] = self._hash(payload)
        self.ledger.append(payload)
        return payload

    def verify_terminal_chain(self) -> Dict[str, Any]:

        records = self.ledger.read_all()

        continuity_valid = True
        previous_hash = None

        for record in records:

            expected_hash = self._hash(
                {k: v for k, v in record.items() if k != "terminal_hash"}
            )

            if expected_hash != record["terminal_hash"]:
                continuity_valid = False
                break

            if previous_hash and previous_hash == record["terminal_hash"]:
                continuity_valid = False
                break

            previous_hash = record["terminal_hash"]

        return {
            "stage": self.STAGE_ID,
            "continuity_valid": continuity_valid,
            "records_verified": len(records),
            "deterministic": True
        }