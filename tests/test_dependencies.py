import pytest
from app.api.dependencies import get_ai_client
from app.clients.openai_client import OpenAIClient
from app.clients.gemini_client import GeminiClient
from app.config import settings

@pytest.mark.parametrize(
    "provider, expected_cls",
    [
        ("openai", OpenAIClient),
        ("gemini", GeminiClient),
        ("qualquer_coisa", OpenAIClient),  # default
    ]
)
def test_get_ai_client_switches(provider, expected_cls):
    # altera dinamicamente o provedor em settings
    settings.ai_provider = provider
    client = get_ai_client()
    assert isinstance(client, expected_cls)