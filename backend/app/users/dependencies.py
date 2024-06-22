from typing import Annotated

from fastapi import Depends, Form, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy import update

from app.core import async_session

from .auth import decode_jwt, get_password_hash, verify_password
from .crud import UserCRUD
from .models import User
from .schemas import SUserCreate

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login", scheme_name="JWT")


async def validate_user(username: str = Form(), password: str = Form()) -> User:
    user = await UserCRUD.find_one_or_none(username=username)

    if not user:
        raise HTTPException(status_code=401, detail="User Not Found")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    return user


def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
) -> dict:

    try:
        payload = decode_jwt(token=token)
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload


async def get_current_user(payload: dict = Depends(get_current_token_payload)) -> User:
    username = payload.get("username")

    if not username:
        raise HTTPException(status_code=400, detail="Invalid data")

    user = await UserCRUD.find_one_or_none(username=username)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid data")

    return user


async def get_user_for_email(request: Request) -> User:
    params = request.query_params
    email = params.get("email")

    if not email:
        raise HTTPException(status_code=400, detail="Invalid email")

    user = await UserCRUD.find_one_or_none(email=email)

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    return user


async def verification_user(user: User = Depends(get_user_for_email)) -> dict:
    query = (
        update(User)
        .where(User.email == user.email)
        .values(is_active=True, is_verified=True)
    )
    async with async_session() as session:
        await session.execute(query)
        await session.commit()
    return {"msg": "User verified", "email": user.email}


async def create_user(user_data: Annotated[SUserCreate, Depends()]):
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
    return True
