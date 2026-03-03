"""
Jarvis Platform — Stage 99.0
Deterministic Meta-Stability Sentinel (DMSS)

Advisory-Only
Deterministic
No execution authority.
No mutation authority.
"""

from typing import Dict, Any, List


class DeterministicMetaStabilitySentinel:
    """
    Evaluates cross-cycle structural stability.
    Detects oscillation, repeated near-boundary states,
    and long-horizon equilibrium degradation.
    """

    STAGE_VERSION = "99.0"
    STABILITY_SEAL = "JARVIS_STAGE_99_META_STABILITY_SENTINEL"

    def __init__(self, instability_threshold: int = 3):
        self.instability_threshold = instability_threshold

    # ------------------------------------------------------------------
    # Near-Boundary Detection
    # ------------------------------------------------------------------

    def _near_boundary(self, envelope_report: Dict[str, Any]) -> bool:
        """
        Detects if any envelope constraint is False
        while overall envelope still certified.
        """
        if not envelope_report.get("envelope_certified", False):
            return True

        for key, value in envelope_report.items():
            if key.endswith("_within_bound") or key.endswith("_static"):
                if value is False:
                    return True

        return False

    # ------------------------------------------------------------------
    # Stability Audit
    # ------------------------------------------------------------------

    def audit_meta_stability(
        self,
        recent_cycle_reports: List[Dict[str, Any]]
    ) -> Dict[str, Any]:

        if not recent_cycle_reports:
            return {
                "stage": self.STAGE_VERSION,
                "seal": self.STABILITY_SEAL,
                "meta_stability_certified": True,
                "note": "No historical cycles to evaluate"
            }

        instability_count = 0

        for cycle in recent_cycle_reports:
            envelope_report = cycle.get("envelope_report", {})
            consensus_report = cycle.get("consensus_report", {})
            temporal_report = cycle.get("temporal_report", {})

            if (
                not consensus_report.get("consensus_certified", True)
                or not temporal_report.get("temporal_integrity_certified", True)
                or self._near_boundary(envelope_report)
            ):
                instability_count += 1

        stable = instability_count < self.instability_threshold

        return {
            "stage": self.STAGE_VERSION,
            "seal": self.STABILITY_SEAL,
            "instability_events_detected": instability_count,
            "meta_stability_certified": stable
        }


# ----------------------------------------------------------------------
# Factory Constructor
# ----------------------------------------------------------------------

def initialize_stage_99(instability_threshold: int = 3) -> DeterministicMetaStabilitySentinel:
    return DeterministicMetaStabilitySentinel(instability_threshold)