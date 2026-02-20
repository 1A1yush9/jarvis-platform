import asyncio
import logging
from .self_reflection_engine import self_reflection_engine

logger = logging.getLogger(__name__)


class ReflectionScheduler:

    INTERVAL_SECONDS = 21600  # every 6 hours

    async def run_loop(self):

        logger.info("[Reflection] Scheduler started")

        while True:
            try:
                self_reflection_engine.reflect()
            except Exception as e:
                logger.error(f"[Reflection ERROR] {e}")

            await asyncio.sleep(self.INTERVAL_SECONDS)


reflection_scheduler = ReflectionScheduler()
