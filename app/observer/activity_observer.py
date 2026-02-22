# app/observer/activity_observer.py

import json
from pathlib import Path
from collections import Counter

LOG_PATH = Path("jarvis_events.json")


class ActivityObserver:
    """
    Stage-4.4 Observer Layer
    Reads system logs and extracts behavioral patterns.
    """

    def load_events(self):
        if not LOG_PATH.exists():
            return []

        try:
            return json.loads(LOG_PATH.read_text())
        except Exception:
            return []

    def action_statistics(self):
        events = self.load_events()

        actions = [
            e["payload"].get("action")
            for e in events
            if e["event_type"] == "action_validation"
        ]

        counter = Counter(actions)

        return {
            "total_events": len(events),
            "action_usage": dict(counter),
        }

    def system_summary(self):
        stats = self.action_statistics()

        return {
            "observer_active": True,
            "total_logged_events": stats["total_events"],
            "most_used_actions": sorted(
                stats["action_usage"].items(),
                key=lambda x: x[1],
                reverse=True,
            ),
        }


observer = ActivityObserver()