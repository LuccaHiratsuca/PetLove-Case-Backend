import anyio
from google import genai
from app.config import settings
from app.services.ai_client import AIClient

class GeminiClient(AIClient):
    """
    Cliente para interação com a API Gemini.
    """

    def __init__(self):
        self.client = genai.Client(api_key=settings.gemini_api_key)

    async def ask(self, prompt: str) -> str:
        """
        Envia um prompt ao modelo Gemini e retorna o texto gerado.

        Como generate_content é síncrono, executamos em thread separada para não bloquear o event loop do FastAPI.
        """
        response = await anyio.to_thread.run_sync(
            lambda: self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
        )
        return response.text
