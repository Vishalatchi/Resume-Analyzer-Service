from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME:str="Resume Analyzer"
    APP_VERSION:str="1.0.0"
    API_PREFIX:str="/api/v1"
    INFISICAL_URL: str = "https://app.infisical.com"
    ENVIRONMENT: str = "dev"
    GROQ_MODEL: str = "llama-3.3-70b-versatile"
    AI_TIMEOUT: int = 60
    MAX_FILE_SIZE: int = 5 * 1024 * 1024
    model_config = SettingsConfigDict(
        env_file = ".env",
        extra="ignore"
    )

settings=Settings()