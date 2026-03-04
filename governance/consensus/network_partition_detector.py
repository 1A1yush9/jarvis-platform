from typing import Dict


class NetworkPartitionDetector:
    """
    Detects governance cluster partitions.

    A partition exists if multiple unique ledger hashes appear.
    """

    def detect(self, local_snapshot: Dict, peer_snapshots: Dict) -> Dict:

        hash_map = {}

        local_hash = local_snapshot["snapshot_hash"]

        hash_map.setdefault(local_hash, []).append("LOCAL_NODE")

        for peer, snap in peer_snapshots.items():

            peer_hash = snap.get("snapshot_hash")

            hash_map.setdefault(peer_hash, []).append(peer)

        partitions = len(hash_map)

        partition_detected = partitions > 1

        return {
            "partition_detected": partition_detected,
            "partition_count": partitions,
            "hash_groups": hash_map,
        }