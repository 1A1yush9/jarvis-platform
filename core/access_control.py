# core/access_control.py

"""
Stage-16.1 — Role-Based Intelligence Access
Controls permissions for Jarvis API usage.
"""

from typing import Dict, Any


class AccessControl:

    def __init__(self):

        # Simple internal role registry
        self.api_keys = {
            "OWNER_KEY": "owner",
            "ADMIN_KEY": "admin",
            "CLIENT_KEY": "client",
        }

        self.permissions = {
            "owner": ["analyze", "control"],
            "admin": ["analyze"],
            "client": ["analyze"],
            "viewer": []
        }

    # --------------------------------------------------
    # Resolve Role
    # --------------------------------------------------
    def get_role(self, api_key: str) -> str:
        return self.api_keys.get(api_key, "viewer")

    # --------------------------------------------------
    # Permission Check
    # --------------------------------------------------
    def allowed(self, role: str, action: str) -> bool:
        return action in self.permissions.get(role, [])