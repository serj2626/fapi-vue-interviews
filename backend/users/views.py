from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from .auth import get_password_hash
from .crud import UserCRUD
from .schemas import SUserCreate

router = APIRouter(tags=["Пользователи && Авторизация"])


@router.get("/")
async def get_users():
    return {"message": "Hello World"}


@router.post("/register", status_code=201)
async def register_user(user_data: Annotated[SUserCreate, Depends()]):
    existing_user_by_email = await UserCRUD.find_one_or_none(email=user_data.email)

    existing_user_by_username = await UserCRUD.find_one_or_none(
        username=user_data.username
    )
    if existing_user_by_email or existing_user_by_username:
        raise HTTPException(status_code=400, detail="User already exists")

    hash_psw = get_password_hash(user_data.password)
    await UserCRUD.add_obj(
        username=user_data.username, email=user_data.email, password=hash_psw
    )
    return {
        "msg": "Вы успешно зарегистрировались, для подтверждения аккаунта, перейдите на свою почту"
    }


@router.post("/login")
async def login():
    return {"message": "Login successful"}
