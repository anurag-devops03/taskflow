from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_ENV: str = "development"
    SECRET_KEY: str = "changeme"

    DATABASE_URL: str
    SYNC_DATABASE_URL: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
