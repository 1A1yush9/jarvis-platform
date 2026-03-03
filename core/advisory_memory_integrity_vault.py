"""
Stage-83.0 — Advisory Memory Integrity Vault (AMIV)

Append-only advisory snapshot vault.
Cryptographically chained.
Bounded retention.
No execution authority.
"""

import hashlib
import json
from typing import Dict, Any, List
from datetime import datetime


class AdvisoryMemoryIntegrityVault:
    """
    Advisory Memory Integrity Vault

    - Append-only advisory record storage
    - Hash-chained ledger model
    - Bounded retention enforcement
    - Deterministic integrity verification
    """

    def __init__(self, max_entries: int = 100):
        self.max_entries = max_entries
        self.ledger: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # Deterministic Hash Utility
    # ------------------------------------------------------------------

    def _hash_entry(self, entry: Dict[str, Any]) -> str:
        encoded = json.dumps(entry, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    # ------------------------------------------------------------------
    # Append Advisory Snapshot
    # ------------------------------------------------------------------

    def append_snapshot(self, advisory_envelope: Dict[str, Any]) -> Dict[str, Any]:
        timestamp = datetime.utcnow().isoformat()

        previous_hash = self.ledger[-1]["entry_hash"] if self.ledger else None

        record = {
            "timestamp": timestamp,
            "previous_hash": previous_hash,
            "advisory_envelope": advisory_envelope
        }

        entry_hash = self._hash_entry(record)
        record["entry_hash"] = entry_hash

        self.ledger.append(record)

        # Enforce bounded retention
        if len(self.ledger) > self.max_entries:
            self.ledger.pop(0)

        return {
            "stage": "83.0",
            "entry_hash": entry_hash,
            "ledger_size": len(self.ledger),
            "advisory_mode": True,
            "execution_authority": False
        }

    # ------------------------------------------------------------------
    # Integrity Verification
    # ------------------------------------------------------------------

    def verify_integrity(self) -> Dict[str, Any]:
        for i in range(1, len(self.ledger)):
            expected_previous = self.ledger[i - 1]["entry_hash"]
            if self.ledger[i]["previous_hash"] != expected_previous:
                return {
                    "integrity_status": False,
                    "corrupted_index": i
                }

        return {
            "integrity_status": True,
            "total_entries": len(self.ledger)
        }

    # ------------------------------------------------------------------
    # Vault Seal
    # ------------------------------------------------------------------

    def generate_vault_seal(self) -> str:
        encoded = json.dumps(self.ledger, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()