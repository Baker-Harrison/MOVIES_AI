from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///dev.dv"

    class Config:
        env_file = ".env"

settings = Settings()
