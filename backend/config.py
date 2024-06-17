from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent

# class AuthJWT(BaseModel):
#     # private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
#     # public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
#     algorithm: str = "RS256"
#     access_token_expire_minutes: int = 5


class Settings(BaseSettings):
    DB_URL: str = 'sqlite+aiosqlite:///' + str(BASE_DIR) + '/interview.db'
    # DB_USER: str
    # DB_PASS: str
    # DB_PORT: int
    # DB_HOST: str
    # DB_NAME: str
    DB_ECHO: bool = True
    # auth_jwt: AuthJWT = AuthJWT()

    # @property
    # def DB_URL(self) -> str:
    #     return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

print(settings.DB_URL)
