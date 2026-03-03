"""
Jarvis Platform — Stage 94.0
Immutable Causal Trace Ledger (ICTL)

Advisory-Only
Append-Only
Deterministic
No execution authority.
"""

import hashlib
import json
import time
from typing import Dict, Any, List


class ImmutableCausalTraceLedger:
    """
    Deterministic append-only causal trace ledger.
    Records certified advisory-state metadata.
    """

    STAGE_VERSION = "94.0"
    LEDGER_SEAL = "JARVIS_STAGE_94_CAUSAL_TRACE_LEDGER"

    def __init__(self):
        self._ledger: List[Dict[str, Any]] = []
        self._previous_hash = "GENESIS"

    # ------------------------------------------------------------------
    # Deterministic Hash Generator
    # ------------------------------------------------------------------

    def _hash_entry(self, entry: Dict[str, Any]) -> str:
        serialized = json.dumps(entry, sort_keys=True)
        return hashlib.sha256(serialized.encode()).hexdigest()

    # ------------------------------------------------------------------
    # Append Entry (Append-Only)
    # ------------------------------------------------------------------

    def append_trace(
        self,
        advisory_state: Dict[str, Any],
        attestation_report: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Appends a new causal trace entry.
        Requires attestation_passed == True.
        """

        if not attestation_report.get("attestation_passed", False):
            return {
                "stage": self.STAGE_VERSION,
                "ledger_append": False,
                "reason": "Attestation failed — entry rejected"
            }

        entry = {
            "timestamp": int(time.time()),
            "advisory_state": advisory_state,
            "attestation_hash": hashlib.sha256(
                json.dumps(attestation_report, sort_keys=True).encode()
            ).hexdigest(),
            "previous_hash": self._previous_hash
        }

        entry_hash = self._hash_entry(entry)
        entry["entry_hash"] = entry_hash

        self._ledger.append(entry)
        self._previous_hash = entry_hash

        return {
            "stage": self.STAGE_VERSION,
            "ledger_append": True,
            "entry_hash": entry_hash,
            "chain_integrity_preserved": True
        }

    # ------------------------------------------------------------------
    # Chain Integrity Verification
    # ------------------------------------------------------------------

    def verify_chain_integrity(self) -> bool:
        """
        Recompute entire chain to ensure no mutation occurred.
        Deterministic verification.
        """
        previous_hash = "GENESIS"

        for entry in self._ledger:
            expected_hash = self._hash_entry({
                "timestamp": entry["timestamp"],
                "advisory_state": entry["advisory_state"],
                "attestation_hash": entry["attestation_hash"],
                "previous_hash": previous_hash
            })

            if entry["entry_hash"] != expected_hash:
                return False

            previous_hash = entry["entry_hash"]

        return True

    # ------------------------------------------------------------------
    # Read-Only Ledger Access
    # ------------------------------------------------------------------

    def get_ledger_snapshot(self) -> List[Dict[str, Any]]:
        """
        Returns a copy of the ledger (read-only safe).
        """
        return list(self._ledger)


# ----------------------------------------------------------------------
# Factory Constructor
# ----------------------------------------------------------------------

def initialize_stage_94() -> ImmutableCausalTraceLedger:
    return ImmutableCausalTraceLedger()