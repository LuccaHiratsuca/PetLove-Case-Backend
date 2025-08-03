from typing import Protocol

class AIClient(Protocol):
    """
    Protocolo (interface) para clientes de IA.
    Define o método `ask` para enviar prompts e obter respostas.
    """

    async def ask(self, prompt: str) -> str:
        """
        Envia um prompt para o modelo de IA e retorna a resposta gerada.

        :param prompt: texto completo a ser enviado ao modelo (já incluindo persona, contexto, etc.).
        :return: string com a resposta do modelo de IA.
        """
        ...
