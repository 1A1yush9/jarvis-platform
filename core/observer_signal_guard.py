# app/core/observer_signal_guard.py

from datetime import datetime, timedelta
import hashlib
import json
import logging

logger = logging.getLogger(__name__)


class ObserverSignalGuard:
    """
    Prevents repeated reactions to identical signals.
    """

    COOLDOWN_MINUTES = 20

    def __init__(self):
        self.last_signal_hash = None
        self.last_trigger_time = None

    # -------------------------------------------------
    # CREATE SIGNAL FINGERPRINT
    # -------------------------------------------------
    def _hash_signal(self, signal):

        data_string = json.dumps(signal, sort_keys=True)
        return hashlib.md5(data_string.encode()).hexdigest()

    # -------------------------------------------------
    # CHECK IF SAFE TO TRIGGER
    # -------------------------------------------------
    def allow_trigger(self, signal):

        new_hash = self._hash_signal(signal)

        # Same signal already handled
        if new_hash == self.last_signal_hash:

            if self.last_trigger_time:
                if datetime.utcnow() - self.last_trigger_time < timedelta(
                    minutes=self.COOLDOWN_MINUTES
                ):
                    logger.info(
                        "[SignalGuard] Duplicate signal ignored."
                    )
                    return False

        # Accept signal
        self.last_signal_hash = new_hash
        self.last_trigger_time = datetime.utcnow()

        return True
