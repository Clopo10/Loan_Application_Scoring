from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent

class Settings(BaseSettings):
    FRONTEND_CORS_ORIGINS: str
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", extra="ignore")

config = Settings()