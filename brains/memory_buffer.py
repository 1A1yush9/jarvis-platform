# brains/memory_buffer.py

import time
from collections import deque


class MemoryBuffer:
    """
    Passive short-term cognitive memory.
    Stores recent signal snapshots.
    No reasoning or execution allowed.
    """

    def __init__(self):
        self.created_at = time.time()
        self.snapshots = deque(maxlen=50)

    # ---------------------------------
    # Store snapshot safely
    # ---------------------------------
    def store_snapshot(self, signal_report: dict):
        snapshot = {
            "timestamp": time.time(),
            "signals": signal_report
        }
        self.snapshots.append(snapshot)

    # ---------------------------------
    # Memory report
    # ---------------------------------
    def report(self):
        uptime = round(time.time() - self.created_at, 2)

        return {
            "status": "memory_active_passive",
            "uptime_seconds": uptime,
            "memory_size": len(self.snapshots),
            "recent_memory": list(self.snapshots)
        }


# global safe instance
memory_buffer = MemoryBuffer()