from fastapi import Depends
from app.config import settings
from app.services.ai_client import AIClient
from app.clients.openai_client import OpenAIClient
from app.clients.gemini_client import GeminiClient

def get_ai_client() -> AIClient:
    if settings.ai_provider.lower() == "gemini":
        return GeminiClient()
    return OpenAIClient()
