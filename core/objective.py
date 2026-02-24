class ObjectiveBuilder:
    """
    Defines success criteria for a given intent.
    """

    def build(self, intent):
        return {
            "primary_objective": "Generate qualified leads",
            "context": {
                "industry": intent.industry,
                "location": intent.location
            },
            "success_criteria": {
                "min_leads": 50,
                "quality": "high",
                "personalization": True
            }
        }
