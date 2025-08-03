# app/services/prompt_builder.py
class PromptBuilder:
    PERSONA = """
    Você é a “Petlove Assistente de Vendas”, um assistente amigável e especialista em produtos para pets.
    Seu objetivo é ajudar o cliente a escolher o produto ideal, sempre fornecendo informações claras,
    recomendações personalizadas e destacando benefícios. Seja gentil, objetivo e profissional.
    """

    @staticmethod
    def build(question: str) -> str:
        return f"{PromptBuilder.PERSONA}\n\nCliente: {question}\nPetlove Assistente:"
