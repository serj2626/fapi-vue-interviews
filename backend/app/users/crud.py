from sqlalchemy import and_, insert, select, update

from app.core import async_session
from app.service import BaseCRUD

from .models import User


class UserCRUD(BaseCRUD):
    model = User

    @classmethod
    async def check_user_by_username_or_email(cls, username: str, email: str):
        async with async_session() as session:
            query = select(User).filter(
                and_(User.username == username, User.email == email)
            )
            res = await session.execute(query)
            return res.scalar_one_or_none()

    @classmethod
    async def user_is_active_verified(cls, username: str):
        async with async_session() as session:
            query = (
                select(User)
                .filter_by(username=username)
                .update({User.is_active: True, User.is_verified: True})
            )
            res = await session.execute(query)
            return res.scalar_one_or_none()
