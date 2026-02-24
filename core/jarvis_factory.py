from app.jarvis_units.jarvis_lead import JarvisLead
from app.jarvis_units.jarvis_marketing import JarvisMarketing


class JarvisFactory:
    """
    Central registry for all Jarvis units.
    """

    def __init__(self):
        self.registry = {
            "jarvis-lead": {
                "class": JarvisLead,
                "role": "Lead Intelligence",
                "allowed_tasks": [
                    "Market Scan",
                    "Lead Discovery",
                    "Lead Validation",
                    "Opportunity Analysis"
                ]
            },
            "jarvis-marketing": {
                "class": JarvisMarketing,
                "role": "Marketing & Copy",
                "allowed_tasks": [
                    "Outreach Strategy",
                    "Copy Generation"
                ]
            }
        }

    def get(self, jarvis_id: str):
        if jarvis_id not in self.registry:
            raise ValueError(f"Jarvis '{jarvis_id}' not registered")

        return self.registry[jarvis_id]["class"]()

    def list_all(self):
        return {
            k: {
                "role": v["role"],
                "allowed_tasks": v["allowed_tasks"]
            }
            for k, v in self.registry.items()
        }
