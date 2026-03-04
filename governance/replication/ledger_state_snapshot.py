import hashlib
import json
import os


class LedgerStateSnapshot:
    """
    Produces deterministic governance state snapshot hashes.
    """

    LEDGER_PATH = "governance/ledger/governance_ledger.jsonl"

    def compute_snapshot_hash(self) -> str:
        if not os.path.exists(self.LEDGER_PATH):
            return self._hash_bytes(b"")

        with open(self.LEDGER_PATH, "rb") as f:
            content = f.read()

        return self._hash_bytes(content)

    def compute_segment_hash(self, last_bytes: int = 4096) -> str:
        if not os.path.exists(self.LEDGER_PATH):
            return self._hash_bytes(b"")

        with open(self.LEDGER_PATH, "rb") as f:
            f.seek(0, os.SEEK_END)
            size = f.tell()
            f.seek(max(size - last_bytes, 0))
            segment = f.read()

        return self._hash_bytes(segment)

    def _hash_bytes(self, b: bytes) -> str:
        h = hashlib.sha256()
        h.update(b)
        return h.hexdigest()

    def snapshot_payload(self) -> dict:
        return {
            "snapshot_hash": self.compute_snapshot_hash(),
            "segment_hash": self.compute_segment_hash(),
        }