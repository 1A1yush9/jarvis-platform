import asyncio
import logging
from datetime import datetime

from app.core.autonomous_growth_brain import autonomous_growth_brain

logger = logging.getLogger(__name__)


class GrowthScheduler:
    """
    Runs strategic growth analysis periodically.

    SAFE DESIGN:
    - advisory only
    - no goal creation
    - no observer triggering
    """

    INTERVAL_SECONDS = 3600  # 1 hour

    def __init__(self):
        self.last_result = None

    async def run_loop(self):

        logger.info("[GrowthScheduler] Started")

        while True:
            try:
                result = autonomous_growth_brain.discover_growth_opportunities()

                self.last_result = {
                    "generated_at": datetime.utcnow().isoformat(),
                    "data": result,
                }

                logger.info(
                    "[GrowthScheduler] Growth analysis completed"
                )

            except Exception as e:
                logger.error(f"[GrowthScheduler ERROR] {e}")

            await asyncio.sleep(self.INTERVAL_SECONDS)


growth_scheduler = GrowthScheduler()
