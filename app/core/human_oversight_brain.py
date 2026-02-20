# app/core/human_oversight_brain.py

from typing import Dict, Any, List
from datetime import datetime
import json
import os
import logging

logger = logging.getLogger(__name__)


class HumanOversightBrain:
    """
    Stores autopilot proposals and waits for
    human approval before execution.
    """

    QUEUE_PATH = "app/memory/approval_queue.json"

    def __init__(self):
        self._ensure_queue()

    # -------------------------------------------------
    # STORAGE
    # -------------------------------------------------
    def _ensure_queue(self):
        os.makedirs("app/memory", exist_ok=True)

        if not os.path.exists(self.QUEUE_PATH):
            with open(self.QUEUE_PATH, "w") as f:
                json.dump({"pending": []}, f)

    def _load(self):
        with open(self.QUEUE_PATH, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.QUEUE_PATH, "w") as f:
            json.dump(data, f, indent=2)

    # -------------------------------------------------
    # ADD PROPOSALS
    # -------------------------------------------------
    def submit_for_approval(
        self,
        autopilot_jobs: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:

        data = self._load()

        for job in autopilot_jobs:
            job["status"] = "pending_approval"
            job["submitted_at"] = datetime.utcnow().isoformat()

            data["pending"].append(job)

        self._save(data)

        return data["pending"]

    # -------------------------------------------------
    # APPROVE / REJECT
    # -------------------------------------------------
    def approve_job(self, job_id: str, approved_by: str):

        data = self._load()

        for job in data["pending"]:
            if job["job_id"] == job_id:
                job["status"] = "approved"
                job["approved_by"] = approved_by
                job["approved_at"] = datetime.utcnow().isoformat()

                self._save(data)
                return job

        return None

    def reject_job(self, job_id: str, rejected_by: str):

        data = self._load()

        for job in data["pending"]:
            if job["job_id"] == job_id:
                job["status"] = "rejected"
                job["rejected_by"] = rejected_by
                job["rejected_at"] = datetime.utcnow().isoformat()

                self._save(data)
                return job

        return None

    def get_pending(self):
        return self._load().get("pending", [])
