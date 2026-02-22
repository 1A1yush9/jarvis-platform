# app/core/auth_manager.py

from fastapi import HTTPException

class AuthManager:
    """
    Stage-5.1 Authentication Layer
    Simple API-key validation.
    Future-ready for database integration.
    """

    # Demo keys (later move to DB or ENV)
    VALID_CLIENT_KEYS = {
        "agency_prayagraj": "JARVIS_KEY_001",
        "demo_client": "JARVIS_KEY_002",
    }

    def verify(self, client_id: str, api_key: str):

        expected_key = self.VALID_CLIENT_KEYS.get(client_id)

        if not expected_key:
            raise HTTPException(
                status_code=401,
                detail="Unknown client_id"
            )

        if api_key != expected_key:
            raise HTTPException(
                status_code=403,
                detail="Invalid API key"
            )

        return True


auth_manager = AuthManager()