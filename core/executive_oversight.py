"""
Stage-39.0 — Executive Oversight & Human Authority Interface

Advisory-only supervisory layer enforcing human authority
over all strategic intelligence outputs.

This module DOES NOT execute actions.
It only evaluates, constrains, and records oversight decisions.
"""

from datetime import datetime
from typing import Dict, Any, Optional
import uuid


class OversightDecision:
    """
    Represents a human authority decision applied to an advisory output.
    """

    def __init__(
        self,
        decision: str,
        reviewer: str,
        notes: Optional[str] = None,
    ):
        self.id = str(uuid.uuid4())
        self.decision = decision  # APPROVED | RESTRICTED | REJECTED | REVIEW_REQUIRED
        self.reviewer = reviewer
        self.notes = notes or ""
        self.timestamp = datetime.utcnow().isoformat()


class ExecutiveOversightInterface:
    """
    Central governance authority ensuring advisory cognition
    remains under human supervision.
    """

    VALID_DECISIONS = {
        "APPROVED",
        "RESTRICTED",
        "REJECTED",
        "REVIEW_REQUIRED",
    }

    def __init__(self):
        self.oversight_log = []
        self.active_constraints = {}

    # ---------------------------------------------------------
    # Oversight Evaluation
    # ---------------------------------------------------------

    def submit_for_review(
        self,
        advisory_payload: Dict[str, Any],
        confidence_score: float,
        risk_level: str,
    ) -> Dict[str, Any]:
        """
        Wrap intelligence output for human oversight.
        """

        return {
            "oversight_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "status": "PENDING_HUMAN_AUTHORITY",
            "confidence": confidence_score,
            "risk_level": risk_level,
            "payload": advisory_payload,
        }

    # ---------------------------------------------------------
    # Human Authority Decision
    # ---------------------------------------------------------

    def apply_human_decision(
        self,
        oversight_id: str,
        decision: str,
        reviewer: str,
        notes: Optional[str] = None,
    ) -> Dict[str, Any]:

        if decision not in self.VALID_DECISIONS:
            raise ValueError("Invalid oversight decision")

        record = OversightDecision(decision, reviewer, notes)

        log_entry = {
            "oversight_id": oversight_id,
            "decision_record": record.__dict__,
        }

        self.oversight_log.append(log_entry)

        # Apply containment logic
        if decision == "RESTRICTED":
            self.active_constraints[oversight_id] = "LIMITED_ADVISORY_SCOPE"

        if decision == "REJECTED":
            self.active_constraints[oversight_id] = "BLOCKED"

        return {
            "status": "HUMAN_AUTHORITY_APPLIED",
            "oversight_id": oversight_id,
            "decision": decision,
            "reviewer": reviewer,
        }

    # ---------------------------------------------------------
    # Constraint Check
    # ---------------------------------------------------------

    def evaluate_constraints(self, oversight_id: str) -> str:
        """
        Returns operational advisory allowance.
        """

        return self.active_constraints.get(
            oversight_id,
            "FULL_ADVISORY_ALLOWED"
        )

    # ---------------------------------------------------------
    # Audit Access
    # ---------------------------------------------------------

    def get_oversight_log(self):
        return {
            "entries": len(self.oversight_log),
            "log": self.oversight_log,
        }


# Singleton instance (system-wide authority layer)
executive_oversight = ExecutiveOversightInterface()