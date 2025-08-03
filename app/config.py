from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    gemini_api_key: str
    ai_provider: str = "openai"  # ou "gemini"

    class Config:
        env_file = ".env"

settings = Settings()
