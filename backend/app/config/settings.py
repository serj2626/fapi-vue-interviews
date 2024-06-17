from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict



print(Path(__file__).parent.parent)

class JWTSettings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


class Settings(BaseSettings):
    DB_URL: str = 'sqlite+aiosqlite:///./interview.db'
    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()

print(settings.DB_URL)
