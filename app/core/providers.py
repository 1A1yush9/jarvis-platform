import os

def get_llm(provider: str):
    if not provider:
        raise ValueError("Provider is required")

    provider = provider.lower().strip()

    if provider == "groq":
        from app.providers.groq_provider import GroqProvider
        return GroqProvider(api_key=os.getenv("GROQ_API_KEY"))

    if provider == "gemini":
        from app.providers.gemini_provider import GeminiProvider
        return GeminiProvider(api_key=os.getenv("GEMINI_API_KEY"))

    raise ValueError(f"Unknown provider: {provider}")
