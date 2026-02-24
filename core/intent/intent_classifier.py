from .intent_models import StrategicIntent, IntentLevel
from .intent_registry import intent_registry


class IntentClassifier:

    def classify_goal(self, goal):

        title = goal.title.lower()

        if "performance" in title or "fix" in title:
            level = IntentLevel.SHORT

        elif "optimize" in title or "conversion" in title:
            level = IntentLevel.MID

        else:
            level = IntentLevel.LONG

        intent = StrategicIntent(
            title=goal.title,
            level=level,
            priority=goal.confidence
        )

        return intent_registry.add(intent)


intent_classifier = IntentClassifier()
