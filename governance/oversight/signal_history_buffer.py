from typing import Dict, List


class SignalHistoryBuffer:
    """
    Maintains a deterministic bounded history of governance signals.
    """

    MAX_HISTORY = 20

    def __init__(self):

        self._history: List[Dict] = []

    def record(self, signal: Dict):

        self._history.append(signal)

        if len(self._history) > self.MAX_HISTORY:
            self._history.pop(0)

    def snapshot(self) -> List[Dict]:

        return list(self._history)