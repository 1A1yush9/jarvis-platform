"""
Jarvis Platform — Stage 105.0
Deterministic Execution Surface Monitor (DESM)

Purpose
-------
Observes the runtime execution surface and detects structural drift.

Constitutional Guarantees
-------------------------
- Advisory cognition ONLY
- No execution authority
- No mutation authority
- Deterministic inspection only
"""

import hashlib
import os
import sys
import json
import time
import pkgutil
import platform

from datetime import datetime


LEDGER_PATH = "governance/ledger/execution_surface_ledger.jsonl"


class ExecutionSurfaceMonitor:

    def __init__(self):

        self.snapshot = {
            "timestamp": None,
            "python_version": None,
            "platform": None,
            "environment_hash": None,
            "loaded_modules_hash": None,
            "filesystem_root_hash": None
        }

    # -------------------------------------------------------
    # Environment Inspection
    # -------------------------------------------------------

    def inspect_environment(self):

        env_items = sorted([f"{k}={v}" for k, v in os.environ.items()])
        env_string = "|".join(env_items)

        env_hash = hashlib.sha256(env_string.encode()).hexdigest()

        return env_hash

    # -------------------------------------------------------
    # Loaded Module Inspection
    # -------------------------------------------------------

    def inspect_loaded_modules(self):

        modules = sorted([module.name for module in pkgutil.iter_modules()])
        modules_string = "|".join(modules)

        module_hash = hashlib.sha256(modules_string.encode()).hexdigest()

        return module_hash

    # -------------------------------------------------------
    # Filesystem Root Snapshot
    # -------------------------------------------------------

    def inspect_filesystem_root(self):

        root_items = []

        for root, dirs, files in os.walk(".", topdown=True):

            for name in files:
                path = os.path.join(root, name)
                root_items.append(path)

        root_items.sort()

        root_string = "|".join(root_items)

        root_hash = hashlib.sha256(root_string.encode()).hexdigest()

        return root_hash

    # -------------------------------------------------------
    # Runtime Snapshot
    # -------------------------------------------------------

    def capture_snapshot(self):

        self.snapshot["timestamp"] = datetime.utcnow().isoformat()

        self.snapshot["python_version"] = sys.version
        self.snapshot["platform"] = platform.platform()

        self.snapshot["environment_hash"] = self.inspect_environment()

        self.snapshot["loaded_modules_hash"] = self.inspect_loaded_modules()

        self.snapshot["filesystem_root_hash"] = self.inspect_filesystem_root()

        return self.snapshot

    # -------------------------------------------------------
    # Ledger Append
    # -------------------------------------------------------

    def append_to_ledger(self, snapshot):

        os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)

        with open(LEDGER_PATH, "a") as ledger:
            ledger.write(json.dumps(snapshot) + "\n")

    # -------------------------------------------------------
    # Deterministic Cycle
    # -------------------------------------------------------

    def run(self):

        snapshot = self.capture_snapshot()

        self.append_to_ledger(snapshot)

        return snapshot


# -------------------------------------------------------
# Standalone Deterministic Entry
# -------------------------------------------------------

def run_execution_surface_monitor():

    monitor = ExecutionSurfaceMonitor()

    snapshot = monitor.run()

    return snapshot


if __name__ == "__main__":

    result = run_execution_surface_monitor()

    print(json.dumps(result, indent=2))