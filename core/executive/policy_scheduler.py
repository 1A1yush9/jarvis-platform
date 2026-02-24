import asyncio
import logging
from .executive_decision_policy import executive_decision_policy

logger = logging.getLogger(__name__)


class PolicyScheduler:

    INTERVAL_SECONDS = 300  # every 5 minutes

    async def run_loop(self):

        logger.info("[EDP] Scheduler started")

        while True:
            try:
                executive_decision_policy.evaluate()
            except Exception as e:
                logger.error(f"[EDP ERROR] {e}")

            await asyncio.sleep(self.INTERVAL_SECONDS)


policy_scheduler = PolicyScheduler()
