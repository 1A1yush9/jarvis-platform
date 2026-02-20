# app/core/reaction_task_manager.py

from datetime import datetime, timedelta
import uuid
import logging

from app.workflow.job_store import jobs
from app.workflow.orchestrator import run_workflow_background
from app.core.adaptive_action_selector import AdaptiveActionSelector
from app.agents.agent_manager import AgentManager

logger = logging.getLogger(__name__)


class ReactionTaskManager:
    """
    Creates autonomous workflow tasks from observer signals.
    """

    COOLDOWN_MINUTES = 15

    def __init__(self):
        self.last_trigger_time = None
        self.action_selector = AdaptiveActionSelector()
        self.agent_manager = AgentManager()

    # -------------------------------------------------
    # SAFETY CHECK
    # -------------------------------------------------
    def _cooldown_active(self):
        if not self.last_trigger_time:
            return False

        return (
            datetime.utcnow() - self.last_trigger_time
            < timedelta(minutes=self.COOLDOWN_MINUTES)
        )

    # -------------------------------------------------
    # CREATE REACTION TASK
    # -------------------------------------------------
    def create_reaction(self, signal):

        if signal["status"] == "stable":
            return

        if self._cooldown_active():
            logger.info("[ReactionManager] Cooldown active.")
            return

        logger.info("[ReactionManager] Creating autonomous task")

        job_id = str(uuid.uuid4())

        # ---- Select action ----
        action = self.action_selector.select_action(signal)

        # ---- Delegate agents ----
        agents = self.agent_manager.select_agents(
            action["action_type"]
        )

        input_data = {
            "industry": "auto_detected",
            "objective": action["action_type"],
            "priority": action["priority"],
            "agents": agents,
            "observer_generated": True,
            "trigger_reason": signal.get("reason"),
        }

        jobs[job_id] = {
            "status": "running",
            "source": "observer_reaction",
            "input": input_data,
        }

        run_workflow_background(job_id, input_data)

        self.last_trigger_time = datetime.utcnow()

        logger.info(f"[ReactionManager] Job started: {job_id}")
