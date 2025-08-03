import openai
from app.config import settings
from app.services.ai_client import AIClient

class OpenAIClient(AIClient):
    def __init__(self):
        openai.api_key = settings.openai_api_key

    async def ask(self, prompt: str) -> str:
        resp = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": prompt}]
        )
        return resp.choices[0].message.content