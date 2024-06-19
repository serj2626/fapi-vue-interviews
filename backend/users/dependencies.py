
from fastapi import Depends, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError


from .auth import decode_jwt, verify_password
from .crud import UserCRUD
from .models import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/users/login",
    scheme_name="JWT"
)


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


async def verification_user():
    pass