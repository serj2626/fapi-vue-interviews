from datetime import datetime

from fastapi import APIRouter, Depends, Request, Response


from .auth import encode_jwt
from .dependencies import (
    create_user,
    get_current_token_payload,
    get_current_user,
    validate_user,
    verification_user,
)
from .models import User
from .schemas import STokenInfo, SUserAuth

router = APIRouter(tags=["Пользователи && Авторизация"])


@router.post("/register", summary="Create new user", status_code=201)
async def register_user(request: Request, result: bool = Depends(create_user)):
    return {
        "msg": "Вы успешно зарегистрировались, для подтверждения аккаунта, перейдите на свою почту"
    }


@router.post(
    "/login",
    summary="Create access and refresh tokens for user",
    response_model=STokenInfo,
)
async def login_user(response: Response, user: SUserAuth = Depends(validate_user)):
    jwt_payload = {"sub": user.id, "username": user.username, "email": user.email}
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
async def confirm_email(email_to: str, result: dict = Depends(verification_user)):
    return result
