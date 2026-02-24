from app.schemas.intent import Intent


class IntentParser:
    """
    Converts raw user input into structured intent.
    Rule-based for now.
    """

    def parse(self, user_input: str) -> Intent:
        text = user_input.lower()

        # Goal
        if "lead" in text:
            goal = "lead_generation"
        else:
            goal = "unknown"

        # Industry
        if "builder" in text or "real estate" in text:
            industry = "real estate builders"
        else:
            industry = "general business"

        # Location
        if "delhi" in text:
            location = "Delhi"
        else:
            location = "Unknown"

        return Intent(
            goal=goal,
            industry=industry,
            location=location,
            outputs=["leads", "outreach_copy"]
        )
