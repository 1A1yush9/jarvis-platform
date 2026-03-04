from typing import Dict


class ReplicationConsensus:
    """
    Deterministic verification of peer state.
    No mutation authority.
    Only validates consistency.
    """

    def evaluate(self, local_snapshot: dict, peer_snapshots: Dict[str, dict]) -> dict:

        mismatches = []
        matches = []

        local_hash = local_snapshot["snapshot_hash"]

        for peer, snapshot in peer_snapshots.items():

            if snapshot["snapshot_hash"] == local_hash:
                matches.append(peer)
            else:
                mismatches.append(
                    {
                        "peer": peer,
                        "peer_hash": snapshot["snapshot_hash"],
                        "local_hash": local_hash,
                    }
                )

        status = "CONSISTENT"

        if mismatches:
            status = "DIVERGENCE_DETECTED"

        return {
            "status": status,
            "matches": matches,
            "mismatches": mismatches,
        }