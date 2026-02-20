import logging
from app.core.executive.executive_decision_policy import (
    executive_decision_policy,
)
from app.core.executive.policy_models import ExecutionMode

logger = logging.getLogger(__name__)


class IncidentResponseEngine:
    """
    Applies automatic safety actions.
    """

    def respond(self, incidents):

        if not incidents:
            return

        for incident in incidents:
            logger.warning(
                f"[INCIDENT] {incident.type} - {incident.message}"
            )

            # High severity → SAFE MODE
            if incident.severity in ["high", "critical"]:
                executive_decision_policy.state.mode = (
                    ExecutionMode.SAFE
                )

                logger.warning(
                    "[IRS] Executive policy forced to SAFE MODE"
                )


incident_response_engine = IncidentResponseEngine()
