from app.core.memory_models import CampaignMemory
from app.core.jarvis_factory import JarvisFactory


class Dispatcher:
    """
    Assigns tasks to Jarvis units via the factory.
    """

    def __init__(self):
        self.factory = JarvisFactory()

    def assign(self, task):
        if task.name in [
            "Market Scan",
            "Lead Discovery",
            "Lead Validation",
            "Opportunity Analysis"
        ]:
            return self.factory.get("jarvis-lead")

        if task.name in [
            "Outreach Strategy",
            "Copy Generation"
        ]:
            return self.factory.get("jarvis-marketing")

        raise ValueError(f"No Jarvis available for task: {task.name}")
