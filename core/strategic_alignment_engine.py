"""
Jarvis Platform — Stage 17.5
Strategic Alignment Engine

Advisory-only cognition layer.

Responsibilities:
- Evaluate strategic consistency
- Detect drift between decisions and objectives
- Provide alignment scoring
- Recommend advisory corrections

SAFE MODE:
No execution authority.
Read-only intelligence analysis.
"""

from datetime import datetime
from typing import Dict, Any, List


class StrategicAlignmentEngine:
    def __init__(self):
        self.engine_name = "Strategic Alignment Engine"
        self.version = "17.5"
        self.mode = "advisory_only"

    # -----------------------------------------------------
    # Core Alignment Evaluation
    # -----------------------------------------------------
    def evaluate_alignment(
        self,
        decisions: List[Dict[str, Any]],
        platform_objectives: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Evaluates whether strategic decisions align
        with platform objectives.
        """

        alignment_score = 0
        drift_flags = []
        recommendations = []

        total = max(len(decisions), 1)

        for decision in decisions:
            score, drift = self._evaluate_single_decision(
                decision, platform_objectives
            )

            alignment_score += score

            if drift:
                drift_flags.append(
                    {
                        "decision_id": decision.get("id"),
                        "reason": drift,
                    }
                )

        normalized_score = round((alignment_score / total), 2)

        # Advisory logic
        if normalized_score < 0.6:
            recommendations.append(
                "Strategic drift detected. Re-evaluate active priorities."
            )

        if normalized_score < 0.4:
            recommendations.append(
                "High misalignment risk. Executive review recommended."
            )

        return {
            "engine": self.engine_name,
            "version": self.version,
            "timestamp": datetime.utcnow().isoformat(),
            "alignment_score": normalized_score,
            "drift_flags": drift_flags,
            "recommendations": recommendations,
            "mode": self.mode,
        }

    # -----------------------------------------------------
    # Internal Decision Analysis
    # -----------------------------------------------------
    def _evaluate_single_decision(
        self,
        decision: Dict[str, Any],
        objectives: Dict[str, Any],
    ):
        """
        Lightweight deterministic scoring.
        No ML — production safe.
        """

        score = 1.0
        drift_reason = None

        revenue_priority = objectives.get("revenue_focus", True)
        safety_priority = objectives.get("safety_priority", True)

        if revenue_priority and not decision.get("revenue_impact"):
            score -= 0.4
            drift_reason = "No revenue contribution detected"

        if safety_priority and decision.get("risk_level") == "high":
            score -= 0.4
            drift_reason = "Violates safety preference"

        score = max(score, 0.0)

        return score, drift_reason

    # -----------------------------------------------------
    # Health Status
    # -----------------------------------------------------
    def status(self) -> Dict[str, Any]:
        return {
            "engine": self.engine_name,
            "version": self.version,
            "status": "operational",
            "mode": self.mode,
        }