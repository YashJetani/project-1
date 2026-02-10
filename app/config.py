from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/todo_db"
    PROJECT_NAME: str = "Todo API"
    API_V1_STR: str = "/api/v1"


settings = Settings()