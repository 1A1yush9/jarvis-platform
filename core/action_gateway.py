# app/core/action_gateway.py

from app.core.system_state import system_state
from app.monitoring.event_logger import event_logger


class ActionGateway:
    """
    Central execution validator.
    Every request must pass through here.
    """

    ALLOWED_ACTIONS = {
        "read": True,
        "analyze": True,
        "automation": False,   # controlled future feature
        "external": False,
    }

    def validate(self, action: str, payload: dict):

        # System health check
        health = system_state.health()
        if health["status"] != "ok":
            raise Exception("System not ready")

        # Permission check
        allowed = self.ALLOWED_ACTIONS.get(action, False)

        event_logger.log(
            "action_validation",
            {
                "action": action,
                "allowed": allowed,
            },
        )

        if not allowed:
            raise PermissionError(f"Action '{action}' is not allowed")

        return True


# Singleton
action_gateway = ActionGateway()