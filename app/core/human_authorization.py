# app/core/human_authorization.py

import uuid
import time

# In-memory approval store (Render safe)
APPROVAL_TOKENS = {}

TOKEN_EXPIRY_SECONDS = 300  # 5 minutes


def create_approval_request(action_payload: dict):
    """
    Generates a human approval token
    and stores pending action safely.
    """

    token = str(uuid.uuid4())

    APPROVAL_TOKENS[token] = {
        "payload": action_payload,
        "created_at": time.time(),
        "approved": False
    }

    return {
        "status": "AWAITING_HUMAN_APPROVAL",
        "approval_token": token,
        "action_preview": action_payload
    }


def approve_token(token: str):
    if token not in APPROVAL_TOKENS:
        return {"status": "INVALID_TOKEN"}

    APPROVAL_TOKENS[token]["approved"] = True

    return {"status": "APPROVED"}


def validate_token(token: str):

    data = APPROVAL_TOKENS.get(token)

    if not data:
        return False

    # Expiry protection
    if time.time() - data["created_at"] > TOKEN_EXPIRY_SECONDS:
        del APPROVAL_TOKENS[token]
        return False

    return data["approved"]


def consume_token(token: str):
    """
    Removes token after execution
    """
    if token in APPROVAL_TOKENS:
        payload = APPROVAL_TOKENS[token]["payload"]
        del APPROVAL_TOKENS[token]
        return payload

    return None