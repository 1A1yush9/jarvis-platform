import asyncio
import logging
from .strategic_resource_allocator import strategic_resource_allocator

logger = logging.getLogger(__name__)


class AllocationScheduler:

    INTERVAL_SECONDS = 600  # every 10 minutes

    async def run_loop(self):

        logger.info("[SRA] Scheduler started")

        while True:
            try:
                strategic_resource_allocator.evaluate()
            except Exception as e:
                logger.error(f"[SRA ERROR] {e}")

            await asyncio.sleep(self.INTERVAL_SECONDS)


allocation_scheduler = AllocationScheduler()
