import asyncio
import logging
from .incident_detector import incident_detector
from .incident_response_engine import incident_response_engine

logger = logging.getLogger(__name__)


class IncidentScheduler:

    INTERVAL_SECONDS = 60  # check every minute

    async def run_loop(self):

        logger.info("[IRS] Incident monitoring started")

        while True:
            try:
                incidents = incident_detector.detect()
                incident_response_engine.respond(incidents)
            except Exception as e:
                logger.error(f"[IRS ERROR] {e}")

            await asyncio.sleep(self.INTERVAL_SECONDS)


incident_scheduler = IncidentScheduler()
