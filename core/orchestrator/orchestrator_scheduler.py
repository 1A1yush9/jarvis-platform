import asyncio
import logging
from .cognitive_orchestrator import cognitive_orchestrator

logger = logging.getLogger(__name__)


class OrchestratorScheduler:

    INTERVAL_SECONDS = 120  # every 2 minutes

    async def run_loop(self):

        logger.info("[Orchestrator] Started")

        while True:
            try:
                cognitive_orchestrator.build_state()
            except Exception as e:
                logger.error(f"[Orchestrator ERROR] {e}")

            await asyncio.sleep(self.INTERVAL_SECONDS)


orchestrator_scheduler = OrchestratorScheduler()
