from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext

from app.core import settings

private_key = settings.auth_jwt.private_key_path.read_text()
public_key = settings.auth_jwt.public_key_path.read_text()
algorithm = settings.auth_jwt.algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def encode_jwt(
    payload: dict,
    private_key: str = private_key,
    algorithm: str = algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:

    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str | bytes, public_key: str = public_key, algorithm: str = algorithm
) -> dict:

    decoded = jwt.decode(token, public_key, algorithms=[algorithm])

    return decoded
