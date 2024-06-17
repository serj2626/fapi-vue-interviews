from pydantic import BaseModel


class SUserCreate(BaseModel):
    username: str
    email: str
    password: str


class STokenInfo(BaseModel):
    access_token: str
    token_type: str