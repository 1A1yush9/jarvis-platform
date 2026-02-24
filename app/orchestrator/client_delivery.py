# ==========================================================
# JARVIS AI — CLIENT DELIVERY ORCHESTRATOR
# Stage 11.1
# ==========================================================

from datetime import datetime
import uuid


class ClientDeliveryOrchestrator:
    """
    Converts strategic decisions into real client delivery pipelines.
    """

    def __init__(self):
        self.projects = {}

    # ------------------------------------------------------
    # Create New Client Project
    # ------------------------------------------------------
    def create_project(self, client_id, project_type, kpi_targets=None):

        project_id = str(uuid.uuid4())

        self.projects[project_id] = {
            "client_id": client_id,
            "project_type": project_type,
            "status": "pending",
            "created_at": datetime.utcnow(),
            "tasks": [],
            "kpi_targets": kpi_targets or {},
            "delivery_score": 0
        }

        return {
            "status": "created",
            "project_id": project_id
        }

    # ------------------------------------------------------
    # Generate Execution Tasks
    # ------------------------------------------------------
    def generate_tasks(self, project_id):

        project = self.projects.get(project_id)

        if not project:
            return {"error": "Project not found"}

        task_templates = {
            "SEO": [
                "Keyword Research",
                "Technical Audit",
                "On-page Optimization",
                "Content Plan",
                "Backlink Strategy"
            ],
            "Ads": [
                "Audience Research",
                "Ad Copy Creation",
                "Campaign Setup",
                "Budget Optimization",
                "Performance Monitoring"
            ],
            "Automation": [
                "Workflow Mapping",
                "Integration Setup",
                "Testing",
                "Deployment",
                "Monitoring"
            ],
            "Consulting": [
                "Business Audit",
                "Strategy Design",
                "Execution Roadmap",
                "Review Sessions"
            ]
        }

        tasks = task_templates.get(project["project_type"], [])

        project["tasks"] = [
            {
                "task": t,
                "completed": False,
                "timestamp": datetime.utcnow()
            }
            for t in tasks
        ]

        project["status"] = "active"

        return {"status": "tasks_generated", "tasks": tasks}

    # ------------------------------------------------------
    # Complete Task
    # ------------------------------------------------------
    def complete_task(self, project_id, task_name):

        project = self.projects.get(project_id)
        if not project:
            return {"error": "Project not found"}

        for task in project["tasks"]:
            if task["task"] == task_name:
                task["completed"] = True

        self._update_delivery_score(project_id)

        return {"status": "task_completed"}

    # ------------------------------------------------------
    # Delivery Score Calculation
    # ------------------------------------------------------
    def _update_delivery_score(self, project_id):

        project = self.projects[project_id]

        total = len(project["tasks"])
        completed = sum(1 for t in project["tasks"] if t["completed"])

        if total > 0:
            project["delivery_score"] = round((completed / total) * 100, 2)

        if project["delivery_score"] == 100:
            project["status"] = "completed"

    # ------------------------------------------------------
    # Project Status
    # ------------------------------------------------------
    def get_project_status(self, project_id):

        project = self.projects.get(project_id)

        if not project:
            return {"error": "Project not found"}

        return project