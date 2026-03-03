"""
Jarvis Platform — Stage-68.0
Deterministic Governance Audit Ledger & Replay Verifier

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Maintains an internal cryptographic ledger of governance reports
and enables deterministic replay verification.

This module:
- Records advisory snapshots
- Chains entries via SHA-256 hashes
- Verifies ledger continuity
- Detects tampering or discontinuity
- Never modifies external systems

Design Guarantees:
------------------
- Deterministic logic
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
import hashlib
from typing import Dict, Any, List


class GovernanceAuditLedger:
    """
    Stage-68.0 Governance Audit Integrity Layer

    Protects against:
    - Advisory history tampering
    - Ledger discontinuity
    - Replay inconsistency
    """

    VERSION = "68.0"

    def __init__(self):
        self._lock = threading.Lock()
        self._ledger: List[Dict[str, Any]] = []
        self._last_hash = "GENESIS"
        self._integrity_violation = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def record(self, aggregated_report: Dict[str, Any]) -> Dict[str, Any]:
        """
        Record governance snapshot into audit ledger.

        Parameters:
        -----------
        aggregated_report : dict
            Final governance snapshot (e.g., Stage-67 harmonized output)

        Returns:
        --------
        Ledger recording report.
        """

        with self._lock:
            entry_hash = self._compute_hash(aggregated_report, self._last_hash)

            ledger_entry = {
                "entry_index": len(self._ledger),
                "previous_hash": self._last_hash,
                "entry_hash": entry_hash,
                "report_fingerprint": self._fingerprint_report(aggregated_report)
            }

            self._ledger.append(ledger_entry)
            self._last_hash = entry_hash

            return {
                "ledger_version": self.VERSION,
                "entry_index": ledger_entry["entry_index"],
                "entry_hash": entry_hash,
                "ledger_length": len(self._ledger),
                "integrity_violation": False,
                "advisory_action": "PROCEED"
            }

    def verify_integrity(self) -> Dict[str, Any]:
        """
        Verify full ledger chain integrity.
        """

        with self._lock:
            previous_hash = "GENESIS"

            for entry in self._ledger:
                recalculated = self._compute_hash(
                    {"fingerprint": entry["report_fingerprint"]},
                    previous_hash
                )

                if recalculated != entry["entry_hash"]:
                    self._integrity_violation = True
                    return {
                        "ledger_version": self.VERSION,
                        "integrity_violation": True,
                        "containment_reason": "LEDGER_TAMPERING_DETECTED",
                        "advisory_action": "INITIATE_AUDIT_INVESTIGATION"
                    }

                previous_hash = entry["entry_hash"]

            self._integrity_violation = False

            return {
                "ledger_version": self.VERSION,
                "integrity_violation": False,
                "ledger_length": len(self._ledger),
                "advisory_action": "PROCEED"
            }

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _compute_hash(self, report: Dict[str, Any], previous_hash: str) -> str:
        """
        Compute deterministic chained hash.
        """
        serialized = str(sorted(report.items())) + previous_hash
        return hashlib.sha256(serialized.encode()).hexdigest()

    def _fingerprint_report(self, report: Dict[str, Any]) -> str:
        """
        Generate deterministic fingerprint of report.
        """
        serialized = str(sorted(report.items()))
        return hashlib.sha256(serialized.encode()).hexdigest()

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "ledger_version": self.VERSION,
            "ledger_length": len(self._ledger),
            "integrity_violation": self._integrity_violation,
            "last_hash": self._last_hash
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_governance_audit_ledger() -> GovernanceAuditLedger:
    """
    Backward compatible instantiation.
    """
    return GovernanceAuditLedger()