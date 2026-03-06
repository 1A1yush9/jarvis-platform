# governance/api/perpetual_integrity_api.py
# Stage-178.0 — Advisory API Interface (Safe)

from __future__ import annotations

from governance.perpetual_integrity_monitor import PerpetualIntegrityMonitor


engine = PerpetualIntegrityMonitor()


def run_integrity_monitor_cycle() -> dict:
    return engine.run_integrity_cycle()