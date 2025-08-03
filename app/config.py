from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configurações carregadas de .env
    """
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    gemini_api_key: str = Field(..., env="GEMINI_API_KEY")
    ai_provider: str = Field("openai", env="AI_PROVIDER")

    
    model_config = SettingsConfigDict(
        env_file=".env", # indica ao BaseSettings onde está o .env
        env_file_encoding="utf-8",
    )

settings = Settings()