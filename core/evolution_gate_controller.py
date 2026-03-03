"""
Jarvis Platform — Stage-65.0
Deterministic Evolution Gate & Governance Version Controller

Operating Mode: Advisory Cognition ONLY
Execution Authority: NONE

Purpose:
--------
Controls governance stack version sequencing and prevents
cross-version instability or unsafe stage transitions.

This module:
- Validates stage version continuity
- Detects incompatible version combinations
- Prevents forward-stage injection without sequence
- Emits advisory evolution validation signals
- Never mutates system state

Design Guarantees:
------------------
- Deterministic logic
- Thread-safe
- No external side-effects
- Fully backward compatible
"""

import threading
from typing import Dict, Any, List


class EvolutionGateController:
    """
    Stage-65.0 Governance Evolution Guard

    Protects against:
    - Stage version discontinuity
    - Partial governance deployment
    - Incompatible module combinations
    """

    VERSION = "65.0"

    MIN_EXPECTED_STAGE = 50
    MAX_EXPECTED_STAGE = 65

    def __init__(self):
        self._lock = threading.Lock()
        self._last_report = None
        self._evolution_violation = False

    # ------------------------------------------------------------------
    # Public Interface
    # ------------------------------------------------------------------

    def validate_versions(self, module_versions: List[str]) -> Dict[str, Any]:
        """
        Validate governance module version continuity.

        Parameters:
        -----------
        module_versions : list of version strings (e.g., "58.0")

        Returns:
        --------
        Evolution validation report.
        """

        with self._lock:
            numeric_versions = self._parse_versions(module_versions)

            continuity_ok = self._check_continuity(numeric_versions)
            boundary_ok = self._check_boundaries(numeric_versions)

            containment_reason = self._evaluate_evolution(
                continuity_ok,
                boundary_ok
            )

            report = {
                "evolution_gate_version": self.VERSION,
                "detected_versions": sorted(numeric_versions),
                "continuity_ok": continuity_ok,
                "boundary_ok": boundary_ok,
                "evolution_violation": containment_reason is not None,
                "containment_reason": containment_reason,
                "advisory_action": self._recommended_action(containment_reason)
            }

            self._last_report = report
            self._evolution_violation = containment_reason is not None

            return report

    # ------------------------------------------------------------------
    # Internal Logic
    # ------------------------------------------------------------------

    def _parse_versions(self, versions: List[str]) -> List[int]:
        """
        Extract major stage numbers from version strings.
        """
        parsed = []

        for v in versions:
            try:
                major = int(float(v))
                parsed.append(major)
            except Exception:
                continue

        return parsed

    def _check_continuity(self, versions: List[int]) -> bool:
        """
        Ensures no stage gaps exist between min and max detected.
        """
        if not versions:
            return True

        expected_range = set(range(min(versions), max(versions) + 1))
        return expected_range.issubset(set(versions))

    def _check_boundaries(self, versions: List[int]) -> bool:
        """
        Ensures versions remain within expected governance boundaries.
        """
        for v in versions:
            if v < self.MIN_EXPECTED_STAGE or v > self.MAX_EXPECTED_STAGE:
                return False
        return True

    def _evaluate_evolution(
        self,
        continuity_ok: bool,
        boundary_ok: bool
    ) -> str | None:
        """
        Determine if evolution violation exists.
        """

        if not continuity_ok:
            return "STAGE_SEQUENCE_DISCONTINUITY"

        if not boundary_ok:
            return "STAGE_BOUNDARY_VIOLATION"

        return None

    def _recommended_action(self, reason: str | None) -> str:
        """
        Advisory-only recommended action.
        """

        if reason == "STAGE_SEQUENCE_DISCONTINUITY":
            return "REQUIRE_FULL_STACK_VERSION_ALIGNMENT"

        if reason == "STAGE_BOUNDARY_VIOLATION":
            return "BLOCK_UNAUTHORIZED_STAGE_TRANSITION"

        return "PROCEED"

    # ------------------------------------------------------------------
    # Health Snapshot
    # ------------------------------------------------------------------

    def health_status(self) -> Dict[str, Any]:
        return {
            "evolution_gate_version": self.VERSION,
            "evolution_violation": self._evolution_violation,
            "last_report": self._last_report
        }


# ----------------------------------------------------------------------
# Backward-Compatible Factory
# ----------------------------------------------------------------------

def get_evolution_gate_controller() -> EvolutionGateController:
    """
    Backward compatible instantiation.
    """
    return EvolutionGateController()