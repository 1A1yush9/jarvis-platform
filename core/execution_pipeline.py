# app/core/execution_pipeline.py

from app.core.human_authorization import (
    create_approval_request,
    validate_token,
    consume_token
)

from app.core.capability_gate import capability_check
from app.core.action_sandbox import sandbox_execute


def propose_action(action_payload: dict):
    """
    Called by Strategy Brain.
    Instead of executing — request approval.
    """

    return create_approval_request(action_payload)


def execute_with_token(token: str):
    """
    Execution allowed ONLY with valid human approval.
    """

    # Step 1 — Validate approval
    if not validate_token(token):
        return {
            "status": "DENIED",
            "reason": "Human approval missing or expired"
        }

    action_payload = consume_token(token)

    # Step 2 — Capability Gate validation
    gate = capability_check(action_payload)

    if gate["allowed"] is False:
        return {
            "status": "BLOCKED_BY_CAPABILITY_GATE",
            "details": gate
        }

    # Step 3 — Sandbox execution
    result = sandbox_execute(action_payload)

    return {
        "status": "EXECUTED",
        "result": result
    }