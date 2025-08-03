import pytest
from pydantic import ValidationError
from app.models.request import QuestionRequest
from app.models.response import AnswerResponse

@pytest.mark.parametrize("question", [
    "Qual a melhor ração para meu gato?",
    "Como escolher brinquedos para cachorro?",
])
def test_question_request_valid(question):
    """Deve criar QuestionRequest válido para strings de pergunta."""
    req = QuestionRequest(question=question)
    assert req.question == question

@pytest.mark.parametrize("payload", [
    {},                               # faltando campo
    {"invalid_field": "valor"},       # campo inesperado
    {"question": 123},                # tipo errado
])
def test_question_request_invalid(payload):
    """Deve lançar ValidationError para payloads inválidos."""
    with pytest.raises(ValidationError):
        QuestionRequest(**payload)

@pytest.mark.parametrize("response", [
    "Aqui está a resposta gerada.",
    "Outra resposta de teste.",
])
def test_answer_response_valid(response):
    """Deve criar AnswerResponse válido para strings de resposta."""
    resp = AnswerResponse(response=response)
    assert resp.response == response

@pytest.mark.parametrize("payload", [
    {},                              # faltando campo
    {"foo": "bar"},                  # campo inesperado
    {"response": 999},               # tipo errado
])
def test_answer_response_invalid(payload):
    """Deve lançar ValidationError para payloads inválidos."""
    with pytest.raises(ValidationError):
        AnswerResponse(**payload)
