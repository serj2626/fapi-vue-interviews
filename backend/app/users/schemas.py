from pydantic import BaseModel, EmailStr, Field


class EmailSchema(BaseModel):
    email: list[EmailStr]


class SUserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=16)
    email: EmailStr = Field(min_length=6, max_length=100)
    password: str


class SUserAuth(BaseModel):
    username: str = Field(min_length=3, max_length=16)
    email: EmailStr = Field(min_length=6, max_length=100)
    password: str
    is_active: bool
    is_verified: bool


class SUserShow(SUserAuth):
    username: str
    email: EmailStr


class STokenInfo(BaseModel):
    access_token: str
    token_type: str
