from sqlalchemy import and_, insert, select

from database import async_session
from service import BaseCRUD

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
