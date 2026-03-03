"""
Jarvis Platform — Stage-74.0
Governance Snapshot Compaction & Integrity-Preserving Compression Engine

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Deterministically compacts historical governance snapshots
while preserving cryptographic integrity chain.

This module:
- Accepts audit ledger entries
- Aggregates older entries into checkpoint blocks
- Preserves hash continuity
- Prevents unbounded ledger growth
- Never mutates original ledger directly

Design Guarantees:
------------------
- Deterministic compaction
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
import hashlib
from typing import Dict, Any, List


class GovernanceSnapshotCompactor:
    """
    Stage-74.0 Ledger Compaction Layer

    Protects against:
    - Unbounded audit ledger growth
    - Replay inefficiency
    - Integrity chain disruption
    """

    VERSION = "74.0"

    COMPACTION_THRESHOLD = 50  # minimum entries before compaction
    BLOCK_SIZE = 25            # entries per checkpoint block

    def __init__(self):
        self._lock = threading.Lock()
        self._last_compaction_hash = None
        self._last_report = None

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def compact(self, ledger_entries: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Perform deterministic ledger compaction.

        Parameters:
        -----------
        ledger_entries : list of ledger entries

        Returns:
        --------
        Compaction advisory report.
        """

        with self._lock:
            total_entries = len(ledger_entries)

            if total_entries < self.COMPACTION_THRESHOLD:
                return {
                    "compactor_version": self.VERSION,
                    "compaction_performed": False,
                    "reason": "INSUFFICIENT_ENTRIES",
                    "advisory_action": "PROCEED"
                }

            blocks = self._create_blocks(ledger_entries)
            checkpoint_hash = self._compute_checkpoint_hash(blocks)

            report = {
                "compactor_version": self.VERSION,
                "compaction_performed": True,
                "original_entries": total_entries,
                "block_count": len(blocks),
                "checkpoint_hash": checkpoint_hash,
                "advisory_action": "ARCHIVE_PREVIOUS_ENTRIES_AND_RETAIN_CHECKPOINT"
            }

            self._last_compaction_hash = checkpoint_hash
            self._last_report = report

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _create_blocks(self, entries: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
        """
        Deterministically split ledger entries into blocks.
        """
        return [
            entries[i:i + self.BLOCK_SIZE]
            for i in range(0, len(entries), self.BLOCK_SIZE)
        ]

    def _compute_checkpoint_hash(self, blocks: List[List[Dict[str, Any]]]) -> str:
        """
        Compute deterministic checkpoint hash for blocks.
        """
        serialized = str([
            sorted(block, key=lambda x: x.get("entry_index", 0))
            for block in blocks
        ])
        return hashlib.sha256(serialized.encode()).hexdigest()

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "compactor_version": self.VERSION,
            "last_compaction_hash": self._last_compaction_hash,
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_governance_snapshot_compactor() -> GovernanceSnapshotCompactor:
    """
    Backward compatible instantiation.
    """
    return GovernanceSnapshotCompactor()