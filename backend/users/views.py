from datetime import datetime
from typing import Annotated
from sqlalchemy import update

from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import EmailStr
from core import async_session
from .auth import encode_jwt, get_password_hash
from .crud import UserCRUD
from .dependencies import (
    get_current_token_payload, get_current_user, validate_user
)
from .models import User
from .schemas import STokenInfo, SUserAuth, SUserCreate

router = APIRouter(tags=["Пользователи && Авторизация"])


@router.post("/register", summary="Create new user", status_code=201)
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


@router.post(
    "/login",
    summary="Create access and refresh tokens for user",
    response_model=STokenInfo,
)
async def login_user(response: Response, user: SUserAuth = Depends(validate_user)):
    jwt_payload = {"sub": user.id,
                   "username": user.username, "email": user.email}
    token = encode_jwt(payload=jwt_payload)
    # response.headers["Authorization"] = f"Bearer {token}"
    # response.set_cookie(key="access_token", value=token, httponly=True)
    return STokenInfo(access_token=token, token_type="Bearer")


@router.get("/user/me", summary="Get current user")
async def get_current_user(
    payload: dict = Depends(get_current_token_payload),
    user: User = Depends(get_current_user),
):
    iat = payload.get("iat")
    return {
        "username": user.username,
        "email": user.email,
        "login_date": datetime.fromtimestamp(iat),
    }


@router.get("/confirm-email/{email_to}")
async def confirm_email(email_to: str):
    user = await UserCRUD.find_one_or_none(email=email_to)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid data")

    query = update(User).where(User.email == email_to).values(
        is_active=True, is_verified=True)
    async with async_session() as session:
        await session.execute(query)
        await session.commit()

    return {"msg": "Ваша почта подтверждена"}
