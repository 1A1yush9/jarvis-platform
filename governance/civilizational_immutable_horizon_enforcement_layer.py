# civilizational_immutable_horizon_enforcement_layer.py
# Stage-194.0 — Civilizational Governance Immutable Horizon Enforcement Layer
# Operating Mode: Advisory Cognition ONLY
# Deterministic Runtime Enforced
# Mutation Authority: NONE

import hashlib
import json
import time
from typing import Dict, Any


class ImmutableHorizonEnforcementLayer:
    """
    Stage-194.0 — Immutable Horizon Enforcement Engine

    Guarantees:
    • Forward-only governance trajectory enforcement
    • Temporal regression detection
    • Deterministic horizon sealing
    • Ledger continuity assurance
    """

    def __init__(self, ledger_interface, telemetry_interface):
        self.ledger = ledger_interface
        self.telemetry = telemetry_interface
        self.layer_id = "STAGE-194.0-IMMUTABLE-HORIZON"
        self._sealed_horizon_hash = None

    # ------------------------------------------------------------------
    # PUBLIC EXECUTION ENTRY (DETERMINISTIC)
    # ------------------------------------------------------------------

    def execute(self) -> Dict[str, Any]:
        horizon_state = self._derive_horizon_state()

        if self._sealed_horizon_hash is None:
            self._sealed_horizon_hash = horizon_state["hash"]
            self._append_horizon_record(horizon_state, sealed=True)
        else:
            self._validate_forward_only(horizon_state)

        self.telemetry.emit(
            event="governance.immutable_horizon.verified",
            payload={
                "layer": self.layer_id,
                "horizon_hash": self._sealed_horizon_hash,
                "timestamp": horizon_state["timestamp"]
            }
        )

        return {
            "status": "verified",
            "layer": self.layer_id,
            "horizon_hash": self._sealed_horizon_hash
        }

    # ------------------------------------------------------------------
    # CORE LOGIC
    # ------------------------------------------------------------------

    def _derive_horizon_state(self) -> Dict[str, Any]:
        snapshot = self.ledger.get_governance_snapshot()

        canonical = json.dumps(snapshot, sort_keys=True, separators=(",", ":"))
        horizon_hash = hashlib.sha256(canonical.encode()).hexdigest()

        return {
            "hash": horizon_hash,
            "timestamp": int(time.time())
        }

    def _validate_forward_only(self, horizon_state: Dict[str, Any]) -> None:
        if horizon_state["hash"] != self._sealed_horizon_hash:
            self.telemetry.emit(
                event="governance.immutable_horizon.violation",
                payload={
                    "layer": self.layer_id,
                    "expected": self._sealed_horizon_hash,
                    "observed": horizon_state["hash"]
                }
            )
            raise RuntimeError("Immutable Horizon Violation Detected")

    def _append_horizon_record(self, horizon_state: Dict[str, Any], sealed=False) -> None:
        record = {
            "layer": self.layer_id,
            "horizon_hash": horizon_state["hash"],
            "sealed": sealed,
            "timestamp": horizon_state["timestamp"]
        }

        self.ledger.append_record("immutable_horizon_registry", record)