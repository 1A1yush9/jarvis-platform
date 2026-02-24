from typing import Dict, List
from .intent_models import StrategicIntent


class IntentRegistry:

    def __init__(self):
        self.intents: Dict[str, StrategicIntent] = {}

    def add(self, intent: StrategicIntent):
        self.intents[intent.id] = intent
        return intent

    def list_all(self) -> List[StrategicIntent]:
        return list(self.intents.values())


intent_registry = IntentRegistry()
