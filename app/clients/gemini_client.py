import httpx
from app.config import settings
from app.services.ai_client import AIClient

class GeminiClient(AIClient):
    def __init__(self):
        self.base_url = "https://gemini.api.google.com/v1"
        self.api_key = settings.gemini_api_key

    async def ask(self, prompt: str) -> str:
        payload = {"prompt": prompt}
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{self.base_url}/chat", json=payload, headers=headers, timeout=30)
            r.raise_for_status()
            return r.json()["response"]