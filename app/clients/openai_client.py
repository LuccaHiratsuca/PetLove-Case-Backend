from openai import AsyncOpenAI, OpenAIError
from app.config import settings
from app.services.ai_client import AIClient

class OpenAIClient(AIClient):
    """
    Cliente para interação com a API OpenAI
    """

    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def ask(self, prompt: str) -> str:
        """
        Envia um prompt ao endpoint de chat completions e retorna o conteúdo da resposta.

        :param prompt: Prompt completo (já incluindo persona/contexto).
        :return: Conteúdo da primeira mensagem gerada pelo modelo.
        :raises RuntimeError: em caso de erro na API.
        """
        try:
            resp = await self.client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": prompt}],
            )
            return resp.choices[0].message.content
        except OpenAIError as e:
            raise RuntimeError(f"OpenAI API error: {e}")