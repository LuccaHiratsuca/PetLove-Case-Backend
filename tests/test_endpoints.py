import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api.dependencies import get_ai_client
from app.services.ai_client import AIClient

def test_question_and_answer_success():
    
    class DummyAI(AIClient):
        async def ask(self, prompt: str) -> str:
            return "resposta dummy"

    # override da dependência
    app.dependency_overrides[get_ai_client] = lambda: DummyAI()
    client = TestClient(app)

    response = client.post("/api/question-and-answer", json={"question": "Teste"})
    assert response.status_code == 200
    assert response.json() == {"response": "resposta dummy"}

    # limpa overrides para não afetar outros testes
    app.dependency_overrides.clear()

def test_question_and_answer_validation_error():
    client = TestClient(app)
    response = client.post("/api/question-and-answer", json={})
    assert response.status_code == 422  # request body inválido