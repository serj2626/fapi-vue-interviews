from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel

from pathlib import Path
from pprint import pprint


BASE_DIR = Path(__file__).resolve().parent


class APPConfig(BaseModel):
    title: str = "API"
    description: str = "API description"
    version: str = "1.0.0"


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_PORT: int
    DB_HOST: str
    DB_NAME: str
    DB_ECHO: bool = True

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    REDIS_HOST: str
    REDIS_PORT: int

    auth_jwt: AuthJWT = AuthJWT()
    app: APPConfig = APPConfig()

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

