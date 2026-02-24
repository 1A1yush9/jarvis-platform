from datetime import datetime
from app.core.autonomy.goal_registry import goal_registry
from app.core.orchestrator.cognitive_orchestrator import (
    cognitive_orchestrator,
)
from .incident_models import Incident


class IncidentDetector:

    MAX_ACTIVE_GOALS = 12

    def detect(self):

        incidents = []

        active_goals = goal_registry.list_active()

        # ---------------------------------
        # Cognitive overload
        # ---------------------------------
        if len(active_goals) > self.MAX_ACTIVE_GOALS:
            incidents.append(
                Incident(
                    type="cognitive_overload",
                    severity="high",
                    message="Too many active goals",
                    detected_at=datetime.utcnow(),
                )
            )

        # ---------------------------------
        # Orchestrator failure
        # ---------------------------------
        if cognitive_orchestrator.current_state is None:
            incidents.append(
                Incident(
                    type="orchestrator_missing",
                    severity="critical",
                    message="Cognitive state unavailable",
                    detected_at=datetime.utcnow(),
                )
            )

        return incidents


incident_detector = IncidentDetector()
