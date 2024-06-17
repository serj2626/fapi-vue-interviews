from datetime import datetime, timedelta
from passlib.context import CryptContext
from pydantic import EmailStr
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def cteate_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=26)
    to_encode.update({"exp": expire})
    # encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)

    # return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    # user = await UserService.find_one_or_none(email=email)
    # if not user and not verify_password(password, user.hashed_password):
    #     return None

    # return user
    ...