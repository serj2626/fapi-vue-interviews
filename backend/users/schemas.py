from pydantic import BaseModel, EmailStr, Field


class SUserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=16)
    email: EmailStr = Field(min_length=6, max_length=100)
    password: str


class STokenInfo(BaseModel):
    access_token: str
    token_type: str
