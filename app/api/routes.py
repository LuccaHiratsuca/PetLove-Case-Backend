from fastapi import APIRouter, Depends, HTTPException
from app.models.request import QuestionRequest
from app.models.response import AnswerResponse
from app.services.prompt_builder import PromptBuilder
from app.api.dependencies import get_ai_client

router = APIRouter()

@router.post("/question-and-answer", response_model=AnswerResponse)
async def question_and_answer(
    req: QuestionRequest,
    ai: get_ai_client = Depends()
):
    prompt = PromptBuilder.build(req.question)
    try:
        answer = await ai.ask(prompt)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    return AnswerResponse(response=answer)
