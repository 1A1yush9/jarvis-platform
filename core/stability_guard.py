# app/core/stability_guard.py

import asyncio
import logging
from typing import Callable, Any, Awaitable

logger = logging.getLogger(__name__)


class StabilityGuard:
    """
    Production safety wrapper.
    Retries unstable async operations safely.
    """

    MAX_RETRIES = 2
    RETRY_DELAY = 2  # seconds

    async def run_safe(
        self,
        step_name: str,
        coro: Callable[[], Awaitable[Any]]
    ) -> Any:

        last_error = None

        for attempt in range(self.MAX_RETRIES + 1):
            try:
                return await coro()

            except Exception as e:
                last_error = e
                logger.warning(
                    f"[StabilityGuard] {step_name} failed "
                    f"(attempt {attempt+1}) : {str(e)}"
                )

                if attempt < self.MAX_RETRIES:
                    await asyncio.sleep(self.RETRY_DELAY)

        logger.error(
            f"[StabilityGuard] {step_name} permanently failed"
        )

        raise last_error
