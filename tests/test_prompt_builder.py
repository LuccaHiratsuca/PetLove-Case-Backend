import pytest
from app.services.prompt_builder import PromptBuilder

@pytest.mark.parametrize(
    "question",
    [
        "Oi, qual a melhor ração?",
        "Como cuidar da pelagem do meu gato?",
    ]
)
def test_build_includes_persona_and_client_tag(question):
    prompt = PromptBuilder.build(question)

    assert PromptBuilder.PERSONA.strip() in prompt # Deve incluir a persona
    assert f"Cliente: {question}" in prompt # Deve incluir a linha com o cliente
    assert prompt.strip().endswith("Petlove Assistente:") # Deve terminar com o marcador do assistente