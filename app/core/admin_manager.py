# app/core/admin_manager.py

from fastapi import HTTPException
from app.core.usage_meter import usage_meter
from app.core.client_context import client_context


class AdminManager:
    """
    Stage-5.3 Admin Control Layer
    Provides owner-level visibility and control.
    """

    # Change later via ENV variable
    ADMIN_KEY = "JARVIS_ADMIN_MASTER_KEY"

    def verify_admin(self, admin_key: str):
        if admin_key != self.ADMIN_KEY:
            raise HTTPException(status_code=403, detail="Invalid admin key")

    def system_clients(self):
        return client_context.clients

    def usage_overview(self):
        return usage_meter.usage


admin_manager = AdminManager()